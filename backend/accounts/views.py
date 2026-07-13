import json

from add_board_members import BOARD_MEMBERS_DATA, create_username
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .forms import CustomUserCreationForm
from .member_directory import preferred_persian_name, should_hide_from_public_members

User = get_user_model()

RESUME_FIELD_NAMES = (
    'city',
    'specialty',
    'experience',
    'bio',
    'workplace',
    'current_position',
    'expertise_areas',
    'work_experience',
    'education',
    'publications',
    'awards',
    'certifications',
    'research_interests',
    'languages',
)


def _text(value):
    return value or ''


def _profile_image_url(user):
    if not user.profile_image:
        return ''

    try:
        profile_image_url = user.profile_image.url
        return profile_image_url if profile_image_url.startswith('/') else f'/{profile_image_url}'
    except Exception:
        return ''


def _resume_payload(user):
    payload = {
        'city': _text(user.city),
        'specialty': _text(user.specialty),
        'experience': user.experience or 0,
        'bio': _text(user.bio),
        'workplace': _text(getattr(user, 'workplace', '')),
        'current_position': _text(getattr(user, 'current_position', '')),
        'expertise_areas': _text(getattr(user, 'expertise_areas', '')),
        'work_experience': _text(getattr(user, 'work_experience', '')),
        'education': _text(user.education),
        'publications': _text(user.publications),
        'awards': _text(user.awards),
        'certifications': _text(user.certifications),
        'research_interests': _text(user.research_interests),
        'languages': _text(user.languages),
    }
    payload['filled_sections'] = [
        key for key, value in payload.items()
        if key != 'experience' and isinstance(value, str) and value.strip()
    ]
    if payload['experience']:
        payload['filled_sections'].insert(0, 'experience')
    return payload


def serialize_user_payload(user):
    return {
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'phone': _text(user.phone),
        'date_joined': user.date_joined.isoformat() if user.date_joined else None,
        'is_staff': user.is_staff,
        'is_superuser': user.is_superuser,
        'approval_status': getattr(user, 'approval_status', None),
        'profile_image': _profile_image_url(user),
        **_resume_payload(user),
    }


@csrf_exempt
@require_http_methods(["POST"])
def login_view(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({'success': False, 'errors': 'نام کاربری و رمز عبور الزامی است'}, status=400)

        user = authenticate(request, username=username, password=password)
        if user is None:
            return JsonResponse({'success': False, 'errors': 'نام کاربری یا رمز عبور اشتباه است'}, status=401)

        if not user.is_active:
            return JsonResponse({'success': False, 'errors': 'حساب کاربری غیرفعال است'}, status=403)

        login(request, user)
        return JsonResponse({'success': True, 'message': 'ورود موفقیت‌آمیز بود', 'user': serialize_user_payload(user)})
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': 'خطا در پردازش درخواست'}, status=400)
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def register_view(request):
    try:
        data = json.loads(request.body)
        if data.get('password') != data.get('password_confirm'):
            return JsonResponse({'success': False, 'errors': 'رمزهای عبور مطابقت ندارند'}, status=400)

        form = CustomUserCreationForm({
            'username': data.get('username'),
            'email': data.get('email', ''),
            'phone': data.get('phone', ''),
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'password1': data.get('password'),
            'password2': data.get('password_confirm'),
        })

        if not form.is_valid():
            error_messages = []
            for field, errors in form.errors.items():
                field_label = form.fields.get(field).label if field in form.fields else ''
                for error in errors:
                    error_messages.append(f'{field_label}: {error}' if field_label else str(error))
            return JsonResponse({'success': False, 'errors': ' | '.join(error_messages) or 'خطا در ثبت نام'}, status=400)

        user = form.save(commit=False)
        user.is_active = False
        user.approval_status = 'pending'
        user.save()

        return JsonResponse({
            'success': True,
            'message': 'درخواست عضویت شما ثبت شد. لطفاً منتظر تایید مدیریت باشید.',
            'user': {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': user.phone,
                'approval_status': user.approval_status,
            },
        })
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': 'خطا در پردازش درخواست'}, status=400)
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=500)


