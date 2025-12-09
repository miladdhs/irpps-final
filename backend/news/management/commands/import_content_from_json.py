"""
Management command to import content from structured_content_complete.json
Usage: python manage.py import_content_from_json --file path/to/file.json [--author-id AUTHOR_ID]
"""
import json
import os
import sys
from pathlib import Path
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone
from django.conf import settings

from news.models import News, Announcement

# Fix encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

User = get_user_model()


class Command(BaseCommand):
    help = 'Import News and Announcements from structured_content_complete.json file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default=None,
            help='Path to structured_content_complete.json file (default: frontend/public/Content/structured_content_complete.json)'
        )
        parser.add_argument(
            '--author-id',
            type=int,
            default=None,
            help='User ID to use as author for all imported content (if not provided, will try to use first staff user)'
        )
        parser.add_argument(
            '--update',
            action='store_true',
            help='Update existing records if they exist (based on slug)'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        author_id = options['author_id']
        update_existing = options['update']

        # Determine file path
        if not file_path:
            # Try multiple possible paths
            base_dir = Path(settings.BASE_DIR)
            possible_paths = [
                # Docker container path (mounted volume)
                base_dir.parent / 'frontend' / 'public' / 'Content' / 'structured_content_complete.json',
                # Local development path
                base_dir.parent.parent / 'frontend' / 'public' / 'Content' / 'structured_content_complete.json',
                # Absolute path in container
                Path('/app') / '..' / 'frontend' / 'public' / 'Content' / 'structured_content_complete.json',
                # Alternative container path
                Path('/opt/irpps/src/frontend/public/Content/structured_content_complete.json'),
            ]
            
            file_path = None
            for path in possible_paths:
                if path.exists():
                    file_path = path
                    break
            
            if not file_path:
                # Default to first path and let it fail with proper error
                file_path = base_dir.parent / 'frontend' / 'public' / 'Content' / 'structured_content_complete.json'
        else:
            file_path = Path(file_path)

        if not file_path.exists():
            self.stderr.write(self.style.ERROR(
                f'❌ File not found: {file_path}\n\n'
                '💡 راه حل:\n'
                '1. استفاده از مسیر کامل:\n'
                '   python3 manage.py import_content_from_json --file /opt/irpps/src/frontend/public/Content/structured_content_complete.json --author-id 1\n\n'
                '2. یا کپی فایل به داخل container:\n'
                '   docker cp /opt/irpps/src/frontend/public/Content/structured_content_complete.json irpps-backend-1:/app/\n'
                '   سپس: python3 manage.py import_content_from_json --file /app/structured_content_complete.json --author-id 1\n\n'
                '3. یا mount کردن volume در docker-compose.yaml'
            ))
            return

        self.stdout.write(self.style.SUCCESS(f'Loading data from: {file_path}'))

        # Load JSON file
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            self.stderr.write(self.style.ERROR(f'Invalid JSON file: {e}'))
            return
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error reading file: {e}'))
            return

        # Get or create author
        author = self.get_author(author_id)
        if not author:
            self.stderr.write(self.style.ERROR('No author found. Please create a user first or use --author-id'))
            return

        self.stdout.write(self.style.SUCCESS(f'Using author: {author.username} (ID: {author.id})'))

        # Import data
        with transaction.atomic():
            news_count = self.import_news(data.get('news', []), author, update_existing)
            announcements_count = self.import_announcements(data.get('announcements', []), author, update_existing)

        self.stdout.write(self.style.SUCCESS(
            f'\nImport completed successfully!\n'
            f'  - News: {news_count["created"]} created, {news_count["updated"]} updated\n'
            f'  - Announcements: {announcements_count["created"]} created, {announcements_count["updated"]} updated'
        ))

    def get_author(self, author_id):
        """Get author user by ID or use first staff user"""
        if author_id:
            try:
                return User.objects.get(id=author_id)
            except User.DoesNotExist:
                self.stderr.write(self.style.WARNING(f'User with ID {author_id} not found. Trying to find staff user...'))
        
        # Try to get first staff user
        staff_user = User.objects.filter(is_staff=True).first()
        if staff_user:
            return staff_user
        
        # Try to get first superuser
        superuser = User.objects.filter(is_superuser=True).first()
        if superuser:
            return superuser
        
        # Try to get any user
        any_user = User.objects.first()
        return any_user

    def import_news(self, news_list, author, update_existing):
        """Import news items"""
        created_count = 0
        updated_count = 0

        if not news_list:
            self.stdout.write(self.style.WARNING('No news items found in JSON file'))
            return {'created': 0, 'updated': 0}

        self.stdout.write(self.style.NOTICE(f'\nImporting {len(news_list)} news items...'))

        for news_data in news_list:
            slug = news_data.get('slug', '').strip()
            
            # اگر slug خالی است، از title یک slug بساز
            if not slug:
                title = news_data.get('title', '')
                if title:
                    # تبدیل title به slug (ساده)
                    import re
                    slug = re.sub(r'[^\w\s-]', '', title)
                    slug = re.sub(r'[-\s]+', '-', slug)
                    slug = slug.lower().strip('-')
                else:
                    self.stderr.write(self.style.WARNING(f'Skipping news item without title and slug'))
                    continue
            
            # اطمینان از اینکه slug خالی نیست
            if not slug:
                self.stderr.write(self.style.WARNING(f'Skipping news item with empty slug: {news_data.get("title", "Unknown")}'))
                continue

            # Prepare defaults
            defaults = {
                'title': news_data.get('title', ''),
                'slug': slug,  # اضافه کردن slug
                'content': news_data.get('content', ''),
                'short_content': news_data.get('short_content') or '',
                'category': news_data.get('category') or '',
                'tags': news_data.get('tags') or '',
                'source': news_data.get('source') or '',
                'is_published': news_data.get('is_published', True),
                'views': news_data.get('views', 0),
                'author': author,
            }

            # Handle image (if provided as path)
            image = news_data.get('image')
            if image and image not in (None, '', 'null'):
                defaults['image'] = image

            # Handle dates
            if news_data.get('created_at'):
                try:
                    defaults['created_at'] = timezone.datetime.fromisoformat(
                        news_data['created_at'].replace('Z', '+00:00')
                    )
                except:
                    pass

            # Check if exists
            existing = News.objects.filter(slug=slug).first()
            
            if existing and update_existing:
                # Update existing
                for key, value in defaults.items():
                    setattr(existing, key, value)
                existing.save()
                updated_count += 1
                self.stdout.write(f'  ✓ Updated: {news_data.get("title", slug)}')
            elif existing:
                # Skip existing
                self.stdout.write(f'  ⊗ Skipped (exists): {news_data.get("title", slug)}')
            else:
                # Create new
                News.objects.create(**defaults)
                created_count += 1
                self.stdout.write(f'  + Created: {news_data.get("title", slug)}')

        return {'created': created_count, 'updated': updated_count}

    def import_announcements(self, announcements_list, author, update_existing):
        """Import announcement items"""
        created_count = 0
        updated_count = 0

        if not announcements_list:
            self.stdout.write(self.style.WARNING('No announcements found in JSON file'))
            return {'created': 0, 'updated': 0}

        self.stdout.write(self.style.NOTICE(f'\nImporting {len(announcements_list)} announcements...'))

        for ann_data in announcements_list:
            slug = ann_data.get('slug', '').strip()
            
            # اگر slug خالی است، از title یک slug بساز
            if not slug:
                title = ann_data.get('title', '')
                if title:
                    # تبدیل title به slug (ساده)
                    import re
                    slug = re.sub(r'[^\w\s-]', '', title)
                    slug = re.sub(r'[-\s]+', '-', slug)
                    slug = slug.lower().strip('-')
                else:
                    self.stderr.write(self.style.WARNING(f'Skipping announcement without title and slug'))
                    continue
            
            # اطمینان از اینکه slug خالی نیست
            if not slug:
                self.stderr.write(self.style.WARNING(f'Skipping announcement with empty slug: {ann_data.get("title", "Unknown")}'))
                continue

            # Prepare defaults
            defaults = {
                'title': ann_data.get('title', ''),
                'slug': slug,  # اضافه کردن slug
                'content': ann_data.get('content', ''),
                'is_published': ann_data.get('is_published', True),
                'is_important': ann_data.get('is_important', False),
                'views': ann_data.get('views', 0),
                'author': author,
            }

            # Handle image (if provided as path)
            image = ann_data.get('image')
            if image and image not in (None, '', 'null'):
                defaults['image'] = image

            # Handle dates
            if ann_data.get('created_at'):
                try:
                    defaults['created_at'] = timezone.datetime.fromisoformat(
                        ann_data['created_at'].replace('Z', '+00:00')
                    )
                except:
                    pass

            # Check if exists
            existing = Announcement.objects.filter(slug=slug).first()
            
            if existing and update_existing:
                # Update existing
                for key, value in defaults.items():
                    setattr(existing, key, value)
                existing.save()
                updated_count += 1
                self.stdout.write(f'  ✓ Updated: {ann_data.get("title", slug)}')
            elif existing:
                # Skip existing
                self.stdout.write(f'  ⊗ Skipped (exists): {ann_data.get("title", slug)}')
            else:
                # Create new
                Announcement.objects.create(**defaults)
                created_count += 1
                self.stdout.write(f'  + Created: {ann_data.get("title", slug)}')

        return {'created': created_count, 'updated': updated_count}

