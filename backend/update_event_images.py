#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
اسکریپت به‌روزرسانی تصاویر رویدادهای موجود
"""
import os
import sys
import django
from pathlib import Path
import shutil

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ispp_project.settings')
django.setup()

from events.models import Event


def update_event_images():
    """به‌روزرسانی تصاویر رویدادها"""
    print("=" * 80)
    print("شروع به‌روزرسانی تصاویر رویدادها...")
    print("=" * 80)
    
    # Base paths
    base_dir = Path(__file__).parent.parent
    frontend_content = base_dir / 'frontend' / 'public' / 'Content'
    media_dir = Path(__file__).parent / 'media' / 'events' / 'covers'
    media_dir.mkdir(parents=True, exist_ok=True)
    
    # نقشه دقیق عنوان رویدادها به تصاویر
    event_image_mapping = {
        'وبینار روز جهانی آسم ۲۰۲۵': 'asthma.jpg',
        'وبینار روز جهانی پنومونی': 'penomoni.jpg',
        'اولین کنگره سراسری بیماری‌های تنفسی کودکان': 'avalin kongere.jpg',
        'چهارمین همایش سالیانه انجمن علمی ریه کودکان ایران (وبینار چهار روزه)': 'chaharomin hamayesh.jpg',
        'ششمین سمینار سالانه بیماری‌های تنفسی کودکان': 'seshomin seminar.jpg',
        'سومین کنگره سراسری بیماری‌های تنفسی کودکان': 'sevomin kongere.jpg',
    }
    
    updated_count = 0
    not_found_count = 0
    skipped_count = 0
    
    # دریافت تمام رویدادها
    events = Event.objects.all()
    
    print(f"\nتعداد کل رویدادها: {events.count()}\n")
    
    for event in events:
        print(f"بررسی رویداد: {event.title}")
        
        # پیدا کردن تصویر مناسب بر اساس عنوان دقیق
        image_file = None
        for event_title, filename in event_image_mapping.items():
            if event_title in event.title or event.title in event_title:
                image_file = filename
                break
        
        if image_file:
            source_image = frontend_content / image_file
            
            if source_image.exists():
                # حذف تصویر قبلی اگر وجود دارد
                if event.cover_image:
                    old_image_path = Path(__file__).parent / 'media' / str(event.cover_image)
                    if old_image_path.exists() and old_image_path.name != image_file:
                        try:
                            old_image_path.unlink()
                            print(f"  🗑 تصویر قبلی حذف شد: {old_image_path.name}")
                        except Exception as e:
                            print(f"  ⚠ خطا در حذف تصویر قبلی: {e}")
                
                # کپی تصویر جدید
                dest_image = media_dir / image_file
                shutil.copy2(source_image, dest_image)
                
                # به‌روزرسانی رویداد
                event.cover_image = f'events/covers/{image_file}'
                event.save()
                
                updated_count += 1
                print(f"  ✓ تصویر به‌روزرسانی شد: {image_file}")
            else:
                print(f"  ⚠ تصویر یافت نشد: {source_image}")
                not_found_count += 1
        else:
            # رویدادهایی که در لیست نیستند را نگه می‌داریم
            skipped_count += 1
            print(f"  ⊗ این رویداد در لیست به‌روزرسانی نیست (نگه داشته می‌شود)")
    
    print(f"\n{'='*80}")
    print(f"خلاصه:")
    print(f"  - تعداد به‌روزرسانی شده: {updated_count}")
    print(f"  - تعداد رد شده (تصویر یافت نشد): {not_found_count}")
    print(f"  - تعداد نگه داشته شده: {skipped_count}")
    print(f"{'='*80}")


if __name__ == '__main__':
    update_event_images()
