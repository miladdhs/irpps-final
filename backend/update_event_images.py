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
    media_dir = Path(__file__).parent / 'media' / 'events' / 'covers'
    media_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"مسیر media: {media_dir}")
    print(f"تصاویر موجود در media: {list(media_dir.glob('*.jpg'))}\n")
    
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
            # بررسی وجود تصویر در media directory
            dest_image = media_dir / image_file
            
            if dest_image.exists():
                # حذف تصویر قبلی اگر وجود دارد و متفاوت است
                if event.cover_image:
                    old_image_path = Path(__file__).parent / 'media' / str(event.cover_image)
                    if old_image_path.exists() and old_image_path.name != image_file:
                        try:
                            old_image_path.unlink()
                            print(f"  🗑 تصویر قبلی حذف شد: {old_image_path.name}")
                        except Exception as e:
                            print(f"  ⚠ خطا در حذف تصویر قبلی: {e}")
                
                # به‌روزرسانی رویداد
                event.cover_image = f'events/covers/{image_file}'
                event.save()
                
                updated_count += 1
                print(f"  ✓ تصویر به‌روزرسانی شد: {image_file}")
            else:
                print(f"  ⚠ تصویر یافت نشد در: {dest_image}")
                print(f"     لطفاً ابتدا تصویر را به مسیر media/events/covers/ کپی کنید")
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
