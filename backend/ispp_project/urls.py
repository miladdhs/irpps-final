"""
URL configuration for ISPP project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

spa_view = TemplateView.as_view(template_name='index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/news/', include('news.urls')),
    path('api/events/', include('events.urls')),
    path('api/dashboard/', include('dashboard.urls')),
]

# Serve static and media files in development
# In production (Docker), Nginx handles static files, but we still need to serve media
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # In production, still serve media files (Nginx proxies to this)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# SPA catch-all route (must be last)
# Exclude API, admin, media, static, and assets paths from SPA routing
urlpatterns += [
    path('', spa_view, name='spa'),
    re_path(r'^(?!api/|admin/|media/|static/|assets/).*$', spa_view),
]

