"""
URL configuration for ISPP project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache
import os

spa_view = TemplateView.as_view(template_name='index.html')


@never_cache
@require_http_methods(["GET"])
def serve_media_with_fallback(request, path):
    """Serve media files with fallback to placeholder if file doesn't exist"""
    from django.conf import settings
    import os
    
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    
    # Check if file exists
    if os.path.exists(file_path) and os.path.isfile(file_path):
        # File exists, serve it normally
        from django.views.static import serve
        return serve(request, path, document_root=settings.MEDIA_ROOT)
    else:
        # File doesn't exist, return SVG placeholder
        svg_placeholder = '''<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#f8f9fa"/>
  <circle cx="100" cy="80" r="30" fill="#dee2e6"/>
  <path d="M 50 150 Q 100 130 150 150" stroke="#dee2e6" stroke-width="3" fill="none"/>
</svg>'''
        response = HttpResponse(svg_placeholder, content_type='image/svg+xml')
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        return response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/news/', include('news.urls')),
    path('api/events/', include('events.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    # Custom media serving with fallback
    re_path(r'^media/(?P<path>.*)$', serve_media_with_fallback, name='media_with_fallback'),
]

# Serve static and media files in development
# In production (Docker), Nginx handles static files, but we still need to serve media
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    # Don't add default media serving since we have custom handler above
else:
    # In production, custom handler above will serve media files (Nginx proxies to this)
    pass

# SPA catch-all route (must be last)
# Exclude API, admin, media, static, and assets paths from SPA routing
urlpatterns += [
    path('', spa_view, name='spa'),
    re_path(r'^(?!api/|admin/|media/|static/|assets/).*$', spa_view),
]

