from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
import json
from .forms import CustomUserCreationForm

User = get_user_model()


@csrf_exempt
@require_http_methods(["POST"])
def login_view(request):
    """Handle user login"""
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return JsonResponse({
                'success': False,
                'errors': 'نام کاربری و رمز عبور الزامی است'
            }, status=400)
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({
                    'success': True,
                    'message': 'ورود موفقیت‌آمیز بود',
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email,
                        'phone': user.phone,
                    }
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': 'حساب کاربری غیرفعال است'
                }, status=403)
        else:
            return JsonResponse({
                'success': False,
                'errors': 'نام کاربری یا رمز عبور اشتباه است'
            }, status=401)
            
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'errors': 'خطا در پردازش درخواست'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def register_view(request):
    """Handle user registration with approval workflow"""
    try:
        data = json.loads(request.body)
        
        # Check if passwords match
        if data.get('password') != data.get('password_confirm'):
            return JsonResponse({
                'success': False,
                'errors': 'رمزهای عبور مطابقت ندارند'
            }, status=400)
        
        # Create form with data
        form_data = {
            'username': data.get('username'),
            'email': data.get('email', ''),
            'phone': data.get('phone', ''),
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'password1': data.get('password'),
            'password2': data.get('password_confirm'),
        }
        
        form = CustomUserCreationForm(form_data)
        
        if form.is_valid():
            user = form.save(commit=False)
            # Set user as inactive and pending approval
            user.is_active = False
            user.approval_status = 'pending'
            user.save()
            
            # DO NOT login the user automatically
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
                }
            })
        else:
            error_messages = []
            for field, errors in form.errors.items():
                field_label = form.fields.get(field).label if field in form.fields else ''
                for error in errors:
                    if field_label:
                        error_messages.append(f"{field_label}: {error}")
                    else:
                        error_messages.append(str(error))

            return JsonResponse({
                'success': False,
                'errors': ' | '.join(error_messages) if error_messages else 'خطا در ثبت نام'
            }, status=400)
            
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'errors': 'خطا در پردازش درخواست'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=500)


@login_required
@require_http_methods(["GET"])
def profile_view(request):
    """Get user profile"""
    user = request.user
    return JsonResponse({
        'success': True,
        'user': {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
            'date_joined': user.date_joined.isoformat(),
            'is_staff': user.is_staff,
            'profile_image': user.profile_image.url if user.profile_image else '',
            'education': user.education or '',
            'publications': user.publications or '',
            'awards': user.awards or '',
            'certifications': user.certifications or '',
            'research_interests': user.research_interests or '',
            'languages': user.languages or '',
        }
    })


@csrf_exempt
@require_http_methods(["POST"])
def logout_view(request):
    """Handle user logout"""
    logout(request)
    return JsonResponse({
        'success': True,
        'message': 'خروج موفقیت‌آمیز بود'
    })


