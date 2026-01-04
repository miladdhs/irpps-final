"""
Management command to add new events
Usage: python manage.py add_new_events
"""
import os
import shutil
from pathlib import Path
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings
from events.models import Event

User = get_user_model()


class Command(BaseCommand):
    help = 'Add new events to the database'

    def handle(self, *args, **options):
        # Get or create a staff user for created_by
        staff_user = User.objects.filter(is_staff=True).first()
        if not staff_user:
            self.stdout.write(self.style.ERROR('No staff user found. Please create one first.'))
            return

        # Base paths
        base_dir = Path(settings.BASE_DIR)
        frontend_content = base_dir.parent / 'frontend' / 'public' / 'Content' / 'lAST'
        media_dir = base_dir / 'media' / 'events' / 'covers'
        media_dir.mkdir(parents=True, exist_ok=True)

        # Event 1: ورکشاپ POCUS
        event1_data = {
            'title': 'ورکشاپ عملی POCUS (سونوگرافی در نقطه مراقبت در بخش مراقبت‌های ویژه) در ریه اطفال',
            'slug': 'workshop-pocus-1404',
            'description': '''عنوان رویداد:
ورکشاپ عملی POCUS (سونوگرافی در نقطه مراقبت در بخش مراقبت‌های ویژه) در ریه اطفال

برگزار کننده:
شرکت ایده گستر قدرت

سرفصل‌های دوره:
این کارگاه شامل مباحث تئوری و عملی زیر می‌باشد:
• اکوکاردیوگرافی پایه: نماهای اصلی، EF، و افیوژن پریکارد
• اولتراسوند پایه ریه: علائم، پنوموتوراکس، و افیوژن پلورال
• سونوگرافی اندام تحتانی
• ارزیابی وضعیت حجم مایعات بدن
• eFAST (سونوگرافی متمرکز برای تروما)
• ارزیابی دیافراگم با اولتراسوند
• اولتراسوند شکم در ICU
• ارزیابی راه هوایی با اولتراسوند

مخاطبین هدف کارگاه:
این دوره برای گروه‌های زیر طراحی شده است:
• متخصصین داخلی
• فوق تخصصین ریه
• فوق تخصصین ریه کودکان
• متخصصین اورژانس
• متخصصین بیهوشی
• جراحان توراکس

مدرس کارگاه:
جناب آقای دکتر مهدی ندیری
فوق تخصص ریه از دانشگاه علوم پزشکی تبریز
مسئول زیر شاخه آموزش سونوگرافی انجمن ریه

اطلاعات برگزاری و ثبت‌نام:
تاریخ برگزاری: ۹ بهمن ماه ۱۴۰۴
ظرفیت: ۱۵ نفر (به صورت حضوری)
نحوه ثبت‌نام: جهت ثبت نام در کارگاه با شماره ۰۹۳۳۱۱۷۴۶۵۳ تماس بگیرید.''',
            'short_description': 'ورکشاپ عملی POCUS در ریه اطفال - شرکت ایده گستر قدرت - ۹ بهمن ۱۴۰۴',
            'event_type': 'workshop',
            'location': 'تهران',
            'event_month': 11,  # بهمن
            'event_year': 1404,
            'organizer': 'شرکت ایده گستر قدرت',
            'target_audience': 'متخصصین داخلی، فوق تخصصین ریه، فوق تخصصین ریه کودکان، متخصصین اورژانس، متخصصین بیهوشی، جراحان توراکس',
            'speakers': 'جناب آقای دکتر مهدی ندیری - فوق تخصص ریه از دانشگاه علوم پزشکی تبریز',
            'contact_info': 'جهت ثبت نام در کارگاه با شماره ۰۹۳۳۱۱۷۴۶۵۳ تماس بگیرید',
            'max_participants': 15,
            'price': 0,
            'is_published': True,
            'is_featured': False,
            'created_by': staff_user,
            'cover_image_path': 'IMG_20251104_071318_242.jpg',
        }

        # Event 2: کنفرانس علمی یک روزه
        event2_data = {
            'title': 'کنفرانس علمی یک روزه: بیماری شایع تنفسی کودکان',
            'slug': 'conference-respiratory-children-1404',
            'description': '''عنوان رویداد:
کنفرانس علمی یک روزه: بیماری شایع تنفسی کودکان

برگزار کننده:
دانشگاه علوم پزشکی شهید صدوقی یزد

اطلاعات بازآموزی:
شناسه بازآموزی: 244403
امتیاز: این کنفرانس دارای ۵ امتیاز بازآموزی برای شرکت‌کنندگان می‌باشد.

دبیر علمی:
دکتر سیده ذلفا مدرسی

گروه‌های هدف:
این کنفرانس برای گروه‌های زیر در نظر گرفته شده است:
• پزشکان عمومی
• متخصصین اطفال
• متخصصین گوش، حلق و بینی (ENT)
• متخصصین عفونی
• متخصصین داخلی
• پرستاران
• مراقبین بهداشتی

زمان و مکان برگزاری:
تاریخ: چهارشنبه، سوم دی ماه ۱۴۰۴
مکان: بیمارستان شهید صدوقی، سالن دکتر جوادی''',
            'short_description': 'کنفرانس علمی یک روزه: بیماری شایع تنفسی کودکان - دانشگاه علوم پزشکی شهید صدوقی یزد - ۳ دی ۱۴۰۴',
            'event_type': 'conference',
            'location': 'بیمارستان شهید صدوقی، سالن دکتر جوادی - یزد',
            'event_month': 10,  # دی
            'event_year': 1404,
            'organizer': 'دانشگاه علوم پزشکی شهید صدوقی یزد',
            'target_audience': 'پزشکان عمومی، متخصصین اطفال، متخصصین گوش حلق و بینی، متخصصین عفونی، متخصصین داخلی، پرستاران، مراقبین بهداشتی',
            'speakers': 'دبیر علمی: دکتر سیده ذلفا مدرسی',
            'agenda': 'شناسه بازآموزی: 244403 - امتیاز: ۵ امتیاز بازآموزی',
            'is_published': True,
            'is_featured': False,
            'created_by': staff_user,
            'cover_image_path': 'photo_2026-01-04_12-05-34.jpg',
        }

        # Event 3: چهارمین کنگره بین‌المللی
        event3_data = {
            'title': 'چهارمین کنگره بین‌المللی ریه و اختلالات تنفسی خواب کودکان',
            'slug': 'congress-pediatric-pulmonary-2026',
            'description': '''عنوان رویداد:
چهارمین کنگره بین‌المللی ریه و اختلالات تنفسی خواب کودکان
(4th International Congress of Pediatric Pulmonary and Sleep Medicine)

محل و زمان برگزاری:
محل برگزاری: مرکز طبی کودکان
زمان: ۲۴ تا ۲۶ دی‌ماه ۱۴۰۴ (معادل 14-16 ژانویه 2026)

اطلاعات بازآموزی:
این کنگره دارای امتیاز بازآموزی برای گروه‌های هدف زیر می‌باشد.
شناسه برنامه: 2۴۶۸۵۵

گروه‌های هدف (دارای امتیاز بازآموزی):
• متخصصین کودکان
• فوق تخصص ریه کودکان
• فوق تخصص ایمونولوژی و آلرژی
• فوق تخصص عفونی کودکان
• فوق تخصص نوزادان
• فوق تخصص بیهوشی و مراقبت‌های ویژه
• متخصصین گوش و حلق و بینی
• پزشکان عمومی''',
            'short_description': 'چهارمین کنگره بین‌المللی ریه و اختلالات تنفسی خواب کودکان - مرکز طبی کودکان - ۲۴ تا ۲۶ دی ۱۴۰۴',
            'event_type': 'congress',
            'location': 'مرکز طبی کودکان',
            'event_month': 10,  # دی
            'event_year': 1404,
            'target_audience': 'متخصصین کودکان، فوق تخصص ریه کودکان، فوق تخصص ایمونولوژی و آلرژی، فوق تخصص عفونی کودکان، فوق تخصص نوزادان، فوق تخصص بیهوشی و مراقبت‌های ویژه، متخصصین گوش و حلق و بینی، پزشکان عمومی',
            'agenda': 'شناسه برنامه: 2۴۶۸۵۵ - زمان: ۲۴ تا ۲۶ دی‌ماه ۱۴۰۴ (معادل 14-16 ژانویه 2026)',
            'is_published': True,
            'is_featured': True,  # Mark as featured
            'created_by': staff_user,
            'cover_image_path': None,  # PDF file, no image
        }

        events_data = [event1_data, event2_data, event3_data]

        for event_data in events_data:
            cover_image_path = event_data.pop('cover_image_path', None)
            
            # Check if event already exists
            if Event.objects.filter(slug=event_data['slug']).exists():
                self.stdout.write(self.style.WARNING(f'Event "{event_data["title"]}" already exists. Skipping...'))
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
                    self.stdout.write(self.style.SUCCESS(f'Copied image: {cover_image_path}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Image not found: {source_image}'))

            # Create event
            event = Event.objects.create(
                **event_data,
                cover_image=cover_image
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully created event: {event.title}'))

        self.stdout.write(self.style.SUCCESS('\nAll events have been processed!'))