@login_required
@require_http_methods(["GET"])
def profile_view(request):
    return JsonResponse({'success': True, 'user': serialize_user_payload(request.user)})


@csrf_exempt
@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return JsonResponse({'success': True, 'message': 'خروج موفقیت‌آمیز بود'})


@login_required
@csrf_exempt
@require_http_methods(["PUT", "PATCH"])
def update_profile_view(request):
    try:
        user = request.user
        data = json.loads(request.body)

        for field in ('first_name', 'last_name', 'email', 'phone', 'city', 'specialty', 'workplace', 'current_position'):
            if field in data:
                setattr(user, field, data[field])

        if 'experience' in data:
            user.experience = int(data['experience'] or 0)

        user.full_clean()
        user.save()
        return JsonResponse({'success': True, 'message': 'پروفایل با موفقیت به‌روزرسانی شد', 'user': serialize_user_payload(user)})
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': 'خطا در پردازش درخواست'}, status=400)
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=500)


@require_http_methods(["GET"])
def members_list_view(request):
    try:
        members = User.objects.filter(is_active=True).order_by('first_name', 'last_name')
        members_data = []

        for member in members:
            if should_hide_from_public_members(member):
                continue

            persian_name = preferred_persian_name(member)
            english_name = member.last_name or ''
            display_name = persian_name or english_name or member.username
            members_data.append({
                'id': member.id,
                'persian_name': persian_name,
                'english_name': english_name,
                'display_name': display_name,
                'email': _text(member.email),
                'phone': _text(member.phone),
                'profile_image': _profile_image_url(member),
                **_resume_payload(member),
            })

        return JsonResponse({'success': True, 'members': members_data, 'count': len(members_data)})
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=500)


