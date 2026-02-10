from datetime import datetime, timedelta
from decimal import Decimal, InvalidOperation

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import json
from .models import Event, EventRegistration

# Try to import jdatetime for Persian date conversion
try:
    import jdatetime
    HAS_JDATETIME = True
except ImportError:
    HAS_JDATETIME = False


def _safe_positive_int(value, default, max_value=None):
    """Convert value to a positive int, falling back to default when invalid."""
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


def calculate_event_dates(event_year, event_month):
    """Calculate start_date and end_date from Persian year and month"""
    if not event_year or not event_month:
        return None, None
    
    try:
        if HAS_JDATETIME:
            # Convert Persian to Gregorian
            # First day of the Persian month
            persian_start = jdatetime.date(event_year, event_month, 1)
            gregorian_start = persian_start.togregorian()
            
            # Last day of the Persian month (approximate - get next month and subtract 1 day)
            if event_month < 12:
                persian_end = jdatetime.date(event_year, event_month + 1, 1) - jdatetime.timedelta(days=1)
            else:
                persian_end = jdatetime.date(event_year + 1, 1, 1) - jdatetime.timedelta(days=1)
            gregorian_end = persian_end.togregorian()
            
            start_date = timezone.make_aware(
                datetime.combine(gregorian_start, datetime.min.time())
            )
            end_date = timezone.make_aware(
                datetime.combine(gregorian_end, datetime.max.time())
            )
            
            return start_date, end_date
        else:
            # Fallback: approximate conversion
            approx_year = event_year + 621
            approx_month = min(event_month, 12)
            
            # Start: first day of month
            start_date = timezone.make_aware(
                datetime(approx_year, approx_month, 1)
            )
            
            # End: last day of month
            if approx_month < 12:
                end_month = approx_month + 1
                end_year = approx_year
            else:
                end_month = 1
                end_year = approx_year + 1
            
            # Get last day of current month
            if end_month == 1:
                last_day = 31
            elif end_month in [4, 6, 9, 11]:
                last_day = 30
            elif end_month == 2:
                last_day = 28
            else:
                last_day = 31
            
            end_date = timezone.make_aware(
                datetime(approx_year, approx_month, last_day, 23, 59, 59)
            )
            
            return start_date, end_date
    except Exception as e:
        # If conversion fails, return None
        return None, None


def _parse_datetime_or_none(value):
    """Parse an ISO datetime string (or datetime object) into an aware datetime."""
    if not value:
        return None

    if isinstance(value, datetime):
        parsed = value
    else:
        parsed = parse_datetime(value)
        if parsed is None:
            raise ValueError(f"فرمت تاریخ/زمان معتبر نیست: {value}")

    if timezone.is_naive(parsed):
        parsed = timezone.make_aware(parsed, timezone.get_current_timezone())

    return parsed


@require_http_methods(["GET"])
def event_list(request):
    """Get list of events.

    If the requester is an authenticated staff user we return the complete list,
    otherwise we limit the output to published items only.
    """
    if request.user.is_authenticated and request.user.is_staff:
        events = Event.objects.all().order_by('-event_year', '-event_month')
    else:
        events = Event.objects.filter(is_published=True).order_by('-event_year', '-event_month')
    
    # Filter by type if provided
    event_type = request.GET.get('type')
    if event_type:
        events = events.filter(event_type=event_type)
    
    # Pagination
    page = _safe_positive_int(request.GET.get('page'), 1)
    per_page = _safe_positive_int(request.GET.get('per_page'), 10, max_value=50)
    paginator = Paginator(events, per_page)
    page_obj = paginator.get_page(page)
    
    events_data = []
    for item in page_obj:
        # Calculate start_date and end_date from event_year and event_month
        start_date, end_date = calculate_event_dates(item.event_year, item.event_month)
        
        # Use the model's property to check if registration is open
        is_registration_open = item.is_registration_open
        
        events_data.append({
            'id': item.id,
            'title': item.title,
            'slug': item.slug,
            'description': item.description[:200] + '...' if len(item.description) > 200 else item.description,
            'event_type': item.get_event_type_display(),
            'event_type_code': item.event_type,
            'image': item.cover_image.url if item.cover_image else (item.image.url if item.image else None),
            'location': item.location,
            'event_month': item.event_month,
            'event_year': item.event_year,
            'start_date': start_date.isoformat() if start_date else None,
            'end_date': end_date.isoformat() if end_date else None,
            'registration_deadline': item.registration_deadline.isoformat() if item.registration_deadline else None,
            'retraining_number': item.retraining_number,
            'max_participants': item.max_participants,
            'price': float(item.price),
            'is_published': item.is_published,
            'is_featured': item.is_featured,
            'is_registration_open': is_registration_open,
            'views': item.views,
            'created_at': item.created_at.isoformat(),
        })
    
    return JsonResponse({
        'success': True,
        'events': events_data,
        'pagination': {
            'page': page_obj.number,
            'pages': paginator.num_pages,
            'total': paginator.count,
            'has_next': page_obj.has_next(),
            'has_prev': page_obj.has_previous(),
        }
    })


