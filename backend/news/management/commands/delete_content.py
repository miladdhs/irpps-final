"""
Management command to delete News and Announcements
Usage: python manage.py delete_content --news-ids 1,2,3 --announcement-ids 1,2
"""
import sys
from django.core.management.base import BaseCommand
from news.models import News, Announcement

# Fix encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


class Command(BaseCommand):
    help = 'Delete News and Announcements by IDs'

    def add_arguments(self, parser):
        parser.add_argument(
            '--news-ids',
            type=str,
            default='',
            help='Comma-separated list of News IDs to delete (e.g., "1,2,3")'
        )
        parser.add_argument(
            '--announcement-ids',
            type=str,
            default='',
            help='Comma-separated list of Announcement IDs to delete (e.g., "1,2")'
        )
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Skip confirmation prompt'
        )

    def handle(self, *args, **options):
        news_ids_str = options['news_ids']
        announcement_ids_str = options['announcement_ids']
        confirm = options['confirm']

        # Parse IDs
        news_ids = []
        if news_ids_str:
            try:
                news_ids = [int(id.strip()) for id in news_ids_str.split(',') if id.strip()]
            except ValueError:
                self.stderr.write(self.style.ERROR('Invalid news IDs format. Use comma-separated numbers (e.g., "1,2,3")'))
                return

        announcement_ids = []
        if announcement_ids_str:
            try:
                announcement_ids = [int(id.strip()) for id in announcement_ids_str.split(',') if id.strip()]
            except ValueError:
                self.stderr.write(self.style.ERROR('Invalid announcement IDs format. Use comma-separated numbers (e.g., "1,2")'))
                return

        if not news_ids and not announcement_ids:
            self.stderr.write(self.style.ERROR('No IDs provided. Use --news-ids or --announcement-ids'))
            return

        # Show what will be deleted
        news_items = []
        if news_ids:
            news_items = News.objects.filter(id__in=news_ids)
            if news_items.exists():
                self.stdout.write(self.style.WARNING('\nخبرهای زیر حذف خواهند شد:'))
                for news in news_items:
                    self.stdout.write(f'  - ID {news.id}: {news.title}')
            else:
                self.stdout.write(self.style.WARNING(f'\nخبر با ID های {news_ids} پیدا نشد.'))

        announcement_items = []
        if announcement_ids:
            announcement_items = Announcement.objects.filter(id__in=announcement_ids)
            if announcement_items.exists():
                self.stdout.write(self.style.WARNING('\nاطلاعیه‌های زیر حذف خواهند شد:'))
                for ann in announcement_items:
                    self.stdout.write(f'  - ID {ann.id}: {ann.title}')
            else:
                self.stdout.write(self.style.WARNING(f'\nاطلاعیه با ID های {announcement_ids} پیدا نشد.'))

        if not news_items.exists() and not announcement_items.exists():
            self.stderr.write(self.style.ERROR('\nهیچ رکوردی برای حذف پیدا نشد.'))
            return

        # Confirm
        if not confirm:
            self.stdout.write(self.style.WARNING('\n⚠️  آیا مطمئن هستید که می‌خواهید این رکوردها را حذف کنید؟'))
            response = input('برای تأیید "yes" تایپ کنید: ')
            if response.lower() != 'yes':
                self.stdout.write(self.style.SUCCESS('عملیات لغو شد.'))
                return

        # Delete
        deleted_news = 0
        deleted_announcements = 0

        if news_items.exists():
            for news in news_items:
                title = news.title
                news.delete()
                deleted_news += 1
                self.stdout.write(self.style.SUCCESS(f'  ✓ حذف شد: {title}'))

        if announcement_items.exists():
            for ann in announcement_items:
                title = ann.title
                ann.delete()
                deleted_announcements += 1
                self.stdout.write(self.style.SUCCESS(f'  ✓ حذف شد: {title}'))

        self.stdout.write(self.style.SUCCESS(
            f'\n✅ حذف با موفقیت انجام شد!\n'
            f'  - خبر: {deleted_news} رکورد\n'
            f'  - اطلاعیه: {deleted_announcements} رکورد'
        ))