@require_http_methods(["GET"])
def board_members_view(request):
    try:
        board_members_config = {
            '1395': [
                'board_Ø³Ù‡ÛŒÙ„Ø§_Ø®Ù„ÛŒÙ„_Ø²Ø§Ø¯Ù‡',
                'board_Ù‚Ù…Ø±_ØªØ§Ø¬_Ø®Ø§Ù†Ø¨Ø§Ø¨Ø§Ø¦ÛŒ',
                'board_Ù…Ø­Ù…Ø¯_Ø±Ø¶Ø§Ø¦ÛŒ',
                'board_Ù…Ø¬ÛŒØ¯_Ú©ÛŒÙˆØ§Ù†ÙØ±',
                'board_Ø³ÛŒØ¯_Ø§Ø­Ù…Ø¯_Ø·Ø¨Ø§Ø·Ø¨Ø§Ø¦ÛŒ',
                'board_Ù…Ø­Ø³Ù†_Ø¹Ù„ÛŒ_Ø³Ù…ÛŒØ±',
                'board_Ø­Ø³ÛŒÙ†Ø¹Ù„ÛŒ_ØºÙØ§Ø±ÛŒ_Ù¾ÙˆØ±',
                'board_Ù…Ø­Ù…Ø¯_Ø±Ø¶Ø§_Ù…Ø¯Ø±Ø³ÛŒ',
                'board_Ø³ÛŒØ¯_Ø¬ÙˆØ§Ø¯_Ø³ÛŒØ¯ÛŒ',
                'board_Ø±ÙˆØ­_Ø§Ù„Ù„Ù‡_Ø´ÛŒØ±Ø²Ø§Ø¯ÛŒ',
                'board_Ø¹Ù„ÛŒØ±Ø¶Ø§_Ø§Ø³Ø¯ÛŒ',
            ],
            '1400': [
                'board_Ù…Ø¬ÛŒØ¯_Ú©ÛŒÙˆØ§Ù†ÙØ±',
                'board_Ù…Ø­Ù…Ø¯_Ø±Ø¶Ø§Ø¦ÛŒ',
                'board_Ø§Ù…ÛŒØ±_Ø±Ø¶Ø§Ø¦ÛŒ',
                'board_Ø¹Ù„ÛŒØ±Ø¶Ø§_Ø¹Ø´Ù‚ÛŒ',
                'board_Ø³ÛŒØ¯_Ù…Ø­Ù…Ø¯_Ø±Ø¶Ø§_Ù…ÛŒØ±Ú©Ø±ÛŒÙ…ÛŒ',
                'board_Ø¨Ø§Ø¨Ú©_Ù‚Ø§Ù„ÛŒØ¨Ø§Ù',
                'board_Ø³ÛŒØ¯_Ø­Ø³ÛŒÙ†_Ù…ÛŒØ±_Ù„ÙˆØ­ÛŒ',
                'board_Ù„Ø¹Ø¨Øª_Ø´Ø§Ù‡Ú©Ø§Ø±',
            ],
            '1403': [
                'board_Ù‚Ù…Ø±_ØªØ§Ø¬_Ø®Ø§Ù†Ø¨Ø§Ø¨Ø§Ø¦ÛŒ',
                'board_Ø³Ù‡ÛŒÙ„Ø§_Ø®Ù„ÛŒÙ„_Ø²Ø§Ø¯Ù‡',
                'board_Ù…Ø­Ù…Ø¯_Ø±Ø¶Ø§Ø¦ÛŒ',
                'board_Ù†Ø§Ø²Ù†ÛŒÙ†_ÙØ±Ø­Ø¨Ø®Ø´',
                'board_Ø§Ù…ÛŒØ±_Ø±Ø¶Ø§Ø¦ÛŒ',
                'board_Ø°Ù„ÙØ§_Ù…Ø¯Ø±Ø³ÛŒ',
                'board_Ø¹Ù„ÛŒØ±Ø¶Ø§_Ø¹Ø´Ù‚ÛŒ',
                'board_Ù…Ø¹ØµÙˆÙ…Ù‡_Ù‚Ø§Ø³Ù…Ù¾ÙˆØ±_Ø¹Ù„Ù…Ø¯Ø§Ø±ÛŒ',
            ],
        }

        result = {}
        for period, usernames in board_members_config.items():
            members = User.objects.filter(username__in=usernames)
            result[period] = [{
                'id': member.id,
                'persian_name': member.first_name or '',
                'english_name': member.last_name or '',
                'display_name': member.first_name or member.last_name or member.username,
                'specialty': member.specialty or '',
                'bio': member.bio or '',
                'profile_image': _profile_image_url(member),
            } for member in members]

        return JsonResponse({'success': True, 'board_members': result})
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=500)


@login_required
@csrf_exempt
@require_http_methods(["POST"])
def upload_profile_image_view(request):
    try:
        user = request.user
        if 'profile_image' not in request.FILES:
            return JsonResponse({'success': False, 'errors': 'فایل عکس ارسال نشده است'}, status=400)

        image_file = request.FILES['profile_image']
        if not image_file.content_type.startswith('image/'):
            return JsonResponse({'success': False, 'errors': 'فایل ارسالی باید یک تصویر باشد'}, status=400)

        user.profile_image = image_file
        user.save()
        return JsonResponse({
            'success': True,
            'message': 'عکس پروفایل با موفقیت به‌روزرسانی شد',
            'profile_image_url': _profile_image_url(user),
            'user': serialize_user_payload(user),
        })
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=500)


@login_required
@csrf_exempt
@require_http_methods(["DELETE", "POST"])
def delete_profile_image_view(request):
    try:
        user = request.user
        if user.profile_image:
            try:
                user.profile_image.delete(save=False)
            except Exception:
                pass
        user.profile_image = None
        user.save()
        return JsonResponse({
            'success': True,
            'message': 'عکس پروفایل با موفقیت حذف شد',
            'profile_image_url': '',
            'user': serialize_user_payload(user),
        })
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=500)