@require_http_methods(["GET"])
def event_detail(request, slug):
    """Get single event"""
    event = get_object_or_404(Event, slug=slug, is_published=True)
    event.views += 1
    event.save(update_fields=['views'])
    
    # Check if user is registered
    is_registered = False
    if request.user.is_authenticated:
        is_registered = EventRegistration.objects.filter(event=event, user=request.user).exists()
    
    # Calculate start_date and end_date from event_year and event_month
    start_date, end_date = calculate_event_dates(event.event_year, event.event_month)
    
    # Use the model's property to check if registration is open
    is_registration_open = event.is_registration_open
    
    return JsonResponse({
        'success': True,
        'event': {
            'id': event.id,
            'title': event.title,
            'slug': event.slug,
            'description': event.description,
            'event_type': event.get_event_type_display(),
            'event_type_code': event.event_type,
            'image': event.cover_image.url if event.cover_image else (event.image.url if event.image else None),
            'location': event.location,
            'event_month': event.event_month,
            'event_year': event.event_year,
            'start_date': start_date.isoformat() if start_date else None,
            'end_date': end_date.isoformat() if end_date else None,
            'registration_deadline': event.registration_deadline.isoformat() if event.registration_deadline else None,
            'retraining_number': event.retraining_number,
            'max_participants': event.max_participants,
            'price': float(event.price),
            'is_featured': event.is_featured,
            'is_registration_open': is_registration_open,
            'is_registered': is_registered,
            'views': event.views,
            'created_at': event.created_at.isoformat(),
        }
    })


