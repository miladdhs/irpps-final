#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to:
1. Remove board members from members list
2. Add new events to database
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

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ispp_project.settings')
django.setup()

from django.contrib.auth import get_user_model
from events.models import Event
import shutil

User = get_user_model()

# لیست اعضای هیئت مدیره که باید از لیست اعضا حذف شوند
BOARD_MEMBERS_TO_HIDE = [
    'دکتر امیر رضائی',
    'دکتر بابک قالیباف',
    'دکتر حسینعلی غفاری پور',
    'دکتر ذلفا مدرسی',
    'دکتر روح الله شیرزادی',
    'دکتر سهیلا خلیل زاده',
    'دکتر سید احمد طباطبائی',
    'دکتر سید جواد سیدی',
    'دکتر سید حسین میر لوحی',
    'دکتر سید محمد رضا میرکریمی',
    'دکتر علیرضا اسدی',
    'دکتر علیرضا عشقی',
    'دکتر قرم تاج خان بابایی',
    'دکتر لعبت شاهکار',
    'دکتر مجید کیوانفر',
    'دکتر محسن علی سمیر',
    'دکتر محمد رضا مدرسی',
    'دکتر محمد رضائی',
    'دکتر معصومه قاسمپور علمداری',
    'دکتر نازنین فرحبخش',
]

def hide_board_members():
    """Hide board members from public members list"""
    print("\n" + "="*60)
    print("حذف اعضای هیئت مدیره از لیست اعضا")
    print("="*60)
    
    hidden_count = 0
    not_found_count = 0
    
    for member_name in BOARD_MEMBERS_TO_HIDE:
        try:
            # جستجو بر اساس نام فارسی
            users = User.objects.filter(first_name=member_name)
            
            if users.exists():
                for user in users:
                    # غیرفعال کردن کاربر (یا می‌توانید حذف کنید)
                    user.is_active = False
                    user.save()
                    print(f"✅ حذف شد: {member_name}")
                    hidden_count += 1
            else:
                print(f"⚠️  یافت نشد: {member_name}")
                not_found_count += 1
                
        except Exception as e:
            print(f"❌ خطا در حذف {member_name}: {e}")
    
    print(f"\n{'='*60}")
    print(f"✅ {hidden_count} عضو حذف شد")
    print(f"⚠️  {not_found_count} عضو یافت نشد")
    print(f"{'='*60}")
    
    return hidden_count > 0

def add_events():
    """Add new events to database"""
    print("\n" + "="*60)
    print("افزودن رویدادهای جدید به دیتابیس")
    print("="*60)
    
    # Get or create a staff user for created_by
    staff_user = User.objects.filter(is_staff=True, is_active=True).first()
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

این وبینار به مناسبت روز جهانی آسم برگزار شد و به بررسی آخرین یافته‌ها و روش‌های درمانی در زمینه آسم کودکان پرداخت.

موضوعات:
• آخرین یافته‌های تحقیقاتی در زمینه آسم کودکان
• روش‌های نوین درمانی
• مدیریت بحران‌های تنفسی
• پیشگیری و کنترل آسم''',
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

این وبینار به مناسبت روز جهانی پنومونی برگزار شد و به بررسی پیشگیری و درمان پنومونی در کودکان پرداخت.

موضوعات:
• تشخیص زودهنگام پنومونی
• روش‌های درمانی مؤثر
• پیشگیری از عفونت‌های تنفسی
• واکسیناسیون و اهمیت آن''',
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

این کنگره با حضور متخصصان برجسته ریه کودکان برگزار شد و به بررسی جامع بیماری‌های تنفسی کودکان پرداخت.

محورهای کنگره:
• بیماری‌های مزمن تنفسی
• عفونت‌های ریوی
• آسم و آلرژی
• اختلالات خواب تنفسی
• تکنیک‌های تشخیصی نوین''',
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

این همایش به صورت وبینار چهار روزه برگزار شد و به بررسی موضوعات مختلف در حوزه ریه کودکان پرداخت.

برنامه همایش:
• روز اول: بیماری‌های انسدادی ریه
• روز دوم: عفونت‌های تنفسی
• روز سوم: آسم و آلرژی
• روز چهارم: تکنیک‌های تشخیصی و درمانی''',
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

این سمینار با حضور اساتید برجسته برگزار شد و به بررسی آخرین پیشرفت‌ها در زمینه بیماری‌های تنفسی کودکان پرداخت.

موضوعات سمینار:
• پیشرفت‌های تشخیصی
• درمان‌های نوین
• مدیریت بیماری‌های مزمن
• آموزش و پژوهش''',
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

این کنگره با حضور گسترده متخصصان برگزار شد و به بررسی چالش‌ها و راهکارهای درمانی در بیماری‌های تنفسی کودکان پرداخت.

محورهای کنگره:
• چالش‌های تشخیصی
• راهکارهای درمانی نوین
• مدیریت بیماری‌های پیچیده
• همکاری‌های بین‌المللی''',
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
    print("اسکریپت پاکسازی و افزودن رویدادها")
    print("=" * 60)
    
    try:
        # Step 1: Hide board members
        hide_board_members()
        
        # Step 2: Add events
        add_events()
        
        print("\n" + "=" * 60)
        print("✅ عملیات با موفقیت انجام شد")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ خطای کلی: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
