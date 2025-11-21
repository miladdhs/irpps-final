from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from news.models import News, Announcement
from events.models import Event, EventRegistration

User = get_user_model()


def is_staff(user):
    return user.is_staff


@login_required
@user_passes_test(is_staff)
def admin_dashboard(request):
    """Admin dashboard with statistics"""
    stats = {
        'total_users': User.objects.count(),
        'total_news': News.objects.count(),
        'published_news': News.objects.filter(is_published=True).count(),
        'total_announcements': Announcement.objects.count(),
        'published_announcements': Announcement.objects.filter(is_published=True).count(),
        'total_events': Event.objects.count(),
        'published_events': Event.objects.filter(is_published=True).count(),
        'total_registrations': EventRegistration.objects.count(),
    }
    
    return JsonResponse({
        'success': True,
        'stats': stats
    })

