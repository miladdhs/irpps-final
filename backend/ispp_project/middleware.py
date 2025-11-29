"""
Custom middleware for handling media file 404 errors
"""
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class Media404HandlerMiddleware(MiddlewareMixin):
    """Handle 404 errors for media files and return placeholder"""
    
    def process_response(self, request, response):
        # Only handle 404 errors for media files
        if response.status_code == 404 and request.path.startswith('/media/'):
            # Get the path without query string for checking extension
            path_without_query = request.path.split('?')[0]
            
            # Check if it's an image request (handle query strings in path)
            image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.avif', '.apng']
            if any(path_without_query.lower().endswith(ext) for ext in image_extensions):
                # Return SVG placeholder instead of 404
                svg_placeholder = '''<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#f8f9fa"/>
  <circle cx="100" cy="80" r="30" fill="#dee2e6"/>
  <path d="M 50 150 Q 100 130 150 150" stroke="#dee2e6" stroke-width="3" fill="none"/>
</svg>'''
                placeholder_response = HttpResponse(svg_placeholder, content_type='image/svg+xml')
                placeholder_response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
                placeholder_response.status_code = 200
                return placeholder_response
        
        return response

