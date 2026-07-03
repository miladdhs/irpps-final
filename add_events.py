#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upsert prepared events into the current configured database and attach cover images.
Usage: python add_events.py
"""
import os
import shutil
import sys
from pathlib import Path

import django

if sys.platform == 'win32':
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

BASE_DIR = Path(__file__).parent
BACKEND_DIR = BASE_DIR / 'backend'
sys.path.insert(0, str(BACKEND_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ispp_project.settings')
django.setup()

from django.contrib.auth import get_user_model

from events.models import Event

User = get_user_model()

EVENT_DEFINITIONS = [
    {
        'title': 'وبینار روز جهانی آسم ۲۰۲۵',
        'slug': 'webinar-world-asthma-day-2025',
        'description': 'وبینار روز جهانی آسم ۲۰۲۵ با تمرکز بر آخرین یافته‌ها و روش‌های درمانی در زمینه آسم کودکان.',
        'short_description': 'وبینار روز جهانی آسم ۲۰۲۵',
        'event_type': 'webinar',
        'location': 'آنلاین',
        'event_month': 2,
        'event_year': 1404,
        'cover_image_path': 'asthma.jpg',
    },
    {
        'title': 'وبینار روز جهانی پنومونی',
        'slug': 'webinar-world-pneumonia-day',
        'description': 'وبینار روز جهانی پنومونی با محور پیشگیری، تشخیص زودهنگام و درمان پنومونی در کودکان.',
        'short_description': 'وبینار روز جهانی پنومونی',
        'event_type': 'webinar',
        'location': 'آنلاین',
        'event_month': 8,
        'event_year': 1403,
        'cover_image_path': 'penomoni.jpg',
    },
    {
        'title': 'اولین کنگره سراسری بیماری‌های تنفسی کودکان',
        'slug': 'first-national-congress-pediatric-respiratory',
        'description': 'اولین کنگره سراسری بیماری‌های تنفسی کودکان با حضور متخصصان برجسته کشور.',
        'short_description': 'اولین کنگره سراسری بیماری‌های تنفسی کودکان',
        'event_type': 'congress',
        'location': 'تهران',
        'event_month': 6,
        'event_year': 1396,
        'cover_image_path': 'avalin kongere.jpg',
    },
    {
        'title': 'چهارمین همایش سالیانه انجمن علمی ریه کودکان ایران (وبینار چهار روزه)',
        'slug': 'fourth-annual-conference-ispp',
        'description': 'چهارمین همایش سالیانه انجمن علمی ریه کودکان ایران به صورت وبینار چهار روزه برگزار شد.',
        'short_description': 'چهارمین همایش سالیانه انجمن علمی ریه کودکان ایران',
        'event_type': 'conference',
        'location': 'آنلاین',
        'event_month': 7,
        'event_year': 1399,
        'cover_image_path': 'chaharomin hamayesh.jpg',
    },
    {
        'title': 'ششمین سمینار سالانه بیماری‌های تنفسی کودکان',
        'slug': 'sixth-annual-seminar-pediatric-respiratory',
        'description': 'ششمین سمینار سالانه بیماری‌های تنفسی کودکان با موضوع تازه‌ترین پیشرفت‌های تشخیصی و درمانی.',
        'short_description': 'ششمین سمینار سالانه بیماری‌های تنفسی کودکان',
        'event_type': 'seminar',
        'location': 'تهران',
        'event_month': 9,
        'event_year': 1401,
        'cover_image_path': 'seshomin seminar.jpg',
    },
    {
        'title': 'سومین کنگره سراسری بیماری‌های تنفسی کودکان',
        'slug': 'third-national-congress-pediatric-respiratory',
        'description': 'سومین کنگره سراسری بیماری‌های تنفسی کودکان با تمرکز بر چالش‌ها و راهکارهای درمانی نوین.',
        'short_description': 'سومین کنگره سراسری بیماری‌های تنفسی کودکان',
        'event_type': 'congress',
        'location': 'تهران',
        'event_month': 5,
        'event_year': 1400,
        'cover_image_path': 'sevomin kongere.jpg',
    },
]


def resolve_cover_image(relative_name: str | None) -> str | None:
    if not relative_name:
        return None

    source = BASE_DIR / 'frontend' / 'public' / 'Content' / relative_name
    if not source.exists():
        print(f'Warning: event image not found: {source}')
        return None

    target_dir = BASE_DIR / 'backend' / 'media' / 'events' / 'covers'
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / relative_name
    shutil.copy2(source, target)
    print(f'Copied event image: {relative_name}')
    return f'events/covers/{relative_name}'


def add_events():
    staff_user = User.objects.filter(is_staff=True).order_by('id').first()
    if not staff_user:
        print('Error: no staff user found. Create an admin/staff user first.')
        return False

    created_count = 0
    updated_count = 0

    for item in EVENT_DEFINITIONS:
        event_data = dict(item)
        cover_image_path = event_data.pop('cover_image_path', None)
        cover_image = resolve_cover_image(cover_image_path)

        defaults = {
            **event_data,
            'is_published': True,
            'is_featured': False,
            'created_by': staff_user,
        }
        if cover_image:
            defaults['cover_image'] = cover_image

        event = Event.objects.filter(slug=event_data['slug']).first()
        if event:
            for key, value in defaults.items():
                setattr(event, key, value)
            event.save()
            updated_count += 1
            print(f'Updated event: {event.title}')
            continue

        Event.objects.create(**defaults)
        created_count += 1
        print(f'Created event: {event_data["title"]}')

    print('\n' + '=' * 60)
    print(f'Created events: {created_count}')
    print(f'Updated events: {updated_count}')
    print('=' * 60)
    return (created_count + updated_count) > 0


if __name__ == '__main__':
    print('=' * 60)
    print('Importing prepared events into current database')
    print('=' * 60)
    try:
        add_events()
    except Exception as exc:
        print(f'Fatal error: {exc}')
        raise