@login_required
@csrf_exempt
@require_http_methods(["PUT", "PATCH"])
def update_profile_view(request):
    """Update user profile"""
    try:
        user = request.user
        data = json.loads(request.body)
        
        # Update user fields
        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        if 'email' in data:
            user.email = data['email']
        if 'phone' in data:
            user.phone = data['phone']
        
        # Validate and save
        user.full_clean()
        user.save()
        
        return JsonResponse({
            'success': True,
            'message': 'پروفایل با موفقیت به‌روزرسانی شد',
            'user': {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': user.phone,
                'date_joined': user.date_joined.isoformat(),
            }
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'errors': 'خطا در پردازش درخواست'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=500)


@require_http_methods(["GET"])
def members_list_view(request):
    """Get list of all members from database"""
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # Get all users from database (exclude superusers/admin)
        members = User.objects.filter(is_superuser=False).order_by('first_name', 'last_name')
        
        members_data = []
        request_scheme = request.scheme
        request_host = request.get_host()
        for member in members:
            # Get names (first_name = Persian, last_name = English)
            persian_name = member.first_name or ''
            english_name = member.last_name or ''
            
            # Use Persian name as display name, fallback to English
            display_name = persian_name or english_name or member.username
            
            # Get profile image URL from database for this specific user
            profile_image_url = ''
            if member.profile_image:
                try:
                    # Get the URL - Django's .url returns a path starting with /media/
                    profile_image_url = member.profile_image.url
                    # Ensure it's a proper URL path (starts with /media/)
                    if profile_image_url and not profile_image_url.startswith('/'):
                        profile_image_url = f"/{profile_image_url}"
                except Exception as e:
                    # If there's an error getting the URL, use empty string (will use default image)
                    profile_image_url = ''
                    print(f"Error getting profile image for user {member.id}: {e}")
            
            members_data.append({
                'id': member.id,
                'persian_name': persian_name,
                'english_name': english_name,
                'display_name': display_name,
                'email': member.email or '',
                'phone': member.phone or '',
                'city': member.city or '',
                'specialty': member.specialty or '',
                'experience': member.experience or 0,
                'rating': float(member.rating) if member.rating else 0.0,
                'bio': member.bio or '',
                'profile_image': profile_image_url,
                'education': member.education or '',
                'publications': member.publications or '',
                'awards': member.awards or '',
                'certifications': member.certifications or '',
                'research_interests': member.research_interests or '',
                'languages': member.languages or '',
            })
        
        return JsonResponse({
            'success': True,
            'members': members_data,
            'count': len(members_data)
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=500)


@require_http_methods(["GET"])
def board_members_view(request):
    """Get list of board members grouped by period"""
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # Define board member usernames for each period
        board_members_config = {
            '1395': [
                'board_سهیلا_خلیل_زاده',
                'board_قمر_تاج_خانبابائی',
                'board_محمد_رضائی',
                'board_مجید_کیوانفر',
                'board_سید_احمد_طباطبائی',
                'board_محسن_علی_سمیر',
                'board_حسینعلی_غفاری_پور',
                'board_محمد_رضا_مدرسی',
                'board_سید_جواد_سیدی',
                'board_روح_الله_شیرزادی',
                'board_علیرضا_اسدی',
            ],
            '1400': [
                'board_مجید_کیوانفر',
                'board_محمد_رضائی',
                'board_امیر_رضائی',
                'board_علیرضا_عشقی',
                'board_سید_محمد_رضا_میرکریمی',
                'board_بابک_قالیباف',
                'board_سید_حسین_میر_لوحی',
                'board_لعبت_شاهکار',
            ],
            '1403': [
                'board_قمر_تاج_خانبابائی',
                'board_سهیلا_خلیل_زاده',
                'board_محمد_رضائی',
                'board_نازنین_فرحبخش',
                'board_امیر_رضائی',
                'board_ذلفا_مدرسی',
                'board_علیرضا_عشقی',
                'board_معصومه_قاسمپور_علمداری',
            ]
        }
        
        result = {}
        
        for period, usernames in board_members_config.items():
            members = User.objects.filter(username__in=usernames)
            
            members_data = []
            for member in members:
                persian_name = member.first_name or ''
                english_name = member.last_name or ''
                display_name = persian_name or english_name or member.username
                
                profile_image_url = ''
                if member.profile_image:
                    try:
                        profile_image_url = member.profile_image.url
                        if profile_image_url and not profile_image_url.startswith('/'):
                            profile_image_url = f"/{profile_image_url}"
                    except Exception as e:
                        profile_image_url = ''
                
                members_data.append({
                    'id': member.id,
                    'persian_name': persian_name,
                    'english_name': english_name,
                    'display_name': display_name,
                    'specialty': member.specialty or '',
                    'bio': member.bio or '',
                    'profile_image': profile_image_url,
                })
            
            result[period] = members_data
        
        return JsonResponse({
            'success': True,
            'board_members': result
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=500)


@login_required
@csrf_exempt
@require_http_methods(["POST"])
def upload_profile_image_view(request):
    """Upload profile image"""
    try:
        user = request.user
        
        if 'profile_image' not in request.FILES:
            return JsonResponse({
                'success': False,
                'errors': 'فایل عکس ارسال نشده است'
            }, status=400)
        
        image_file = request.FILES['profile_image']
        
        # Validate image file
        if not image_file.content_type.startswith('image/'):
            return JsonResponse({
                'success': False,
                'errors': 'فایل ارسالی باید یک تصویر باشد'
            }, status=400)
        
        # Save image
        user.profile_image = image_file
        user.save()
        
        # Get the URL - Django's .url returns a path starting with /media/
        profile_image_url = user.profile_image.url
        # Ensure it's a proper URL path (starts with /media/)
        if profile_image_url and not profile_image_url.startswith('/'):
            profile_image_url = f"/{profile_image_url}"
        
        return JsonResponse({
            'success': True,
            'message': 'عکس پروفایل با موفقیت به‌روزرسانی شد',
            'profile_image_url': profile_image_url
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=500)


@login_required
@csrf_exempt
@require_http_methods(["DELETE", "POST"])
def delete_profile_image_view(request):
    """Delete profile image"""
    try:
        user = request.user
        
        # Delete the image file if it exists
        if user.profile_image:
            try:
                # Try to delete the file, but don't fail if it doesn't exist
                user.profile_image.delete(save=False)
            except Exception as file_error:
                # Log the error but continue
                print(f"Warning: Could not delete file: {file_error}")
        
        # Clear the profile_image field
        user.profile_image = None
        user.save()
        
        return JsonResponse({
            'success': True,
            'message': 'عکس پروفایل با موفقیت حذف شد'
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=500)


@login_required
@csrf_exempt
@require_http_methods(["PUT", "PATCH", "POST"])
def update_resume_view(request):
    """Update user resume information"""
    try:
        user = request.user
        
        # Handle both JSON and form data
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST
        
        # Update resume fields
        if 'education' in data:
            user.education = data['education']
        if 'publications' in data:
            user.publications = data['publications']
        if 'awards' in data:
            user.awards = data['awards']
        if 'certifications' in data:
            user.certifications = data['certifications']
        if 'research_interests' in data:
            user.research_interests = data['research_interests']
        if 'languages' in data:
            user.languages = data['languages']
        if 'bio' in data:
            user.bio = data['bio']
        
        # Validate and save
        user.full_clean()
        user.save()
        
        return JsonResponse({
            'success': True,
            'message': 'رزومه با موفقیت به‌روزرسانی شد',
            'resume': {
                'education': user.education or '',
                'publications': user.publications or '',
                'awards': user.awards or '',
                'certifications': user.certifications or '',
                'research_interests': user.research_interests or '',
                'languages': user.languages or '',
                'bio': user.bio or '',
            }
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'errors': 'خطا در پردازش درخواست'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=500)


# Membership Management API Endpoints

@staff_member_required
@require_http_methods(["GET"])
def pending_members_view(request):
    """Get list of pending membership requests (admin only)"""
    try:
        pending_users = User.objects.filter(
            approval_status='pending',
            is_superuser=False
        ).order_by('-requested_at')
        
        members_data = []
        for user in pending_users:
            members_data.append({
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
            })
        
        return JsonResponse({
            'success': True,
            'pending_members': members_data,
            'count': len(members_data)
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=500)


@staff_member_required
@csrf_exempt
@require_http_methods(["POST"])
def approve_member_view(request, user_id):
    """Approve a pending member (admin only)"""
    try:
        user = User.objects.get(id=user_id, approval_status='pending')
        admin_user = request.user
        
        # Approve the user
        user.approve_membership(admin_user)
        
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
            }
        })
        
    except User.DoesNotExist:
        return JsonResponse({
            'success': False,
            'errors': 'کاربر یافت نشد یا قبلاً پردازش شده است'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=500)


@staff_member_required
@csrf_exempt
@require_http_methods(["POST"])
def reject_member_view(request, user_id):
    """Reject a pending member (admin only)"""
    try:
        data = json.loads(request.body) if request.body else {}
        reason = data.get('reason', '')
        
        user = User.objects.get(id=user_id, approval_status='pending')
        admin_user = request.user
        
        # Reject the user
        user.reject_membership(reason, admin_user)
        
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
            }
        })
        
    except User.DoesNotExist:
        return JsonResponse({
            'success': False,
            'errors': 'کاربر یافت نشد یا قبلاً پردازش شده است'
        }, status=404)
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'errors': 'خطا در پردازش درخواست'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=500)