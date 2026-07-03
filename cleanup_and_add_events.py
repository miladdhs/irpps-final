#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hide board members from the public members list and upsert prepared events.
"""
import os
import sys
import django
from pathlib import Path

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
from add_events import add_events

User = get_user_model()

BOARD_MEMBER_USERNAMES = [
    'board_سهیلا_خلیل_زاده',
    'board_قمر_تاج_خان_بابائی',
    'board_محمد_رضائی',
    'board_مجید_کیوانفر',
    'board_سید_احمد_طباطبائی',
    'board_محسن_علی_سمیر',
    'board_حسینعلی_غفاری_پور',
    'board_محمد_رضا_مدرسی',
    'board_سید_جواد_سیدی',
    'board_روح_الله_شیرزادی',
    'board_علیرضا_اسدی',
    'board_امیر_رضائی',
    'board_علیرضا_عشقی',
    'board_سید_محمد_رضا_میرکریمی',
    'board_بابک_قالیباف',
    'board_سید_حسین_میر_لوحی',
    'board_لعنت_شاهکار',
    'board_نازنین_فرحبخش',
    'board_ذلفا_مدرسی',
    'board_معصومه_قاسمپور_علمداری',
]


def hide_board_members():
    print('\n' + '=' * 60)
    print('خارج کردن اعضای هیئت مدیره از لیست عمومی اعضا')
    print('=' * 60)

    updated = 0
    for username in BOARD_MEMBER_USERNAMES:
        user = User.objects.filter(username=username).first()
        if not user:
            print(f'⚠️  کاربر پیدا نشد: {username}')
            continue

        user.is_active = False
        user.save(update_fields=['is_active'])
        updated += 1
        print(f'✅ غیرفعال شد: {username}')

    print(f'✅ {updated} عضو از لیست عمومی خارج شد')
    return True


if __name__ == '__main__':
    print('=' * 60)
    print('پاکسازی اعضا و به‌روزرسانی رویدادها')
    print('=' * 60)
    hide_board_members()
    add_events()
