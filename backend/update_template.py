#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script برای به‌روزرسانی خودکار templates/index.html از dist/index.html
این script باید بعد از npm run build اجرا شود.
"""

import os
import re
import sys
from pathlib import Path

# تنظیم encoding برای خروجی در Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent
DIST_HTML = BASE_DIR.parent / 'frontend' / 'dist' / 'index.html'
TEMPLATE_HTML = BASE_DIR / 'templates' / 'index.html'


def update_template():
    """به‌روزرسانی templates/index.html از dist/index.html"""
    
    if not DIST_HTML.exists():
        print(f"[ERROR] فایل {DIST_HTML} پیدا نشد!")
        print("لطفاً ابتدا npm run build را اجرا کنید.")
        return False
    
    # خواندن dist/index.html
    with open(DIST_HTML, 'r', encoding='utf-8') as f:
        dist_content = f.read()
    
    # تبدیل مسیرهای static به Django template tags
    # تبدیل src="/assets/..." به src="{% static 'assets/...' %}"
    def replace_asset_path(match):
        path = match.group(1)
        # حذف / از ابتدای مسیر
        if path.startswith('/'):
            path = path[1:]
        return 'src="{% static \'' + path + '\' %}"'
    
    def replace_asset_href(match):
        path = match.group(1)
        # حذف / از ابتدای مسیر
        if path.startswith('/'):
            path = path[1:]
        return 'href="{% static \'' + path + '\' %}"'
    
    dist_content = re.sub(r'src="(/assets/[^"]+)"', replace_asset_path, dist_content)
    dist_content = re.sub(r'href="(/assets/[^"]+)"', replace_asset_href, dist_content)
    
    # تبدیل src="/bootstrap.bundle.min.js" به src="{% static 'bootstrap.bundle.min.js' %}"
    dist_content = re.sub(
        r'src="(/bootstrap\.bundle\.min\.js)"',
        lambda m: 'src="{% static \'bootstrap.bundle.min.js\' %}"',
        dist_content
    )
    
    # افزودن {% load static %} در ابتدای <head> (اگر وجود نداشته باشد)
    if '{% load static %}' not in dist_content:
        dist_content = dist_content.replace('<head>', '<head>\n\t{% load static %}')
    
    # حفظ محتوای SSR (اگر در template موجود باشد)
    # این بخش محتوای Django template tags را حفظ می‌کند
    # اگر می‌خواهید محتوای SSR حفظ شود، باید قبل از build آن را در template نگه دارید
    
    # اطمینان از وجود پوشه templates
    TEMPLATE_HTML.parent.mkdir(exist_ok=True)
    
    # نوشتن به templates/index.html
    with open(TEMPLATE_HTML, 'w', encoding='utf-8') as f:
        f.write(dist_content)
    
    print(f"[SUCCESS] {TEMPLATE_HTML} با موفقیت به‌روز شد!")
    return True


if __name__ == '__main__':
    update_template()

