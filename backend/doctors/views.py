"""
Views for doctors app - handling file listings for doctors section
"""
import os
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
from pathlib import Path


def get_content_base_path():
    """Get the base path for Content directory"""
    # In Docker/production, Content is in frontend/public/Content
    # In development, it's in frontend/public/Content
    base_dir = Path(settings.BASE_DIR)
    
    # Try different possible locations
    possible_paths = [
        base_dir.parent / 'frontend' / 'public' / 'Content',
        base_dir / 'frontend' / 'public' / 'Content',
        base_dir / 'Content',
    ]
    
    for path in possible_paths:
        if path.exists():
            return path
    
    # Fallback to BASE_DIR/Content
    return base_dir / 'Content'


@require_http_methods(["GET"])
def files_list_view(request):
    """
    List files for doctors section based on category
    Categories: skyroom, video, slides, books, broshour, resources
    """
    try:
        category = request.GET.get('category', '')
        content_base = get_content_base_path()
        
        if not content_base.exists():
            return JsonResponse({
                'success': False,
                'errors': 'پوشه محتوا یافت نشد'
            }, status=404)
        
        files_data = []
        
        if category == 'skyroom':
            # SkyRoom - external links (could be stored in a config or database)
            # For now, return empty or placeholder
            files_data = []
            
        elif category == 'video':
            # Video files - search for video files in Content
            video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm']
            for ext in video_extensions:
                for video_file in content_base.rglob(f'*{ext}'):
                    if video_file.is_file():
                        relative_path = video_file.relative_to(content_base)
                        files_data.append({
                            'name': video_file.name,
                            'path': str(relative_path).replace('\\', '/'),
                            'type': 'video',
                            'size': video_file.stat().st_size,
                            'url': f'/Content/{str(relative_path).replace(chr(92), "/")}'
                        })
        
        elif category == 'slides':
            # Slides - PDF and PPT files
            slide_extensions = ['.pdf', '.ppt', '.pptx']
            for ext in slide_extensions:
                for slide_file in content_base.rglob(f'*{ext}'):
                    if slide_file.is_file():
                        relative_path = slide_file.relative_to(content_base)
                        files_data.append({
                            'name': slide_file.name,
                            'path': str(relative_path).replace('\\', '/'),
                            'type': 'application/pdf' if ext == '.pdf' else 'application/vnd.ms-powerpoint',
                            'size': slide_file.stat().st_size,
                            'url': f'/Content/{str(relative_path).replace(chr(92), "/")}'
                        })
        
        elif category == 'books':
            # Books - read from Content/Books/ with subfolders
            books_dir = content_base / 'Books'
            if books_dir.exists():
                for book_file in books_dir.rglob('*.pdf'):
                    if book_file.is_file():
                        relative_path = book_file.relative_to(content_base)
                        # Get folder structure for organization
                        folder_path = book_file.parent.relative_to(books_dir)
                        files_data.append({
                            'name': book_file.name,
                            'path': str(relative_path).replace('\\', '/'),
                            'folder': str(folder_path).replace('\\', '/') if str(folder_path) != '.' else '',
                            'type': 'application/pdf',
                            'size': book_file.stat().st_size,
                            'url': f'/Content/{str(relative_path).replace(chr(92), "/")}'
                        })
        
        elif category == 'broshour':
            # Broshour - read from Content/Broshour/
            broshour_dir = content_base / 'Broshour'
            if broshour_dir.exists():
                for file in broshour_dir.iterdir():
                    if file.is_file():
                        relative_path = file.relative_to(content_base)
                        file_ext = file.suffix.lower()
                        file_type = 'image/jpeg' if file_ext in ['.jpg', '.jpeg'] else 'image/png' if file_ext == '.png' else 'application/octet-stream'
                        files_data.append({
                            'name': file.name,
                            'path': str(relative_path).replace('\\', '/'),
                            'type': file_type,
                            'size': file.stat().st_size,
                            'url': f'/Content/{str(relative_path).replace(chr(92), "/")}'
                        })
        
        elif category == 'resources':
            # Resources - PDF files in Content root
            for pdf_file in content_base.glob('*.pdf'):
                if pdf_file.is_file():
                    relative_path = pdf_file.relative_to(content_base)
                    files_data.append({
                        'name': pdf_file.name,
                        'path': str(relative_path).replace('\\', '/'),
                        'type': 'application/pdf',
                        'size': pdf_file.stat().st_size,
                        'url': f'/Content/{str(relative_path).replace(chr(92), "/")}'
                    })
        
        else:
            return JsonResponse({
                'success': False,
                'errors': 'دسته‌بندی نامعتبر است'
            }, status=400)
        
        return JsonResponse({
            'success': True,
            'files': files_data,
            'count': len(files_data),
            'category': category
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({
            'success': False,
            'errors': str(e)
        }, status=500)
