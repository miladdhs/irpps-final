#!/usr/bin/env python
"""
Script to add initial services to the database
Run this after creating the services app and running migrations
"""
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ispp_project.settings')
django.setup()

from services.models import Service

def add_services():
    """Add initial services to database"""
    
    services_data = [
        {
            'title': 'مشاوره تخصصی',
            'description': 'ارائه مشاوره‌های علمی و تخصصی در زمینه بیماری‌های ریوی نوزادان و کودکان',
            'icon': 'medical_information',
            'link': '/contact',
            'link_text': 'درخواست مشاوره',
            'order': 1
        },
        {
            'title': 'درمان‌های نوین',
            'description': 'معرفی و بکارگیری جدیدترین پروتکل‌های درمانی بین‌المللی برای بیماران تنفسی',
            'icon': 'healing',
            'link': '/services',
            'link_text': 'اطلاعات بیشتر',
            'order': 2
        },
        {
            'title': 'پیشگیری و سلامت',
            'description': 'برنامه‌های غربالگری و آگاهی‌رسانی جهت جلوگیری از بروز بیماری‌های مزمن ریوی',
            'icon': 'health_and_safety',
            'link': '/education',
            'link_text': 'برنامه‌های پیشگیری',
            'order': 3
        },
        {
            'title': 'آموزش مداوم',
            'description': 'برگزاری کارگاه‌ها و کنفرانس‌های علمی برای پزشکان و متخصصان سراسر کشور',
            'icon': 'school',
            'link': '/events',
            'link_text': 'رویدادهای آموزشی',
            'order': 4
        },
        {
            'title': 'پژوهش علمی',
            'description': 'حمایت از پایان‌نامه‌ها و طرح‌های تحقیقاتی در حوزه تنفس و آسم کودکان',
            'icon': 'biotech',
            'link': '/publications',
            'link_text': 'پروژه‌های تحقیقاتی',
            'order': 5
        },
        {
            'title': 'حمایت از بیماران',
            'description': 'ارائه خدمات حمایتی و مددکاری برای خانواده‌های دارای کودک با بیماری خاص',
            'icon': 'volunteer_activism',
            'link': '/contact',
            'link_text': 'درخواست حمایت',
            'order': 6
        }
    ]
    
    print("🚀 شروع اضافه کردن خدمات...")
    
    for service_data in services_data:
        service, created = Service.objects.get_or_create(
            title=service_data['title'],
            defaults=service_data
        )
        
        if created:
            print(f"✅ خدمت '{service.title}' با موفقیت اضافه شد")
        else:
            # Update existing service
            for key, value in service_data.items():
                setattr(service, key, value)
            service.save()
            print(f"🔄 خدمت '{service.title}' به‌روزرسانی شد")
    
    print(f"\n✨ تعداد کل خدمات: {Service.objects.count()}")
    print("✅ عملیات با موفقیت انجام شد!")

if __name__ == '__main__':
    add_services()
