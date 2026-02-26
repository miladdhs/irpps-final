#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add new events directly to the database
Usage: python add_events.py
"""
import os
import sys
import django
from pathlib import Path

# Fix encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Add backend directory to path
backend_dir = Path(__file__).parent / 'backend'
sys.path.insert(0, str(backend_dir))

# Set database environment variables for online database (must be set before Django setup)
os.environ['DB_HOST'] = '45.149.79.217'
os.environ['DB_USER'] = 'root'
os.environ['DB_PASSWORD'] = 'Re27cwv9TsNCBqPvbYgJ'
os.environ['DB_NAME'] = 'irporg_DB'
os.environ['DB_PORT'] = '3306'
os.environ['IS_DOCKER'] = 'False'

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ispp_project.settings')
django.setup()

from django.contrib.auth import get_user_model
from events.models import Event
import shutil

User = get_user_model()

def add_events():
    # Get or create a staff user for created_by
    staff_user = User.objects.filter(is_staff=True).first()
    if not staff_user:
        print("❌ خطا: هیچ کاربر staff یافت نشد. لطفاً ابتدا یک کاربر staff ایجاد کنید.")
        return False

    # Base paths
    base_dir = Path(__file__).parent
    frontend_content = base_dir / 'frontend' / 'public' / 'Content'
    media_dir = base_dir / 'backend' / 'media' / 'events' / 'covers'
    media_dir.mkdir(parents=True, exist_ok=True)

    # Event 1: وبینار روز جهانی آسم ۲۰۲۵
    event1_data = {
        'title': 'وبینار روز جهانی آسم ۲۰۲۵',
        'slug': 'webinar-world-asthma-day-2025',
        'description': '''وبینار روز جهانی آسم ۲۰۲۵

این وبینار به مناسبت روز جهانی آسم برگزار شد و به بررسی آخرین یافته‌ها و روش‌های درمانی در زمینه آسم کودکان پرداخت.''',
        'short_description': 'وبینار روز جهانی آسم ۲۰۲۵',
        'event_type': 'webinar',
        'location': 'آنلاین',
        'event_month': 2,  # اردیبهشت
        'event_year': 1404,
        'is_published': True,
        'is_featured': False,
        'created_by': staff_user,
        'cover_image_path': 'asthma.jpg',
    }

    # Event 2: وبینار روز جهانی پنومونی
    event2_data = {
        'title': 'وبینار روز جهانی پنومونی',
        'slug': 'webinar-world-pneumonia-day',
        'description': '''وبینار روز جهانی پنومونی

این وبینار به مناسبت روز جهانی پنومونی برگزار شد و به بررسی پیشگیری و درمان پنومونی در کودکان پرداخت.''',
        'short_description': 'وبینار روز جهانی پنومونی',
        'event_type': 'webinar',
        'location': 'آنلاین',
        'event_month': 8,  # آبان
        'event_year': 1403,
        'is_published': True,
        'is_featured': False,
        'created_by': staff_user,
        'cover_image_path': 'penomoni.jpg',
    }

    # Event 3: اولین کنگره سراسری بیماری‌های تنفسی کودکان
    event3_data = {
        'title': 'اولین کنگره سراسری بیماری‌های تنفسی کودکان',
        'slug': 'first-national-congress-pediatric-respiratory',
        'description': '''اولین کنگره سراسری بیماری‌های تنفسی کودکان

این کنگره با حضور متخصصان برجسته ریه کودکان برگزار شد و به بررسی جامع بیماری‌های تنفسی کودکان پرداخت.''',
        'short_description': 'اولین کنگره سراسری بیماری‌های تنفسی کودکان',
        'event_type': 'congress',
        'location': 'تهران',
        'event_month': 6,  # شهریور
        'event_year': 1396,
        'is_published': True,
        'is_featured': False,
        'created_by': staff_user,
        'cover_image_path': 'avalin kongere.jpg',
    }

    # Event 4: چهارمین همایش سالیانه انجمن علمی ریه کودکان ایران
    event4_data = {
        'title': 'چهارمین همایش سالیانه انجمن علمی ریه کودکان ایران (وبینار چهار روزه)',
        'slug': 'fourth-annual-conference-ispp',
        'description': '''چهارمین همایش سالیانه انجمن علمی ریه کودکان ایران

این همایش به صورت وبینار چهار روزه برگزار شد و به بررسی موضوعات مختلف در حوزه ریه کودکان پرداخت.''',
        'short_description': 'چهارمین همایش سالیانه انجمن علمی ریه کودکان ایران (وبینار چهار روزه)',
        'event_type': 'conference',
        'location': 'آنلاین',
        'event_month': 7,  # مهر
        'event_year': 1399,
        'is_published': True,
        'is_featured': False,
        'created_by': staff_user,
        'cover_image_path': 'chaharomin hamayesh.jpg',
    }

    # Event 5: ششمین سمینار سالانه بیماری‌های تنفسی کودکان
    event5_data = {
        'title': 'ششمین سمینار سالانه بیماری‌های تنفسی کودکان',
        'slug': 'sixth-annual-seminar-pediatric-respiratory',
        'description': '''ششمین سمینار سالانه بیماری‌های تنفسی کودکان

این سمینار با حضور اساتید برجسته برگزار شد و به بررسی آخرین پیشرفت‌ها در زمینه بیماری‌های تنفسی کودکان پرداخت.''',
        'short_description': 'ششمین سمینار سالانه بیماری‌های تنفسی کودکان',
        'event_type': 'seminar',
        'location': 'تهران',
        'event_month': 9,  # آذر
        'event_year': 1401,
        'is_published': True,
        'is_featured': False,
        'created_by': staff_user,
        'cover_image_path': 'seshomin seminar.jpg',
    }

    # Event 6: سومین کنگره سراسری بیماری‌های تنفسی کودکان
    event6_data = {
        'title': 'سومین کنگره سراسری بیماری‌های تنفسی کودکان',
        'slug': 'third-national-congress-pediatric-respiratory',
        'description': '''سومین کنگره سراسری بیماری‌های تنفسی کودکان

این کنگره با حضور گسترده متخصصان برگزار شد و به بررسی چالش‌ها و راهکارهای درمانی در بیماری‌های تنفسی کودکان پرداخت.''',
        'short_description': 'سومین کنگره سراسری بیماری‌های تنفسی کودکان',
        'event_type': 'congress',
        'location': 'تهران',
        'event_month': 5,  # مرداد
        'event_year': 1400,
        'is_published': True,
        'is_featured': False,
        'created_by': staff_user,
        'cover_image_path': 'sevomin kongere.jpg',
    }

    events_data = [event1_data, event2_data, event3_data, event4_data, event5_data, event6_data]
    success_count = 0
    skip_count = 0

    for event_data in events_data:
        cover_image_path = event_data.pop('cover_image_path', None)
        
        # Check if event already exists
        if Event.objects.filter(slug=event_data['slug']).exists():
            print(f"⚠️  رویداد «{event_data['title']}» قبلاً وجود دارد. رد می‌شود...")
            skip_count += 1
            continue

        # Copy cover image if provided
        cover_image = None
        if cover_image_path:
            source_image = frontend_content / cover_image_path
            if source_image.exists():
                dest_image = media_dir / cover_image_path
                shutil.copy2(source_image, dest_image)
                # Set cover_image field (relative to MEDIA_ROOT)
                cover_image = f'events/covers/{cover_image_path}'
                print(f"✅ تصویر کپی شد: {cover_image_path}")
            else:
                print(f"⚠️  تصویر یافت نشد: {source_image}")

        # Create event
        try:
            event = Event.objects.create(
                **event_data,
                cover_image=cover_image
            )
            print(f"✅ رویداد با موفقیت ایجاد شد: {event.title}")
            success_count += 1
        except Exception as e:
            print(f"❌ خطا در ایجاد رویداد «{event_data['title']}»: {e}")
            continue

    print(f"\n{'='*60}")
    print(f"✅ {success_count} رویداد با موفقیت اضافه شد")
    if skip_count > 0:
        print(f"⚠️  {skip_count} رویداد رد شد (قبلاً وجود داشت)")
    print(f"{'='*60}")
    
    return success_count > 0

if __name__ == '__main__':
    print("=" * 60)
    print("افزودن رویدادهای جدید به دیتابیس")
    print("=" * 60)
    print()
    
    try:
        add_events()
    except Exception as e:
        print(f"\n❌ خطای کلی: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

