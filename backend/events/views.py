import json
from datetime import datetime
from decimal import Decimal, InvalidOperation

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Event, EventRegistration

DEFAULT_EVENT_IMAGE = '/img/events.png'

try:
    import jdatetime

    HAS_JDATETIME = True
except ImportError:
    HAS_JDATETIME = False


def _safe_positive_int(value, default, max_value=None):
    try:
        value_int = int(value)
    except (TypeError, ValueError):
        return default
    if value_int <= 0:
        return default
    if max_value is not None and value_int > max_value:
        return max_value
    return value_int


def is_staff(user):
    return user.is_staff


def _image_url(image_field, default_url=None):
    if not image_field:
        return default_url
    try:
        if not image_field.storage.exists(image_field.name):
            return default_url
        return image_field.url
    except Exception:
        return default_url


def _event_image_url(event):
    return _image_url(event.cover_image) or _image_url(event.image) or DEFAULT_EVENT_IMAGE


def calculate_event_dates(event_year, event_month):
    if not event_year or not event_month:
        return None, None
    try:
        if HAS_JDATETIME:
            persian_start = jdatetime.date(event_year, event_month, 1)
            gregorian_start = persian_start.togregorian()
            if event_month < 12:
                persian_end = jdatetime.date(event_year, event_month + 1, 1) - jdatetime.timedelta(days=1)
            else:
                persian_end = jdatetime.date(event_year + 1, 1, 1) - jdatetime.timedelta(days=1)
            gregorian_end = persian_end.togregorian()
            return gregorian_start, gregorian_end

        approx_year = event_year + 621
        approx_month = min(event_month, 12)
        start_date = datetime(approx_year, approx_month, 1).date()
        if approx_month == 12:
            end_date = datetime(approx_year, approx_month, 31).date()
        elif approx_month in (4, 6, 9, 11):
            end_date = datetime(approx_year, approx_month, 30).date()
        elif approx_month == 2:
            end_date = datetime(approx_year, approx_month, 28).date()
        else:
            end_date = datetime(approx_year, approx_month, 31).date()
        return start_date, end_date
    except Exception:
        return None, None


def _normalize_event_dates(item):
    legacy_start, legacy_end = calculate_event_dates(item.event_year, item.event_month)
    event_date = item.event_date or legacy_start
    registration_date = item.registration_date or item.registration_deadline
    return event_date, registration_date, legacy_end


def _get_event_status(item, event_date=None):
    today = timezone.localdate()
    registration_deadline = item.registration_date or item.registration_deadline
    effective_event_date = event_date

    has_ended = bool(effective_event_date and effective_event_date < today)
    registration_open = bool(not has_ended and item.is_registration_open)

    if has_ended:
        status_code = 'ended'
    elif registration_open:
        status_code = 'registration_open'
    else:
        status_code = 'registration_closed'

    return {
        'has_ended': has_ended,
        'is_registration_open': registration_open,
        'status_code': status_code,
        'registration_deadline': registration_deadline,
    }


def _serialize_event(item):
    event_date, registration_date, legacy_end = _normalize_event_dates(item)
    status = _get_event_status(item, event_date)
    return {
        'id': item.id,
        'title': item.title,
        'slug': item.slug,
        'description': item.description,
        'short_description': item.short_description or '',
        'event_type': item.get_event_type_display(),
        'event_type_code': item.event_type,
        'image': _event_image_url(item),
        'location': item.location,
        'event_month': item.event_month,
        'event_year': item.event_year,
        'event_date': event_date.isoformat() if event_date else None,
        'registration_date': registration_date.isoformat() if registration_date else None,
        'start_date': event_date.isoformat() if event_date else None,
        'end_date': legacy_end.isoformat() if legacy_end else None,
        'registration_deadline': status['registration_deadline'].isoformat() if status['registration_deadline'] else None,
        'retraining_number': item.retraining_number,
        'max_participants': item.max_participants,
        'price': float(item.price),
        'organizer': item.organizer or '',
        'target_audience': item.target_audience or '',
        'prerequisites': item.prerequisites or '',
        'agenda': item.agenda or '',
        'speakers': item.speakers or '',
        'contact_info': item.contact_info or '',
        'is_published': item.is_published,
        'is_featured': item.is_featured,
        'is_registration_open': status['is_registration_open'],
        'has_ended': status['has_ended'],
        'status_code': status['status_code'],
        'views': item.views,
        'created_at': item.created_at.isoformat(),
        'updated_at': item.updated_at.isoformat(),
    }


def _parse_form_date(value):
    if value in (None, '', 'null'):
        return None
    parsed = parse_date(value)
    if parsed:
        return parsed
    raise ValueError(f'فرمت تاریخ معتبر نیست: {value}')


def _sync_legacy_fields(event, event_date):
    if not event_date:
        return

    if HAS_JDATETIME:
        jalali_date = jdatetime.date.fromgregorian(date=event_date)
        event.event_year = jalali_date.year
        event.event_month = jalali_date.month