@csrf_exempt
@login_required
@require_http_methods(["POST"])
def event_register(request, id):
    """Register for an event"""
    try:
        event = get_object_or_404(Event, id=id, is_published=True)
        
        # Check if registration is open
        if not event.is_registration_open:
            return JsonResponse({
                'success': False,
                'errors': 'مهلت ثبت نام به پایان رسیده است'
            }, status=400)
        
        # Check if already registered
        if EventRegistration.objects.filter(event=event, user=request.user).exists():
            return JsonResponse({
                'success': False,
                'errors': 'شما قبلاً در این رویداد ثبت نام کرده‌اید'
            }, status=400)
        
        # Check max participants
        if event.max_participants:
            current_registrations = EventRegistration.objects.filter(event=event).count()
            if current_registrations >= event.max_participants:
                return JsonResponse({
                    'success': False,
                    'errors': 'ظرفیت رویداد تکمیل شده است'
                }, status=400)
        
        # Create registration
        registration = EventRegistration.objects.create(
            event=event,
            user=request.user
        )
        
        return JsonResponse({
            'success': True,
            'message': 'ثبت نام با موفقیت انجام شد',
            'registration': {
                'id': registration.id,
                'event': event.title,
            }
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=400)


@csrf_exempt
@login_required
@user_passes_test(is_staff)
@require_http_methods(["POST"])
def event_create(request):
    """Create new event"""
    try:
        max_participants = request.POST.get('max_participants')
        if max_participants in (None, '', 'null'):
            max_participants = None
        else:
            max_participants = int(max_participants)

        price = request.POST.get('price', 0)
        if price in (None, '', 'null'):
            price = Decimal('0')
        else:
            try:
                price = Decimal(str(price))
            except (InvalidOperation, TypeError, ValueError) as exc:
                raise ValueError(f"فرمت مبلغ معتبر نیست: {price}") from exc
        
        event_month = request.POST.get('event_month')
        if event_month in (None, '', 'null'):
            event_month = None
        else:
            event_month = int(event_month)
        
        event_year = request.POST.get('event_year')
        if event_year in (None, '', 'null'):
            event_year = None
        else:
            event_year = int(event_year)
        
        registration_deadline = None
        if request.POST.get('registration_deadline'):
            from django.utils.dateparse import parse_date
            registration_deadline = parse_date(request.POST.get('registration_deadline'))
        
        event = Event.objects.create(
            title=request.POST.get('title'),
            slug=request.POST.get('slug'),
            description=request.POST.get('description'),
            short_description=request.POST.get('short_description', ''),
            event_type=request.POST.get('event_type', 'other'),
            location=request.POST.get('location'),
            event_month=event_month,
            event_year=event_year,
            registration_deadline=registration_deadline,
            retraining_number=request.POST.get('retraining_number', ''),
            max_participants=max_participants,
            price=price,
            organizer=request.POST.get('organizer', ''),
            target_audience=request.POST.get('target_audience', ''),
            prerequisites=request.POST.get('prerequisites', ''),
            agenda=request.POST.get('agenda', ''),
            speakers=request.POST.get('speakers', ''),
            contact_info=request.POST.get('contact_info', ''),
            is_published=request.POST.get('is_published', 'true').lower() == 'true',
            is_featured=request.POST.get('is_featured', 'false').lower() == 'true',
            created_by=request.user
        )
        
        if 'cover_image' in request.FILES:
            event.cover_image = request.FILES['cover_image']
            event.save()
        
        return JsonResponse({
            'success': True,
            'message': 'رویداد با موفقیت ایجاد شد',
            'event': {
                'id': event.id,
                'title': event.title,
            }
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=400)


@csrf_exempt
@login_required
@user_passes_test(is_staff)
@require_http_methods(["PUT", "POST"])
def event_update(request, id):
    """Update event"""
    try:
        event = get_object_or_404(Event, id=id)
        
        # Handle both JSON and FormData
        if request.content_type and 'application/json' in request.content_type:
            data = json.loads(request.body)
            
            event.title = data.get('title', event.title)
            event.slug = data.get('slug', event.slug)
            event.description = data.get('description', event.description)
            event.event_type = data.get('event_type', event.event_type)
            event.location = data.get('location', event.location)
            event.event_year = data.get('event_year', event.event_year)
            event.event_month = data.get('event_month', event.event_month)
            event.retraining_number = data.get('retraining_number', event.retraining_number)
            event.is_published = data.get('is_published', event.is_published)
            event.is_featured = data.get('is_featured', event.is_featured)
            
            if 'price' in data:
                event.price = Decimal(str(data['price']))
            if 'max_participants' in data:
                event.max_participants = data['max_participants']
        else:
            # FormData
            event.title = request.POST.get('title', event.title)
            event.slug = request.POST.get('slug', event.slug)
            event.description = request.POST.get('description', event.description)
            event.event_type = request.POST.get('event_type', event.event_type)
            event.location = request.POST.get('location', event.location)
            
            if request.POST.get('event_year'):
                event.event_year = int(request.POST.get('event_year'))
            if request.POST.get('event_month'):
                event.event_month = int(request.POST.get('event_month'))
            if request.POST.get('retraining_number'):
                event.retraining_number = request.POST.get('retraining_number')
            
            event.is_published = request.POST.get('is_published', 'true').lower() == 'true'
            event.is_featured = request.POST.get('is_featured', 'false').lower() == 'true'
            
            if 'cover_image' in request.FILES:
                event.cover_image = request.FILES['cover_image']
        
        event.save()
        
        return JsonResponse({
            'success': True,
            'message': 'رویداد با موفقیت بروزرسانی شد',
            'event': {
                'id': event.id,
                'title': event.title,
            }
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=400)


@csrf_exempt
@login_required
@user_passes_test(is_staff)
@require_http_methods(["DELETE"])
def event_delete(request, id):
    """Delete event"""
    try:
        event = get_object_or_404(Event, id=id)
        event.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'رویداد با موفقیت حذف شد'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=400)

