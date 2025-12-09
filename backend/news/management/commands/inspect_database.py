"""
Management command to inspect and print database content
Usage: python manage.py inspect_database [--model MODEL_NAME] [--format FORMAT]
"""
import sys
import json
import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from news.models import News, Announcement
from events.models import Event

# Fix encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

User = get_user_model()


class Command(BaseCommand):
    help = 'Inspect and print database content (News, Announcements, Events, Users)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--model',
            type=str,
            choices=['news', 'announcements', 'events', 'users', 'all'],
            default='all',
            help='Model to inspect (default: all)'
        )
        parser.add_argument(
            '--format',
            type=str,
            choices=['table', 'json', 'count'],
            default='table',
            help='Output format (default: table)'
        )
        parser.add_argument(
            '--limit',
            type=int,
            default=None,
            help='Limit number of records to display'
        )

    def handle(self, *args, **options):
        # Check database connection first
        try:
            from django.db import connection
            connection.ensure_connection()
        except Exception as e:
            self.stderr.write(self.style.ERROR(
                f'❌ خطا در اتصال به دیتابیس: {str(e)}\n\n'
                '💡 راه حل:\n'
                '1. اگر MySQL در Docker است، از داخل container اجرا کنید:\n'
                '   docker exec -it irpps-backend-1 python3 manage.py inspect_database\n\n'
                '2. یا IP Docker container را پیدا کنید:\n'
                '   docker inspect irpps-mysql-1 | grep IPAddress\n'
                '   سپس: export DB_HOST=<IP_ADDRESS>\n\n'
                '3. یا از docker-compose exec استفاده کنید:\n'
                '   docker-compose exec backend python3 manage.py inspect_database'
            ))
            return
        
        model_name = options['model']
        output_format = options['format']
        limit = options['limit']

        if model_name == 'all':
            self.inspect_all(output_format, limit)
        elif model_name == 'news':
            self.inspect_news(output_format, limit)
        elif model_name == 'announcements':
            self.inspect_announcements(output_format, limit)
        elif model_name == 'events':
            self.inspect_events(output_format, limit)
        elif model_name == 'users':
            self.inspect_users(output_format, limit)

    def inspect_all(self, output_format, limit):
        """Inspect all models"""
        self.stdout.write(self.style.SUCCESS('\n=== Database Inspection Report ===\n'))
        
        self.stdout.write(self.style.WARNING('--- NEWS ---'))
        self.inspect_news(output_format, limit)
        
        self.stdout.write(self.style.WARNING('\n--- ANNOUNCEMENTS ---'))
        self.inspect_announcements(output_format, limit)
        
        self.stdout.write(self.style.WARNING('\n--- EVENTS ---'))
        self.inspect_events(output_format, limit)
        
        self.stdout.write(self.style.WARNING('\n--- USERS ---'))
        self.inspect_users(output_format, limit)

    def inspect_news(self, output_format, limit):
        """Inspect News model"""
        queryset = News.objects.all().order_by('-created_at')
        if limit:
            queryset = queryset[:limit]
        
        count = News.objects.count()
        self.stdout.write(self.style.NOTICE(f'Total News: {count}'))
        
        if output_format == 'count':
            return
        
        if output_format == 'json':
            data = []
            for news in queryset:
                data.append({
                    'id': news.id,
                    'title': news.title,
                    'slug': news.slug,
                    'category': news.category,
                    'source': news.source,
                    'is_published': news.is_published,
                    'views': news.views,
                    'author': news.author.username if news.author else None,
                    'created_at': news.created_at.isoformat() if news.created_at else None,
                })
            self.stdout.write(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            # Table format
            self.stdout.write(f'\n{"ID":<5} {"Title":<50} {"Category":<20} {"Published":<10} {"Views":<8}')
            self.stdout.write('-' * 100)
            for news in queryset:
                title = news.title[:47] + '...' if len(news.title) > 50 else news.title
                published = '✓' if news.is_published else '✗'
                self.stdout.write(
                    f'{news.id:<5} {title:<50} {news.category or "N/A":<20} {published:<10} {news.views:<8}'
                )

    def inspect_announcements(self, output_format, limit):
        """Inspect Announcement model"""
        queryset = Announcement.objects.all().order_by('-created_at')
        if limit:
            queryset = queryset[:limit]
        
        count = Announcement.objects.count()
        self.stdout.write(self.style.NOTICE(f'Total Announcements: {count}'))
        
        if output_format == 'count':
            return
        
        if output_format == 'json':
            data = []
            for ann in queryset:
                data.append({
                    'id': ann.id,
                    'title': ann.title,
                    'slug': ann.slug,
                    'is_published': ann.is_published,
                    'is_important': ann.is_important,
                    'views': ann.views,
                    'author': ann.author.username if ann.author else None,
                    'created_at': ann.created_at.isoformat() if ann.created_at else None,
                })
            self.stdout.write(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            # Table format
            self.stdout.write(f'\n{"ID":<5} {"Title":<50} {"Important":<10} {"Published":<10} {"Views":<8}')
            self.stdout.write('-' * 100)
            for ann in queryset:
                title = ann.title[:47] + '...' if len(ann.title) > 50 else ann.title
                published = '✓' if ann.is_published else '✗'
                important = '✓' if ann.is_important else '✗'
                self.stdout.write(
                    f'{ann.id:<5} {title:<50} {important:<10} {published:<10} {ann.views:<8}'
                )

    def inspect_events(self, output_format, limit):
        """Inspect Event model"""
        queryset = Event.objects.all().order_by('-event_year', '-event_month')
        if limit:
            queryset = queryset[:limit]
        
        count = Event.objects.count()
        self.stdout.write(self.style.NOTICE(f'Total Events: {count}'))
        
        if output_format == 'count':
            return
        
        if output_format == 'json':
            data = []
            for event in queryset:
                data.append({
                    'id': event.id,
                    'title': event.title,
                    'slug': event.slug,
                    'event_type': event.event_type,
                    'location': event.location,
                    'event_year': event.event_year,
                    'event_month': event.event_month,
                    'organizer': getattr(event, 'organizer', '') or '',
                    'is_published': event.is_published,
                    'is_featured': getattr(event, 'is_featured', False),
                })
            self.stdout.write(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            # Table format
            self.stdout.write(f'\n{"ID":<5} {"Title":<50} {"Type":<15} {"Year":<6} {"Location":<20}')
            self.stdout.write('-' * 100)
            for event in queryset:
                title = event.title[:47] + '...' if len(event.title) > 50 else event.title
                location = event.location[:18] + '...' if event.location and len(event.location) > 20 else (event.location or 'N/A')
                self.stdout.write(
                    f'{event.id:<5} {title:<50} {event.event_type:<15} {event.event_year or "N/A":<6} {location:<20}'
                )

    def inspect_users(self, output_format, limit):
        """Inspect User model"""
        queryset = User.objects.all().order_by('-date_joined')
        if limit:
            queryset = queryset[:limit]
        
        count = User.objects.count()
        self.stdout.write(self.style.NOTICE(f'Total Users: {count}'))
        
        if output_format == 'count':
            return
        
        if output_format == 'json':
            data = []
            for user in queryset:
                data.append({
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'is_staff': user.is_staff,
                    'is_superuser': user.is_superuser,
                    'is_active': user.is_active,
                    'date_joined': user.date_joined.isoformat() if user.date_joined else None,
                })
            self.stdout.write(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            # Table format
            self.stdout.write(f'\n{"ID":<5} {"Username":<20} {"Email":<30} {"Staff":<8} {"Active":<8}')
            self.stdout.write('-' * 100)
            for user in queryset:
                email = user.email[:28] + '...' if user.email and len(user.email) > 30 else (user.email or 'N/A')
                staff = '✓' if user.is_staff else '✗'
                active = '✓' if user.is_active else '✗'
                self.stdout.write(
                    f'{user.id:<5} {user.username:<20} {email:<30} {staff:<8} {active:<8}'
                )

