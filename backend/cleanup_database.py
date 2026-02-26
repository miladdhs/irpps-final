#!/usr/bin/env python
"""
اسکریپت تمیزکاری دیتابیس
1. حذف کاربران خاص (احمد، زهرا، علی، فاطمه، محمد، میلاد)
2. تنظیم مهلت ثبت‌نام برای رویدادهای قدیمی (قبل از اسفند 1404)
"""
import os
import sys
import django
from datetime import date

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ispp_project.settings')
django.setup()

from accounts.models import CustomUser
from events.models import Event
from django.db.models import Q


def delete_specific_users():
    """حذف کاربران خاص از دیتابیس"""
    names_to_delete = ['احمد', 'زهرا', 'علی', 'فاطمه', 'محمد', 'میلاد']
    
    print("=" * 50)
    print("حذف کاربران خاص...")
    print("=" * 50)
    
    deleted_count = 0
    for name in names_to_delete:
        # جستجو در first_name (نام فارسی)
        users = CustomUser.objects.filter(
            Q(first_name__icontains=name) | 
            Q(username__icontains=name)
        ).exclude(is_superuser=True)  # حفظ سوپریوزرها
        
        for user in users:
            print(f"حذف کاربر: {user.username} - {user.first_name} {user.last_name}")
            user.delete()
            deleted_count += 1
    
    print(f"\n✓ تعداد {deleted_count} کاربر حذف شد")
    return deleted_count


def fix_old_events_registration_deadline():
    """تنظیم مهلت ثبت‌نام برای رویدادهای قدیمی"""
    print("\n" + "=" * 50)
    print("تنظیم مهلت ثبت‌نام رویدادهای قدیمی...")
    print("=" * 50)
    
    # رویدادهایی که قبل از اسفند 1404 هستند
    # اسفند 1404 = سال 1404، ماه 12
    old_events = Event.objects.filter(
        Q(event_year__lt=1404) | 
        Q(event_year=1404, event_month__lt=12)
    )
    
    updated_count = 0
    for event in old_events:
        # محاسبه تاریخ پایان رویداد (آخرین روز ماه رویداد)
        if event.event_year and event.event_month:
            # تبدیل تاریخ شمسی به میلادی (تقریبی)
            # برای سادگی، از یک تاریخ گذشته استفاده می‌کنیم
            
            # محاسبه تعداد روزهای هر ماه شمسی
            days_in_month = 31 if event.event_month <= 6 else (30 if event.event_month <= 11 else 29)
            
            # تبدیل تقریبی تاریخ شمسی به میلادی
            # سال 1404 شمسی ≈ 2025-2026 میلادی
            gregorian_year = event.event_year + 621
            
            # ماه‌های شمسی به میلادی (تقریبی)
            month_mapping = {
                1: (3, 21), 2: (4, 21), 3: (5, 22), 4: (6, 22),
                5: (7, 23), 6: (8, 23), 7: (9, 23), 8: (10, 23),
                9: (11, 22), 10: (12, 22), 11: (1, 21), 12: (2, 20)
            }
            
            month, day = month_mapping.get(event.event_month, (1, 1))
            
            # اگر ماه 11 یا 12 است، سال میلادی را یکی اضافه می‌کنیم
            if event.event_month >= 11:
                gregorian_year += 1
            
            try:
                # تاریخ پایان ماه رویداد
                deadline = date(gregorian_year, month, min(day + days_in_month - 1, 28))
                
                if event.registration_deadline != deadline:
                    old_deadline = event.registration_deadline
                    event.registration_deadline = deadline
                    event.save()
                    
                    print(f"رویداد: {event.title}")
                    print(f"  سال/ماه: {event.event_year}/{event.event_month}")
                    print(f"  مهلت قبلی: {old_deadline}")
                    print(f"  مهلت جدید: {deadline}")
                    print()
                    
                    updated_count += 1
            except ValueError as e:
                print(f"خطا در تنظیم تاریخ برای رویداد {event.title}: {e}")
    
    print(f"✓ تعداد {updated_count} رویداد به‌روزرسانی شد")
    return updated_count


def main():
    """اجرای اصلی اسکریپت"""
    print("\n" + "=" * 50)
    print("شروع تمیزکاری دیتابیس")
    print("=" * 50 + "\n")
    
    try:
        # 1. حذف کاربران خاص
        deleted_users = delete_specific_users()
        
        # 2. تنظیم مهلت ثبت‌نام رویدادهای قدیمی
        updated_events = fix_old_events_registration_deadline()
        
        print("\n" + "=" * 50)
        print("خلاصه نتایج:")
        print("=" * 50)
        print(f"✓ کاربران حذف شده: {deleted_users}")
        print(f"✓ رویدادهای به‌روزرسانی شده: {updated_events}")
        print("\n✓ تمیزکاری دیتابیس با موفقیت انجام شد!")
        
    except Exception as e:
        print(f"\n✗ خطا در اجرای اسکریپت: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
