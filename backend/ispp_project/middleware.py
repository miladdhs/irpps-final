"""
Custom middleware for handling media file 404 errors and database connection retry
"""
import time
import logging
from django.http import HttpResponse, HttpResponseServerError
from django.utils.deprecation import MiddlewareMixin
from django.db import connection
from django.db.utils import OperationalError, DatabaseError

logger = logging.getLogger(__name__)


class DatabaseRetryMiddleware(MiddlewareMixin):
    """Handle database connection failures with retry logic and exponential backoff"""
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.max_retries = 3
        self.base_delay = 1.0  # Base delay in seconds
        super().__init__(get_response)
    
    def process_request(self, request):
        """Check database connection before processing request"""
        for attempt in range(self.max_retries + 1):
            try:
                # Test database connection
                connection.ensure_connection()
                break
            except (OperationalError, DatabaseError) as e:
                if attempt == self.max_retries:
                    # All retry attempts exhausted
                    logger.error(f"Database connection failed after {self.max_retries} attempts: {str(e)}")
                    return HttpResponseServerError(
                        "Service temporarily unavailable. Please try again later.",
                        content_type="text/plain"
                    )
                
                # Calculate exponential backoff delay
                delay = self.base_delay * (2 ** attempt)
                logger.warning(f"Database connection attempt {attempt + 1} failed, retrying in {delay}s: {str(e)}")
                time.sleep(delay)
        
        return None


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

