from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
import json
from .models import News, Announcement


DEFAULT_NEWS_IMAGE = '/img/news.png'


def _image_url(image_field, default_url=DEFAULT_NEWS_IMAGE):
    if not image_field:
        return default_url

    try:
        if not image_field.storage.exists(image_field.name):
            return default_url
        return image_field.url
    except Exception:
        return default_url


def _serialize_news(item, include_content=True):
    payload = {
        'id': item.id,
        'title': item.title,
        'slug': item.slug,
        'short_content': item.short_content or '',
        'category': item.category or '',
        'tags': item.tags or '',
        'source': item.source or '',
        'image': _image_url(item.image),
        'author': item.author.get_full_name() or item.author.username,
        'is_published': item.is_published,
        'views': item.views,
        'created_at': item.created_at.isoformat(),
        'updated_at': item.updated_at.isoformat(),
    }
    if include_content:
        payload['content'] = item.content
    return payload


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
    
    news_data = [_serialize_news(item) for item in page_obj]
    
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
    queryset = News.objects.all() if request.user.is_authenticated and request.user.is_staff else News.objects.filter(is_published=True)
    news = get_object_or_404(queryset, slug=slug)
    news.views += 1
    news.save(update_fields=['views'])
    
    return JsonResponse({
        'success': True,
        'news': _serialize_news(news)
    })


@require_http_methods(["GET"])
def news_detail_by_id(request, id):
    """Get single news item by numeric id for legacy links."""
    queryset = News.objects.all() if request.user.is_authenticated and request.user.is_staff else News.objects.filter(is_published=True)
    news = get_object_or_404(queryset, id=id)
    news.views += 1
    news.save(update_fields=['views'])

    return JsonResponse({
        'success': True,
        'news': _serialize_news(news)
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
@require_http_methods(["PUT", "POST"])
def news_update(request, id):
    """Update news"""
    try:
        news = get_object_or_404(News, id=id)

        if request.content_type and 'application/json' in request.content_type:
            data = json.loads(request.body)

            news.title = data.get('title', news.title)
            news.slug = data.get('slug', news.slug)
            news.content = data.get('content', news.content)
            news.short_content = data.get('short_content', news.short_content)
            news.category = data.get('category', news.category)
            news.tags = data.get('tags', news.tags)
            news.source = data.get('source', news.source)
            news.is_published = data.get('is_published', news.is_published)
        else:
            news.title = request.POST.get('title', news.title)
            news.slug = request.POST.get('slug', news.slug)
            news.content = request.POST.get('content', news.content)
            news.short_content = request.POST.get('short_content', news.short_content)
            news.category = request.POST.get('category', news.category)
            news.tags = request.POST.get('tags', news.tags)
            news.source = request.POST.get('source', news.source)
            news.is_published = request.POST.get('is_published', 'true').lower() == 'true'

            if 'image' in request.FILES:
                news.image = request.FILES['image']

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
        'image': _image_url(item.image),
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


@csrf_exempt
@login_required
@user_passes_test(is_staff)
@require_http_methods(["PUT"])
def announcement_update(request, id):
    """Update announcement"""
    try:
        announcement = get_object_or_404(Announcement, id=id)
        data = json.loads(request.body)
        
        announcement.title = data.get('title', announcement.title)
        announcement.slug = data.get('slug', announcement.slug)
        announcement.content = data.get('content', announcement.content)
        announcement.is_published = data.get('is_published', announcement.is_published)
        announcement.is_important = data.get('is_important', announcement.is_important)
        announcement.save()
        
        return JsonResponse({
            'success': True,
            'message': 'اطلاعیه با موفقیت بروزرسانی شد',
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


@csrf_exempt
@login_required
@user_passes_test(is_staff)
@require_http_methods(["DELETE"])
def announcement_delete(request, id):
    """Delete announcement"""
    try:
        announcement = get_object_or_404(Announcement, id=id)
        announcement.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'اطلاعیه با موفقیت حذف شد'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=400)

