#!/usr/bin/env python
"""
اسکریپت اضافه کردن اعضای هیئت مدیره انجمن علمی ریه کودکان ایران
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

# اطلاعات اعضای هیئت مدیره
BOARD_MEMBERS_DATA = {
    # موسسین انجمن (1395)
    'founders_1395': [
        {
            'persian_name': 'دکتر سهیلا خلیل زاده',
            'english_name': 'Dr. Soheila Khalilzadeh',
            'position': 'رئیس انجمن',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1395',
            'role': 'president'
        },
        {
            'persian_name': 'دکتر قمر تاج خانبابائی',
            'english_name': 'Dr. Ghamar Taj Khanbabai',
            'position': 'نائب رئیس',
            'specialty': 'فوق تخصص آسم و آلرژی کودکان',
            'period': '1395',
            'role': 'vice_president'
        },
        {
            'persian_name': 'دکتر محمد رضائی',
            'english_name': 'Dr. Mohammad Rezaei',
            'position': 'دبیر انجمن',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1395',
            'role': 'secretary'
        },
        {
            'persian_name': 'دکتر مجید کیوانفر',
            'english_name': 'Dr. Majid Keyvanfar',
            'position': 'خزانه دار',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1395',
            'role': 'treasurer'
        },
        {
            'persian_name': 'دکتر سید احمد طباطبائی',
            'english_name': 'Dr. Seyed Ahmad Tabatabaei',
            'position': 'عضو هیئت مدیره',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1395',
            'role': 'board_member'
        },
        {
            'persian_name': 'دکتر محسن علی سمیر',
            'english_name': 'Dr. Mohsen Ali Samir',
            'position': 'عضو هیئت مدیره',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1395',
            'role': 'board_member'
        },
        {
            'persian_name': 'دکتر حسینعلی غفاری پور',
            'english_name': 'Dr. Hosseinali Ghaffaripour',
            'position': 'عضو هیئت مدیره',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1395',
            'role': 'board_member'
        },
        {
            'persian_name': 'دکتر محمد رضا مدرسی',
            'english_name': 'Dr. Mohammad Reza Modarresi',
            'position': 'عضو هیئت مدیره علی البدل',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1395',
            'role': 'alternate_board_member'
        },
        {
            'persian_name': 'دکتر سید جواد سیدی',
            'english_name': 'Dr. Seyed Javad Seyedi',
            'position': 'عضو هیئت مدیره علی البدل',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1395',
            'role': 'alternate_board_member'
        },
        {
            'persian_name': 'دکتر روح الله شیرزادی',
            'english_name': 'Dr. Rouhollah Shirzadi',
            'position': 'بازرس اصلی',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1395',
            'role': 'main_inspector'
        },
        {
            'persian_name': 'دکتر علیرضا اسدی',
            'english_name': 'Dr. Alireza Asadi',
            'position': 'بازرس علی البدل',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1395',
            'role': 'alternate_inspector'
        },
    ],
    
    # اعضای هیئت مدیره سال 1400
    'board_1400': [
        {
            'persian_name': 'دکتر مجید کیوانفر',
            'english_name': 'Dr. Majid Keyvanfar',
            'position': 'رئیس انجمن',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1400',
            'role': 'president'
        },
        {
            'persian_name': 'دکتر محمد رضائی',
            'english_name': 'Dr. Mohammad Rezaei',
            'position': 'نائب رئیس',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1400',
            'role': 'vice_president'
        },
        {
            'persian_name': 'دکتر امیر رضائی',
            'english_name': 'Dr. Amir Rezaei',
            'position': 'دبیر انجمن',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1400',
            'role': 'secretary'
        },
        {
            'persian_name': 'دکتر علیرضا عشقی',
            'english_name': 'Dr. Alireza Eshghi',
            'position': 'خزانه دار',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1400',
            'role': 'treasurer'
        },
        {
            'persian_name': 'دکتر سید محمد رضا میرکریمی',
            'english_name': 'Dr. Seyed Mohammad Reza Mirkarimi',
            'position': 'عضو هیئت مدیره',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1400',
            'role': 'board_member'
        },
        {
            'persian_name': 'دکتر بابک قالیباف',
            'english_name': 'Dr. Babak Ghalibaf',
            'position': 'عضو هیئت مدیره',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1400',
            'role': 'board_member'
        },
        {
            'persian_name': 'دکتر سید حسین میر لوحی',
            'english_name': 'Dr. Seyed Hossein Mirlouhi',
            'position': 'عضو هیئت مدیره',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1400',
            'role': 'board_member'
        },
        {
            'persian_name': 'دکتر لعبت شاهکار',
            'english_name': 'Dr. Lobat Shahkar',
            'position': 'بازرس اصلی',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1400',
            'role': 'main_inspector'
        },
    ],
    
    # اعضای هیئت مدیره سال 1403
    'board_1403': [
        {
            'persian_name': 'دکتر قمر تاج خانبابائی',
            'english_name': 'Dr. Ghamar Taj Khanbabai',
            'position': 'رئیس انجمن',
            'specialty': 'فوق تخصص آسم و آلرژی کودکان',
            'period': '1403',
            'role': 'president'
        },
        {
            'persian_name': 'دکتر سهیلا خلیل زاده',
            'english_name': 'Dr. Soheila Khalilzadeh',
            'position': 'نائب رئیس',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1403',
            'role': 'vice_president'
        },
        {
            'persian_name': 'دکتر محمد رضائی',
            'english_name': 'Dr. Mohammad Rezaei',
            'position': 'دبیر انجمن',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1403',
            'role': 'secretary'
        },
        {
            'persian_name': 'دکتر نازنین فرحبخش',
            'english_name': 'Dr. Nazanin Farahbakhsh',
            'position': 'خزانه دار',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1403',
            'role': 'treasurer'
        },
        {
            'persian_name': 'دکتر امیر رضائی',
            'english_name': 'Dr. Amir Rezaei',
            'position': 'عضو هیئت مدیره',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1403',
            'role': 'board_member'
        },
        {
            'persian_name': 'دکتر ذلفا مدرسی',
            'english_name': 'Dr. Zolfa Modarresi',
            'position': 'عضو هیئت مدیره',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1403',
            'role': 'board_member'
        },
        {
            'persian_name': 'دکتر علیرضا عشقی',
            'english_name': 'Dr. Alireza Eshghi',
            'position': 'عضو هیئت مدیره',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1403',
            'role': 'board_member'
        },
        {
            'persian_name': 'دکتر معصومه قاسمپور علمداری',
            'english_name': 'Dr. Masoumeh Ghasempour Alamdari',
            'position': 'بازرس اصلی',
            'specialty': 'فوق تخصص ریه کودکان',
            'period': '1403',
            'role': 'main_inspector'
        },
    ]
}


def create_username(persian_name):
    """Generate username from Persian name"""
    # Remove 'دکتر' prefix
    name = persian_name.replace('دکتر ', '').strip()
    # Replace spaces with underscore and make lowercase
    username = name.replace(' ', '_').lower()
    # Add prefix to avoid conflicts
    username = f"board_{username}"
    return username


def add_board_members():
    """Add all board members to database"""
    print("شروع اضافه کردن اعضای هیئت مدیره...")
    print("=" * 80)
    
    created_count = 0
    updated_count = 0
    
    for period_key, members in BOARD_MEMBERS_DATA.items():
        print(f"\n{'='*80}")
        print(f"دوره: {period_key}")
        print(f"{'='*80}")
        
        for member_data in members:
            username = create_username(member_data['persian_name'])
            
            try:
                # Check if user already exists
                user, created = User.objects.get_or_create(
                    username=username,
                    defaults={
                        'first_name': member_data['persian_name'],
                        'last_name': member_data['english_name'],
                        'specialty': member_data['specialty'],
                        'bio': f"{member_data['position']} - دوره {member_data['period']}",
                        'is_active': True,
                        'approval_status': 'approved',
                    }
                )
                
                if created:
                    created_count += 1
                    print(f"✓ ایجاد شد: {member_data['persian_name']} ({member_data['position']})")
                else:
                    # Update existing user
                    user.first_name = member_data['persian_name']
                    user.last_name = member_data['english_name']
                    user.specialty = member_data['specialty']
                    user.bio = f"{member_data['position']} - دوره {member_data['period']}"
                    user.is_active = True
                    user.approval_status = 'approved'
                    user.save()
                    updated_count += 1
                    print(f"⊗ به‌روزرسانی شد: {member_data['persian_name']} ({member_data['position']})")
                    
            except Exception as e:
                print(f"✗ خطا در ایجاد/به‌روزرسانی {member_data['persian_name']}: {str(e)}")
    
    print(f"\n{'='*80}")
    print(f"خلاصه:")
    print(f"  - تعداد ایجاد شده: {created_count}")
    print(f"  - تعداد به‌روزرسانی شده: {updated_count}")
    print(f"  - جمع کل: {created_count + updated_count}")
    print(f"{'='*80}")


if __name__ == '__main__':
    add_board_members()
