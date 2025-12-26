"""
Views for publications section
"""
import os
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
from pathlib import Path


def get_content_base_path():
    """Get the base path for Content directory"""
    base_dir = Path(settings.BASE_DIR)
    
    possible_paths = [
        base_dir.parent / 'frontend' / 'public' / 'Content',
        base_dir / 'frontend' / 'public' / 'Content',
        base_dir / 'Content',
    ]
    
    for path in possible_paths:
        if path.exists():
            return path
    
    return base_dir / 'Content'


@require_http_methods(["GET"])
def publications_files_view(request):
    """
    List files for publications section based on category
    Categories: newsletters, congress, products, research
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
        
        if category == 'newsletters':
            # Newsletters - PDF files (could be in a specific folder)
            for pdf_file in content_base.rglob('*newsletter*.pdf'):
                if pdf_file.is_file():
                    relative_path = pdf_file.relative_to(content_base)
                    files_data.append({
                        'name': pdf_file.name,
                        'path': str(relative_path).replace('\\', '/'),
                        'type': 'application/pdf',
                        'size': pdf_file.stat().st_size,
                        'url': f'/Content/{str(relative_path).replace(chr(92), "/")}'
                    })
        
        elif category == 'congress':
            # Congress booklets - PDF files with congress/congress in name
            for pdf_file in content_base.rglob('*congress*.pdf'):
                if pdf_file.is_file():
                    relative_path = pdf_file.relative_to(content_base)
                    files_data.append({
                        'name': pdf_file.name,
                        'path': str(relative_path).replace('\\', '/'),
                        'type': 'application/pdf',
                        'size': pdf_file.stat().st_size,
                        'url': f'/Content/{str(relative_path).replace(chr(92), "/")}'
                    })
            # Also check for سمینار
            for pdf_file in content_base.rglob('*سمینار*.pdf'):
                if pdf_file.is_file():
                    relative_path = pdf_file.relative_to(content_base)
                    files_data.append({
                        'name': pdf_file.name,
                        'path': str(relative_path).replace('\\', '/'),
                        'type': 'application/pdf',
                        'size': pdf_file.stat().st_size,
                        'url': f'/Content/{str(relative_path).replace(chr(92), "/")}'
                    })
        
        elif category == 'products':
            # Other products - various files
            for file in content_base.glob('*.pdf'):
                if file.is_file() and 'newsletter' not in file.name.lower() and 'congress' not in file.name.lower() and 'سمینار' not in file.name:
                    relative_path = file.relative_to(content_base)
                    files_data.append({
                        'name': file.name,
                        'path': str(relative_path).replace('\\', '/'),
                        'type': 'application/pdf',
                        'size': file.stat().st_size,
                        'url': f'/Content/{str(relative_path).replace(chr(92), "/")}'
                    })
        
        elif category == 'research':
            # Research - PDF files (could be in a specific folder or have specific naming)
            for pdf_file in content_base.rglob('*.pdf'):
                if pdf_file.is_file():
                    # Filter research-related files
                    name_lower = pdf_file.name.lower()
                    if any(keyword in name_lower for keyword in ['research', 'study', 'مقاله', 'تحقیق']):
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

