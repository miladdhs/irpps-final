from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
import json
from .models import News, Announcement


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


@require_http_methods(["GET"])
def news_list(request):
    """Get list of news.

    If the requester is an authenticated staff user we return the complete list,
    otherwise we limit the output to published items only.
    """
    if request.user.is_authenticated and request.user.is_staff:
        news = News.objects.all().order_by('-created_at')
    else:
        news = News.objects.filter(is_published=True).order_by('-created_at')
    
    # Pagination
    page = _safe_positive_int(request.GET.get('page'), 1)
    per_page = _safe_positive_int(request.GET.get('per_page'), 10, max_value=50)
    paginator = Paginator(news, per_page)
    page_obj = paginator.get_page(page)
    
    news_data = [{
        'id': item.id,
        'title': item.title,
        'slug': item.slug,
        'content': item.content[:200] + '...' if len(item.content) > 200 else item.content,
        'image': item.image.url if item.image else None,
        'author': item.author.get_full_name() or item.author.username,
        'is_published': item.is_published,
        'views': item.views,
        'created_at': item.created_at.isoformat(),
    } for item in page_obj]
    
    return JsonResponse({
        'success': True,
        'news': news_data,
        'pagination': {
            'page': page_obj.number,
            'pages': paginator.num_pages,
            'total': paginator.count,
            'has_next': page_obj.has_next(),
            'has_prev': page_obj.has_previous(),
        }
    })


@require_http_methods(["GET"])
def news_detail(request, slug):
    """Get single news item"""
    news = get_object_or_404(News, slug=slug, is_published=True)
    news.views += 1
    news.save(update_fields=['views'])
    
    return JsonResponse({
        'success': True,
        'news': {
            'id': news.id,
            'title': news.title,
            'slug': news.slug,
            'content': news.content,
            'image': news.image.url if news.image else None,
            'author': news.author.get_full_name() or news.author.username,
            'views': news.views,
            'created_at': news.created_at.isoformat(),
            'updated_at': news.updated_at.isoformat(),
        }
    })


@csrf_exempt
@login_required
@user_passes_test(is_staff)
@require_http_methods(["POST"])
def news_create(request):
    """Create new news"""
    try:
        news = News.objects.create(
            title=request.POST.get('title'),
            slug=request.POST.get('slug'),
            content=request.POST.get('content'),
            short_content=request.POST.get('short_content', ''),
            category=request.POST.get('category', ''),
            tags=request.POST.get('tags', ''),
            source=request.POST.get('source', ''),
            author=request.user,
            is_published=request.POST.get('is_published', 'true').lower() == 'true'
        )
        
        if 'image' in request.FILES:
            news.image = request.FILES['image']
            news.save()
        
        return JsonResponse({
            'success': True,
            'message': 'خبر با موفقیت ایجاد شد',
            'news': {
                'id': news.id,
                'title': news.title,
                'slug': news.slug,
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
@require_http_methods(["PUT"])
def news_update(request, id):
    """Update news"""
    try:
        news = get_object_or_404(News, id=id)
        data = json.loads(request.body)
        
        news.title = data.get('title', news.title)
        news.slug = data.get('slug', news.slug)
        news.content = data.get('content', news.content)
        news.is_published = data.get('is_published', news.is_published)
        news.save()
        
        return JsonResponse({
            'success': True,
            'message': 'خبر با موفقیت بروزرسانی شد',
            'news': {
                'id': news.id,
                'title': news.title,
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
def news_delete(request, id):
    """Delete news"""
    try:
        news = get_object_or_404(News, id=id)
        news.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'خبر با موفقیت حذف شد'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=400)


# Announcement views (similar to news)
@require_http_methods(["GET"])
def announcement_list(request):
    """Get list of announcements.

    If the requester is an authenticated staff user we return the complete list,
    otherwise we limit the output to published items only.
    """
    if request.user.is_authenticated and request.user.is_staff:
        announcements = Announcement.objects.all().order_by('-created_at')
    else:
        announcements = Announcement.objects.filter(is_published=True).order_by('-created_at')
    
    page = _safe_positive_int(request.GET.get('page'), 1)
    per_page = _safe_positive_int(request.GET.get('per_page'), 10, max_value=50)
    paginator = Paginator(announcements, per_page)
    page_obj = paginator.get_page(page)
    
    announcements_data = [{
        'id': item.id,
        'title': item.title,
        'slug': item.slug,
        'content': item.content[:200] + '...' if len(item.content) > 200 else item.content,
        'image': item.image.url if item.image else None,
        'author': item.author.get_full_name() or item.author.username,
        'is_important': item.is_important,
        'is_published': item.is_published,
        'views': item.views,
        'created_at': item.created_at.isoformat(),
    } for item in page_obj]
    
    return JsonResponse({
        'success': True,
        'announcements': announcements_data,
        'pagination': {
            'page': page_obj.number,
            'pages': paginator.num_pages,
            'total': paginator.count,
            'has_next': page_obj.has_next(),
            'has_prev': page_obj.has_previous(),
        }
    })


@csrf_exempt
@login_required
@user_passes_test(is_staff)
@require_http_methods(["POST"])
def announcement_create(request):
    """Create new announcement"""
    try:
        data = json.loads(request.body)
        
        announcement = Announcement.objects.create(
            title=data.get('title'),
            slug=data.get('slug'),
            content=data.get('content'),
            author=request.user,
            is_published=data.get('is_published', True),
            is_important=data.get('is_important', False)
        )
        
        return JsonResponse({
            'success': True,
            'message': 'اطلاعیه با موفقیت ایجاد شد',
            'announcement': {
                'id': announcement.id,
                'title': announcement.title,
            }
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=400)