@require_http_methods(["GET"])
def event_list(request):
    queryset = Event.objects.all() if request.user.is_authenticated and request.user.is_staff else Event.objects.filter(is_published=True)
    events = queryset.order_by('-event_date', '-event_year', '-event_month', '-created_at')

    event_type = request.GET.get('type')
    if event_type:
        events = events.filter(event_type=event_type)

    page = _safe_positive_int(request.GET.get('page'), 1)
    per_page = _safe_positive_int(request.GET.get('per_page'), 10, max_value=50)
    paginator = Paginator(events, per_page)
    page_obj = paginator.get_page(page)

    return JsonResponse({
        'success': True,
        'events': [_serialize_event(item) for item in page_obj],
        'pagination': {
            'page': page_obj.number,
            'pages': paginator.num_pages,
            'total': paginator.count,
            'has_next': page_obj.has_next(),
            'has_prev': page_obj.has_previous(),
        },
    })


@require_http_methods(["GET"])
def event_detail(request, slug):
    queryset = Event.objects.all() if request.user.is_authenticated and request.user.is_staff else Event.objects.filter(is_published=True)
    event = get_object_or_404(queryset, slug=slug)
    if event.is_published:
        event.views += 1
        event.save(update_fields=['views'])

    is_registered = False
    if request.user.is_authenticated:
        is_registered = EventRegistration.objects.filter(event=event, user=request.user).exists()

    payload = _serialize_event(event)
    payload['is_registered'] = is_registered
    return JsonResponse({'success': True, 'event': payload})


@csrf_exempt
@login_required
@require_http_methods(["POST"])
def event_register(request, id):
    try:
        event = get_object_or_404(Event, id=id, is_published=True)
        status = _get_event_status(event, _normalize_event_dates(event)[0])
        if not status['is_registration_open']:
            return JsonResponse({'success': False, 'errors': 'مهلت ثبت نام به پایان رسیده است'}, status=400)

        if EventRegistration.objects.filter(event=event, user=request.user).exists():
            return JsonResponse({'success': False, 'errors': 'شما قبلاً در این رویداد ثبت نام کرده‌اید'}, status=400)

        if event.max_participants and EventRegistration.objects.filter(event=event).count() >= event.max_participants:
            return JsonResponse({'success': False, 'errors': 'ظرفیت رویداد تکمیل شده است'}, status=400)

        registration = EventRegistration.objects.create(event=event, user=request.user)
        return JsonResponse({'success': True, 'message': 'ثبت نام با موفقیت انجام شد', 'registration': {'id': registration.id, 'event': event.title}})
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=400)


def _parse_price(value):
    if value in (None, '', 'null'):
        return Decimal('0')
    try:
        return Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ValueError(f'فرمت مبلغ معتبر نیست: {value}') from exc


def _parse_max_participants(value):
    if value in (None, '', 'null'):
        return None
    return int(value)


def _apply_event_data(event, data, files=None):
    files = files or {}
    for field in ('title', 'slug', 'description', 'short_description', 'event_type', 'location', 'organizer', 'target_audience', 'prerequisites', 'agenda', 'speakers', 'contact_info', 'retraining_number'):
        if field in data:
            setattr(event, field, data.get(field) or '')

    if 'is_published' in data:
        event.is_published = str(data.get('is_published')).lower() == 'true' if not isinstance(data.get('is_published'), bool) else data.get('is_published')
    if 'is_featured' in data:
        event.is_featured = str(data.get('is_featured')).lower() == 'true' if not isinstance(data.get('is_featured'), bool) else data.get('is_featured')
    if 'price' in data:
        event.price = _parse_price(data.get('price'))
    if 'max_participants' in data:
        event.max_participants = _parse_max_participants(data.get('max_participants'))
    if 'event_year' in data and data.get('event_year') not in (None, '', 'null'):
        event.event_year = int(data.get('event_year'))
    if 'event_month' in data and data.get('event_month') not in (None, '', 'null'):
        event.event_month = int(data.get('event_month'))
    if 'event_date' in data:
        event.event_date = _parse_form_date(data.get('event_date'))
    if 'registration_date' in data:
        event.registration_date = _parse_form_date(data.get('registration_date'))
        event.registration_deadline = event.registration_date
    if 'registration_deadline' in data and 'registration_date' not in data:
        event.registration_deadline = _parse_form_date(data.get('registration_deadline'))

    _sync_legacy_fields(event, event.event_date)

    if 'cover_image' in files:
        event.cover_image = files['cover_image']


@csrf_exempt
@login_required
@user_passes_test(is_staff)
@require_http_methods(["POST"])
def event_create(request):
    try:
        event = Event(created_by=request.user)
        _apply_event_data(event, request.POST, request.FILES)
        event.save()
        return JsonResponse({'success': True, 'message': 'رویداد با موفقیت ایجاد شد', 'event': {'id': event.id, 'title': event.title}})
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=400)


@csrf_exempt
@login_required
@user_passes_test(is_staff)
@require_http_methods(["PUT", "POST"])
def event_update(request, id):
    try:
        event = get_object_or_404(Event, id=id)
        if request.content_type and 'application/json' in request.content_type:
            data = json.loads(request.body)
            _apply_event_data(event, data)
        else:
            _apply_event_data(event, request.POST, request.FILES)
        event.save()
        return JsonResponse({'success': True, 'message': 'رویداد با موفقیت بروزرسانی شد', 'event': {'id': event.id, 'title': event.title}})
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=400)


@csrf_exempt
@login_required
@user_passes_test(is_staff)
@require_http_methods(["DELETE"])
def event_delete(request, id):
    try:
        event = get_object_or_404(Event, id=id)
        event.delete()
        return JsonResponse({'success': True, 'message': 'رویداد با موفقیت حذف شد'})
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=400)