@login_required
@csrf_exempt
@require_http_methods(["PUT", "PATCH", "POST"])
def update_resume_view(request):
    try:
        user = request.user
        data = json.loads(request.body) if request.content_type == 'application/json' else request.POST

        for field in RESUME_FIELD_NAMES:
            if field in data:
                value = data[field]
                if field == 'experience':
                    setattr(user, field, int(value or 0))
                else:
                    setattr(user, field, value)

        user.full_clean()
        user.save()
        return JsonResponse({
            'success': True,
            'message': 'رزومه با موفقیت به‌روزرسانی شد',
            'resume': _resume_payload(user),
            'user': serialize_user_payload(user),
        })
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': 'خطا در پردازش درخواست'}, status=400)
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=500)


@staff_member_required
@require_http_methods(["GET"])
def pending_members_view(request):
    try:
        pending_users = User.objects.filter(approval_status='pending', is_superuser=False).order_by('-requested_at')
        members_data = [{
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
            'city': user.city,
            'specialty': user.specialty,
            'experience': user.experience,
            'bio': user.bio,
            'requested_at': user.requested_at.isoformat(),
            'approval_status': user.approval_status,
        } for user in pending_users]
        return JsonResponse({'success': True, 'pending_members': members_data, 'count': len(members_data)})
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=500)


@staff_member_required
@csrf_exempt
@require_http_methods(["POST"])
def approve_member_view(request, user_id):
    try:
        user = User.objects.get(id=user_id, approval_status='pending')
        user.approve_membership(request.user)
        return JsonResponse({
            'success': True,
            'message': f'عضویت {user.first_name} {user.last_name} تایید شد',
            'user': {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'approval_status': user.approval_status,
                'is_active': user.is_active,
                'approved_at': user.approved_at.isoformat() if user.approved_at else None,
            },
        })
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'errors': 'کاربر یافت نشد یا قبلاً پردازش شده است'}, status=404)
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=500)


@staff_member_required
@csrf_exempt
@require_http_methods(["POST"])
def reject_member_view(request, user_id):
    try:
        data = json.loads(request.body) if request.body else {}
        user = User.objects.get(id=user_id, approval_status='pending')
        user.reject_membership(data.get('reason', ''), request.user)
        return JsonResponse({
            'success': True,
            'message': f'عضویت {user.first_name} {user.last_name} رد شد',
            'user': {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'approval_status': user.approval_status,
                'is_active': user.is_active,
                'rejection_reason': user.rejection_reason,
            },
        })
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'errors': 'کاربر یافت نشد یا قبلاً پردازش شده است'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': 'خطا در پردازش درخواست'}, status=400)
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=500)


@require_http_methods(["GET"])
def board_members_view_v2(request):
    try:
        result = {}
        for period_key, configured_members in BOARD_MEMBERS_DATA.items():
            period = configured_members[0]['period'] if configured_members else period_key
            members_data = []

            for configured_member in configured_members:
                username = create_username(configured_member['persian_name'])
                member = User.objects.filter(username=username).first()
                members_data.append({
                    'id': member.id if member else None,
                    'username': username,
                    'persian_name': configured_member['persian_name'],
                    'english_name': configured_member['english_name'],
                    'display_name': configured_member['persian_name'],
                    'position': configured_member['position'],
                    'role': configured_member['role'],
                    'specialty': (member.specialty if member else None) or configured_member['specialty'] or '',
                    'bio': (member.bio if member else None) or f"{configured_member['position']} - دوره {configured_member['period']}",
                    'profile_image': _profile_image_url(member) if member else '',
                })

            result[period] = members_data

        return JsonResponse({'success': True, 'board_members': result})
    except Exception as exc:
        return JsonResponse({'success': False, 'errors': str(exc)}, status=500)
