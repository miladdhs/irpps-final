#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clean up canonical board-member accounts, then upsert prepared events into the
current configured database.
"""
import os
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

from add_events import add_events
from add_board_members import BOARD_MEMBERS_DATA, create_username

User = get_user_model()

BOARD_MEMBER_USERNAMES = sorted({
    create_username(member["persian_name"])
    for members in BOARD_MEMBERS_DATA.values()
    for member in members
})


def prepare_board_members():
    print('\n' + '=' * 60)
    print('Preparing board-member accounts')
    print('=' * 60)

    users = User.objects.filter(username__in=BOARD_MEMBER_USERNAMES).order_by('username')
    updated = 0
    missing = 0

    for username in BOARD_MEMBER_USERNAMES:
        user = users.filter(username=username).first()
        if not user:
            missing += 1
            print(f'Missing board user: {username}')
            continue

        changed_fields = []
        if not user.is_active:
            user.is_active = True
            changed_fields.append('is_active')
        if not user.is_staff:
            user.is_staff = True
            changed_fields.append('is_staff')

        if changed_fields:
            user.save(update_fields=changed_fields)
            updated += 1
            print(f'Updated board user: {user.username}')

    print(f'Board users expected: {len(BOARD_MEMBER_USERNAMES)}')
    print(f'Board users found: {users.count()}')
    print(f'Board users updated: {updated}')
    print(f'Board users missing: {missing}')
    return True


if __name__ == '__main__':
    print('=' * 60)
    print('Preparing board users and importing prepared events')
    print('=' * 60)
    prepare_board_members()
    add_events()
