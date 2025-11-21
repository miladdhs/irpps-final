"""
Management command to add 5 sample users to the database
Usage: python manage.py add_sample_users
"""
import os
import sys
import shutil
from pathlib import Path
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.files import File
from django.conf import settings
from django.db import transaction

# Fix encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

User = get_user_model()


class Command(BaseCommand):
    help = 'Add 5 sample users to the database with specified profile image'

    def add_arguments(self, parser):
        parser.add_argument(
            '--image',
            type=str,
            default='public/tst2.jpg',
            help='Path to profile image file'
        )

    def handle(self, *args, **options):
        image_path = options['image']
        
        # Get absolute path
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        source_image = base_dir / image_path
        
        if not source_image.exists():
            self.stdout.write(self.style.ERROR(f'Image file not found: {source_image}'))
            return
        
        self.stdout.write(f'Using profile image from: {source_image}')
        
        # Ensure media directory exists
        media_root = Path(settings.MEDIA_ROOT)
        profile_images_dir = media_root / 'profile_images'
        profile_images_dir.mkdir(parents=True, exist_ok=True)
        
        # Sample users data
        sample_users = [
            {
                'username': 'dr_ahmadi',
                'first_name': 'احمد',
                'last_name': 'احمدی',
                'first_name_fa': 'دکتر احمد',
                'last_name_fa': 'احمدی',
                'email': 'dr.ahmadi@ispp.ir',
                'phone': '09121234567',
                'city': 'تهران',
                'specialty': 'متخصص ریه کودکان',
                'experience': 15,
                'rating': 4.8,
                'bio': 'دکتر احمد احمدی متخصص ریه کودکان با بیش از 15 سال تجربه در تشخیص و درمان بیماری‌های تنفسی کودکان است. وی فارغ‌التحصیل دانشگاه علوم پزشکی تهران و دارای بورد تخصصی ریه کودکان می‌باشد.',
                'education': 'دکترای پزشکی - دانشگاه علوم پزشکی تهران\nتخصص ریه کودکان - بیمارستان کودکان مفید',
                'publications': 'بیش از 25 مقاله علمی در زمینه بیماری‌های ریوی کودکان\nنویسنده کتاب "راهنمای تشخیص آسم کودکان"',
                'awards': 'جایزه بهترین پژوهشگر سال 1400 انجمن ریه کودکان\nتقدیرنامه از وزارت بهداشت برای خدمات برجسته',
                'certifications': 'گواهینامه بین‌المللی طب اطفال\nگواهینامه تخصصی ریه کودکان از انجمن اروپایی',
                'research_interests': 'آسم کودکان، بیماری‌های مزمن ریوی، آلرژی تنفسی',
                'languages': 'فارسی، انگلیسی، عربی'
            },
            {
                'username': 'dr_karimi',
                'first_name': 'فاطمه',
                'last_name': 'کریمی',
                'first_name_fa': 'دکتر فاطمه',
                'last_name_fa': 'کریمی',
                'email': 'dr.karimi@ispp.ir',
                'phone': '09129876543',
                'city': 'اصفهان',
                'specialty': 'فوق تخصص ریه کودکان',
                'experience': 12,
                'rating': 4.9,
                'bio': 'دکتر فاطمه کریمی فوق تخصص ریه کودکان و یکی از اعضای برجسته انجمن علمی ریه کودکان ایران است. تخصص ویژه وی در زمینه درمان آسم شدید کودکان و بیماری‌های نادر ریوی می‌باشد.',
                'education': 'دکترای پزشکی - دانشگاه علوم پزشکی اصفهان\nفوق تخصص ریه کودکان - بیمارستان کودکان علی اصغر',
                'publications': 'نویسنده بیش از 30 مقاله در مجلات معتبر بین‌المللی\nسردبیر مجله ریه کودکان ایران',
                'awards': 'جایزه ملی تحقیقات پزشکی 1399\nنشان عالی خدمات پزشکی از رئیس جمهور',
                'certifications': 'عضو انجمن بین‌المللی ریه کودکان\nگواهینامه تخصصی از دانشگاه هاروارد',
                'research_interests': 'بیماری‌های نادر ریوی، ژن درمانی، طب شخصی‌سازی شده',
                'languages': 'فارسی، انگلیسی، فرانسوی'
            },
            {
                'username': 'dr_hosseini',
                'first_name': 'محمد',
                'last_name': 'حسینی',
                'first_name_fa': 'دکتر محمد',
                'last_name_fa': 'حسینی',
                'email': 'dr.hosseini@ispp.ir',
                'phone': '09135551234',
                'city': 'مشهد',
                'specialty': 'متخصص اطفال و ریه کودکان',
                'experience': 18,
                'rating': 4.7,
                'bio': 'دکتر محمد حسینی با بیش از 18 سال تجربه در زمینه طب اطفال و ریه کودکان، یکی از پیشگامان در استفاده از روش‌های نوین درمانی در شرق کشور محسوب می‌شود.',
                'education': 'دکترای پزشکی - دانشگاه علوم پزشکی مشهد\nتخصص اطفال و فوق تخصص ریه کودکان',
                'publications': 'نویسنده 20 مقاله علمی و 3 کتاب تخصصی\nمترجم کتاب "اصول ریه کودکان نلسون"',
                'awards': 'استاد نمونه دانشگاه علوم پزشکی مشهد\nجایزه انجمن پزشکان ایران برای نوآوری در درمان',
                'certifications': 'گواهینامه بین‌المللی اولتراسونوگرافی ریه\nمدرک تخصصی طب اورژانس کودکان',
                'research_interests': 'اولتراسونوگرافی ریه، طب اورژانس تنفسی، تله‌مدیسین',
                'languages': 'فارسی، انگلیسی، عربی'
            },
            {
                'username': 'dr_moradi',
                'first_name': 'زهرا',
                'last_name': 'مرادی',
                'first_name_fa': 'دکتر زهرا',
                'last_name_fa': 'مرادی',
                'email': 'dr.moradi@ispp.ir',
                'phone': '09177778888',
                'city': 'شیراز',
                'specialty': 'متخصص آلرژی و ایمونولوژی کودکان',
                'experience': 10,
                'rating': 4.6,
                'bio': 'دکتر زهرا مرادی متخصص آلرژی و ایمونولوژی کودکان است که تخصص ویژه‌ای در زمینه تشخیص و درمان آلرژی‌های تنفسی و آسم کودکان دارد. وی عضو فعال انجمن آلرژی ایران نیز می‌باشد.',
                'education': 'دکترای پزشکی - دانشگاه علوم پزشکی شیراز\nفوق تخصص آلرژی و ایمونولوژی کودکان - بیمارستان نمازی',
                'publications': 'نویسنده 15 مقاله در زمینه آلرژی کودکان\nهمکار در تألیف "راهنمای آلرژی کودکان ایران"',
                'awards': 'جایزه بهترین پژوهش بالینی انجمن آلرژی ایران\nتقدیرنامه از دانشگاه علوم پزشکی شیراز',
                'certifications': 'گواهینامه بین‌المللی تست‌های آلرژی\nمدرک تخصصی ایمونوتراپی از اروپا',
                'research_interests': 'آلرژی غذایی، ایمونوتراپی، آسم شدید کودکان',
                'languages': 'فارسی، انگلیسی'
            },
            {
                'username': 'dr_rezaei',
                'first_name': 'علی',
                'last_name': 'رضایی',
                'first_name_fa': 'دکتر علی',
                'last_name_fa': 'رضایی',
                'email': 'dr.rezaei@ispp.ir',
                'phone': '09194445555',
                'city': 'تبریز',
                'specialty': 'متخصص ریه کودکان و طب خواب',
                'experience': 8,
                'rating': 4.5,
                'bio': 'دکتر علی رضایی جوان‌ترین عضو هیئت علمی انجمن ریه کودکان است که تخصص نوینی در زمینه اختلالات خواب مرتبط با تنفس در کودکان دارد. وی پیشگام استفاده از فناوری‌های نوین در تشخیص است.',
                'education': 'دکترای پزشکی - دانشگاه علوم پزشکی تبریز\nفلوشیپ طب خواب کودکان - بیمارستان کودکان تهران',
                'publications': 'نویسنده 12 مقاله در زمینه طب خواب کودکان\nمقالات متعدد در مجلات بین‌المللی',
                'awards': 'جایزه بهترین پژوهشگر جوان انجمن ریه کودکان\nبورسیه تحقیقاتی از دانشگاه استنفورد',
                'certifications': 'گواهینامه بین‌المللی طب خواب\nمدرک تخصصی پلی‌سومنوگرافی کودکان',
                'research_interests': 'اختلالات خواب تنفسی، آپنه خواب کودکان، فناوری‌های تشخیصی نوین',
                'languages': 'فارسی، انگلیسی، ترکی آذربایجانی'
            }
        ]
        
        try:
            with transaction.atomic():
                created_count = 0
                updated_count = 0
                
                for user_data in sample_users:
                    username = user_data.pop('username')
                    
                    # Check if user already exists
                    user, created = User.objects.get_or_create(
                        username=username,
                        defaults=user_data
                    )
                    
                    if created:
                        # Set password
                        user.set_password('123456')  # Default password
                        user.save()
                        created_count += 1
                        self.stdout.write(f'Created user: {username} - {user_data["first_name_fa"]} {user_data["last_name_fa"]}')
                    else:
                        # Update existing user
                        for key, value in user_data.items():
                            setattr(user, key, value)
                        user.set_password('123456')  # Reset password
                        user.save()
                        updated_count += 1
                        self.stdout.write(f'Updated user: {username} - {user_data["first_name_fa"]} {user_data["last_name_fa"]}')
                    
                    # Set profile image
                    try:
                        # Create a unique filename for each user
                        image_filename = f'profile_{username}.jpg'
                        dest_image = profile_images_dir / image_filename
                        
                        # Copy the source image to media directory
                        shutil.copy2(source_image, dest_image)
                        
                        # Set the profile image
                        with open(dest_image, 'rb') as f:
                            user.profile_image.save(
                                image_filename,
                                File(f),
                                save=True
                            )
                        
                        self.stdout.write(f'  → Set profile image for {username}')
                        
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'  → Warning: Could not set profile image for {username}: {str(e)}'))
                
                # Summary
                self.stdout.write('')
                self.stdout.write(self.style.SUCCESS('=' * 60))
                self.stdout.write(self.style.SUCCESS('Sample Users Creation Summary:'))
                self.stdout.write(self.style.SUCCESS(f'  Created: {created_count}'))
                self.stdout.write(self.style.SUCCESS(f'  Updated: {updated_count}'))
                self.stdout.write(self.style.SUCCESS(f'  Total processed: {len(sample_users)}'))
                self.stdout.write(self.style.SUCCESS('  Default password for all users: 123456'))
                self.stdout.write(self.style.SUCCESS('=' * 60))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            import traceback
            traceback.print_exc()

