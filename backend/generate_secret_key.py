#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
اسکریپت برای تولید SECRET_KEY امن برای Django
"""

import os
import sys

# Add Django to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from django.core.management.utils import get_random_secret_key
    secret_key = get_random_secret_key()
    print("\n" + "="*60)
    print("SECRET_KEY تولید شده:")
    print("="*60)
    print(secret_key)
    print("="*60)
    print("\nاین کلید را در فایل .env خود کپی کنید.")
    print("="*60 + "\n")
except ImportError:
    # Fallback if Django is not installed
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(alphabet) for i in range(50))
    print("\n" + "="*60)
    print("SECRET_KEY تولید شده (بدون Django):")
    print("="*60)
    print(secret_key)
    print("="*60)
    print("\nاین کلید را در فایل .env خود کپی کنید.")
    print("="*60 + "\n")

