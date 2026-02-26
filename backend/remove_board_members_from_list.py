#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
اسکریپت حذف اعضای هیئت مدیره از لیست اعضای عمومی
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ispp_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# لیست اعضای هیئت مدیره که باید حذف شوند
BOARD_MEMBERS_TO_REMOVE = [
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


def remove_board_members():
    """حذف اعضای هیئت مدیره از دیتابیس"""
    print("=" * 80)
    print("شروع حذف اعضای هیئت مدیره از لیست اعضا...")
    print("=" * 80)
    
    deleted_count = 0
    not_found_count = 0
    
    for member_name in BOARD_MEMBERS_TO_REMOVE:
        try:
            # جستجو بر اساس نام فارسی
            users = User.objects.filter(first_name=member_name)
            
            if users.exists():
                count = users.count()
                users.delete()
                deleted_count += count
                print(f"✓ حذف شد: {member_name} ({count} رکورد)")
            else:
                not_found_count += 1
                print(f"⚠ یافت نشد: {member_name}")
                
        except Exception as e:
            print(f"✗ خطا در حذف {member_name}: {str(e)}")
    
    print(f"\n{'='*80}")
    print(f"خلاصه:")
    print(f"  - تعداد حذف شده: {deleted_count}")
    print(f"  - تعداد یافت نشده: {not_found_count}")
    print(f"{'='*80}")


if __name__ == '__main__':
    confirm = input("آیا مطمئن هستید که می‌خواهید اعضای هیئت مدیره را حذف کنید؟ (yes/no): ")
    if confirm.lower() in ['yes', 'y', 'بله']:
        remove_board_members()
    else:
        print("عملیات لغو شد.")
