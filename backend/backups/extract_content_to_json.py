#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
اسکریپت استخراج و پردازش محتوای فایل‌های Content
هر فایل به عنوان یک محتوای جداگانه پردازش می‌شود
"""

import json
import re
import os
from datetime import datetime
from pathlib import Path
import unicodedata
import html

# مسیر پوشه Content
CONTENT_DIR = Path("frontend/public/Content")
OUTPUT_FILE = "content_extracted.json"

def persian_to_slug(text):
    """تبدیل متن فارسی به اسلاگ URL-friendly"""
    if not text:
        return ""
    
    # تبدیل اعداد فارسی به انگلیسی
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    for i, p in enumerate(persian_digits):
        text = text.replace(p, english_digits[i])
    
    # جدول تبدیل حروف فارسی به لاتین
    persian_to_latin = {
        'آ': 'a', 'ا': 'a', 'ب': 'b', 'پ': 'p', 'ت': 't', 'ث': 's',
        'ج': 'j', 'چ': 'ch', 'ح': 'h', 'خ': 'kh', 'د': 'd', 'ذ': 'z',
        'ر': 'r', 'ز': 'z', 'ژ': 'zh', 'س': 's', 'ش': 'sh', 'ص': 's',
        'ض': 'z', 'ط': 't', 'ظ': 'z', 'ع': 'a', 'غ': 'gh', 'ف': 'f',
        'ق': 'gh', 'ک': 'k', 'گ': 'g', 'ل': 'l', 'م': 'm', 'ن': 'n',
        'و': 'v', 'ه': 'h', 'ی': 'y', 'ئ': 'y', 'ي': 'y',
        ' ': '-', '_': '-', '.': '', ',': '', '،': '', '؛': '', ':': '',
        '؟': '', '!': '', '(': '', ')': '', '[': '', ']': '', '{': '', '}': '',
        '/': '-', '\\': '-', '|': '-', '"': '', "'": '', '«': '', '»': '',
    }
    
    result = []
    for char in text:
        if char in persian_to_latin:
            result.append(persian_to_latin[char])
        elif char.isalnum():
            result.append(char.lower())
        elif char in ['-', '_']:
            result.append('-')
    
    # تبدیل به رشته و پاکسازی
    slug = ''.join(result)
    slug = re.sub(r'[^a-z0-9-]', '', slug.lower())
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    
    # اگر خالی شد، یک اسلاگ پیش‌فرض بساز
    if not slug:
        slug = 'item-' + str(abs(hash(text)) % 10000)
    
    return slug

def extract_short_content(content, max_length=500):
    """استخراج خلاصه از محتوا"""
    if not content:
        return None
    
    # حذف HTML tags و لینک‌ها
    content = re.sub(r'<[^>]+>', '', content)
    content = re.sub(r'https?://[^\s]+', '', content)
    content = re.sub(r'\s+', ' ', content)
    content = content.strip()
    
    # حذف خطوط خالی و فاصله‌های اضافی
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    content = ' '.join(lines)
    
    if len(content) <= max_length:
        return content
    
    # پیدا کردن نقطه پایان مناسب
    truncated = content[:max_length]
    last_period = truncated.rfind('.')
    last_space = truncated.rfind(' ')
    
    if last_period > max_length * 0.7:
        return truncated[:last_period + 1]
    elif last_space > max_length * 0.7:
        return truncated[:last_space] + '...'
    else:
        return truncated + '...'

def extract_title_from_filename(filename):
    """استخراج عنوان از نام فایل"""
    # حذف پسوند
    name = Path(filename).stem
    # حذف اعداد و تاریخ‌ها
    name = re.sub(r'\d{4}-\d{2}-\d{2}', '', name)
    name = re.sub(r'\(\d+\)', '', name)
    name = re.sub(r'^\d+', '', name)
    name = name.strip(' -_')
    
    # اگر نام فایل فارسی است، برگردان
    if any('\u0600' <= char <= '\u06FF' for char in name):
        return name.replace('_', ' ').replace('-', ' ')
    
    return None

def process_html_file(file_path):
    """پردازش فایل HTML"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # استخراج عنوان
        title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "تاریخچه انجمن علمی ریه کودکان ایران"
        
        # استخراج محتوای فارسی
        persian_section = re.search(r'<div class="card persian">(.*?)</div>', html_content, re.DOTALL)
        if persian_section:
            content = persian_section.group(1)
            # حذف HTML tags
            content = re.sub(r'<[^>]+>', '', content)
            content = html.unescape(content)
            content = re.sub(r'\s+', ' ', content).strip()
            
            # تعیین نوع محتوا
            if "تاریخچه" in title or "history" in title.lower():
                return {
                    "type": "news",
                    "title": title,
                    "slug": persian_to_slug(title),
                    "content": content,
                    "short_content": extract_short_content(content),
                    "category": "تاریخچه",
                    "tags": "تاریخچه,انجمن,ریه کودکان",
                    "source": "انجمن علمی ریه کودکان ایران",
                    "image": None
                }
    except Exception as e:
        print(f"⚠️  خطا در پردازش HTML {file_path.name}: {e}")
    
    return None

def process_pdf_file(file_path):
    """پردازش فایل PDF - استخراج نام و ایجاد محتوا"""
    filename = file_path.name
    
    # استخراج عنوان از نام فایل
    title = extract_title_from_filename(filename)
    if not title:
        # اگر نام فایل عددی است، از نام فایل استفاده کن
        title = filename.replace('.pdf', '').replace('_', ' ')
    
    # تعیین نوع محتوا بر اساس نام فایل
    content_type = "news"
    category = "عمومی"
    tags = "سند,PDF"
    
    if "سمینار" in filename or "همایش" in filename or "کنگره" in filename:
        content_type = "event"
        category = "همایش"
        tags = "همایش,سمینار,کنگره"
    elif "تاریخچه" in filename or "history" in filename.lower():
        category = "تاریخچه"
        tags = "تاریخچه,سند"
    
    # ایجاد محتوای توصیفی
    content = f"این فایل PDF با نام '{filename}' در پوشه محتوا قرار دارد. برای مشاهده محتوای کامل، لطفاً فایل PDF را دانلود کنید."
    
    return {
        "type": content_type,
        "title": title,
        "slug": persian_to_slug(title),
        "content": content,
        "short_content": extract_short_content(content),
        "category": category,
        "tags": tags,
        "source": "انجمن علمی ریه کودکان ایران",
        "file_path": f"Content/{filename}",
        "image": None
    }

def process_docx_file(file_path):
    """پردازش فایل Word"""
    filename = file_path.name
    
    # استخراج عنوان از نام فایل
    title = extract_title_from_filename(filename)
    if not title:
        title = filename.replace('.docx', '').replace('_', ' ')
    
    # تعیین نوع محتوا
    content_type = "news"
    category = "عمومی"
    tags = "سند,Word"
    
    if "اطلاعات" in filename or "404" in filename:
        category = "اطلاعات"
        tags = "اطلاعات,سند"
    
    # ایجاد محتوای توصیفی
    content = f"این فایل Word با نام '{filename}' در پوشه محتوا قرار دارد. برای مشاهده محتوای کامل، لطفاً فایل Word را دانلود کنید."
    
    return {
        "type": content_type,
        "title": title,
        "slug": persian_to_slug(title),
        "content": content,
        "short_content": extract_short_content(content),
        "category": category,
        "tags": tags,
        "source": "انجمن علمی ریه کودکان ایران",
        "file_path": f"Content/{filename}",
        "image": None
    }

def create_news_from_image(file_path):
    """ایجاد خبر از تصویر"""
    filename = file_path.name
    file_stem = Path(filename).stem
    
    # تعیین نوع و دسته‌بندی بر اساس نام فایل
    category = "عمومی"
    tags = "تصویر,گالری"
    content_type = "news"
    
    if "photo_2025" in filename or "photo-2025" in filename:
        category = "همایش"
        tags = "همایش,تصویر,گالری,رویداد"
        # استخراج تاریخ و زمان کامل از نام فایل
        date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-(\d{2})', filename)
        if date_match:
            year, month, day, hour, minute, second = date_match.groups()
            # استفاده از زمان کامل برای منحصر به فرد کردن
            title = f"تصویر همایش سالیانه ریه کودکان - {year}/{month}/{day} ساعت {hour}:{minute}:{second}"
        else:
            # استخراج شماره از نام فایل
            number_match = re.search(r'(\d{2})$', file_stem)
            if number_match:
                img_num = number_match.group(1)
                title = f"تصویر همایش سالیانه ریه کودکان - شماره {img_num}"
            else:
                # استفاده از بخش آخر نام فایل
                file_parts = file_stem.split('_')
                if len(file_parts) > 1:
                    img_id = file_parts[-1]
                    title = f"تصویر همایش سالیانه ریه کودکان - {img_id}"
                else:
                    title = f"تصویر همایش سالیانه ریه کودکان - {file_stem}"
        
        content = f"این تصویر از مجموعه تصاویر همایش سالیانه انجمن علمی ریه کودکان ایران است. تصویر مربوط به رویدادهای علمی و تخصصی برگزار شده در زمینه بیماری‌های ریوی کودکان می‌باشد."
        
    elif "img_2025" in filename or "img-2025" in filename:
        category = "خبر"
        tags = "خبر,تصویر"
        date_match = re.search(r'(\d{4})(\d{2})(\d{2})', filename)
        if date_match:
            year, month, day = date_match.groups()
            title = f"تصویر خبر - {year}/{month}/{day}"
        else:
            title = "تصویر خبر"
        
        content = f"این تصویر مربوط به اخبار و رویدادهای انجمن علمی ریه کودکان ایران است."
        
    elif "image" in filename.lower():
        category = "عمومی"
        tags = "تصویر,گالری"
        title = "تصویر گالری انجمن"
        content = f"این تصویر از گالری تصاویر انجمن علمی ریه کودکان ایران است."
        
    else:
        # استخراج عنوان از نام فایل
        title = file_stem.replace('_', ' ').replace('-', ' ')
        # حذف اعداد و تاریخ
        title = re.sub(r'\d{4}[-_]?\d{2}[-_]?\d{2}', '', title)
        title = re.sub(r'\(\d+\)', '', title)
        title = title.strip()
        
        if not title or len(title) < 3:
            title = f"تصویر {file_stem}"
        
        content = f"این تصویر با نام '{filename}' در گالری تصاویر انجمن علمی ریه کودکان ایران قرار دارد."
    
    # ایجاد محتوای کامل
    full_content = f"{content}\n\nاین تصویر بخشی از آرشیو تصاویر انجمن علمی ریه کودکان ایران می‌باشد و مربوط به فعالیت‌ها و رویدادهای علمی این انجمن است."
    
    slug = persian_to_slug(title)
    if not slug or len(slug) < 5:
        slug = persian_to_slug(file_stem) or f"image-{abs(hash(filename)) % 10000}"
    
    return {
        "type": "news",
        "title": title,
        "slug": slug,
        "content": full_content,
        "short_content": extract_short_content(full_content),
        "category": category,
        "tags": tags,
        "source": "انجمن علمی ریه کودکان ایران",
        "image": f"Content/{filename}",
        "is_published": True,
        "author": 1,
        "views": 0,
        "file_path": None
    }

def process_other_txt():
    """پردازش فایل other.txt - تفکیک به چند محتوا"""
    news_items = []
    
    try:
        with open(CONTENT_DIR / "other.txt", "r", encoding="utf-8") as f:
            content = f.read()
        
        # تقسیم بر اساس شماره‌گذاری
        sections = re.split(r'\d+\.\s*لینک', content)
        
        for i, section in enumerate(sections[1:], 1):
            lines = section.strip().split('\n')
            if not lines:
                continue
            
            # استخراج عنوان
            title = None
            date = None
            source = None
            content_text = []
            
            for line in lines:
                line = line.strip()
                if line.startswith('عنوان:'):
                    title = line.replace('عنوان:', '').strip()
                elif line.startswith('تاریخ انتشار:'):
                    date_str = line.replace('تاریخ انتشار:', '').strip()
                    date = date_str
                elif line.startswith('محتوای کامل'):
                    continue
                elif line and not line.startswith('http'):
                    content_text.append(line)
            
            if title and content_text:
                full_content = '\n\n'.join(content_text)
                # حذف لینک‌ها از محتوا
                full_content = re.sub(r'https?://[^\s]+', '', full_content)
                full_content = re.sub(r'\s+', ' ', full_content).strip()
                
                slug = persian_to_slug(title)
                if not slug or len(slug) < 5:
                    slug = f"khabar-{i}"
                
                # تعیین دسته‌بندی بر اساس محتوا
                category = "بیماری‌های تنفسی"
                tags = "ریه کودکان,بیماری‌های تنفسی"
                
                if "دخانیات" in full_content or "قلیان" in full_content:
                    tags += ",دخانیات,هشدار"
                if "آلودگی" in full_content:
                    tags += ",آلودگی هوا"
                if "کنگره" in full_content or "همایش" in full_content:
                    category = "همایش"
                    tags += ",همایش,کنگره"
                
                news_item = {
                    "type": "news",
                    "title": title,
                    "slug": slug,
                    "content": full_content,
                    "short_content": extract_short_content(full_content),
                    "category": category,
                    "tags": tags,
                    "source": "شفقنا / مهرنیوز / وبدا",
                    "image": None
                }
                news_items.append(news_item)
        
        # استخراج برنامه همایش از other.txt
        agenda_match = re.search(r'پنجمین همایش سالیانه.*?پایان همایش', content, re.DOTALL)
        if agenda_match:
            agenda_text = agenda_match.group(0)
            agenda_text = re.sub(r'https?://[^\s]+', '', agenda_text)
            agenda_text = re.sub(r'\s+', ' ', agenda_text).strip()
            
            # استخراج لیست سخنرانان
            speakers_list = []
            speaker_pattern = r'دکتر\s+[^\n]+'
            speakers = re.findall(speaker_pattern, agenda_text)
            unique_speakers = list(set(speakers))[:20]
            speakers_text = '، '.join(unique_speakers[:10]) if unique_speakers else "دکتر قمرتاج خانبابایی و سایر اساتید"
            
            title = "پنجمین همایش سالیانه انجمن علمی ریه کودکان ایران"
            slug = persian_to_slug(title)
            
            event = {
                "type": "event",
                "title": title,
                "slug": slug,
                "description": agenda_text,
                "short_description": "پنجمین همایش سالیانه انجمن علمی ریه کودکان ایران در تاریخ ۳۱ خرداد و ۱ تیر ۱۴۰۳ در بیمارستان کودکان مفید تهران برگزار می‌شود.",
                "event_type": "seminar",
                "location": "تهران - خیابان شریعتی، نرسیده به میرداماد، بیمارستان کودکان مفید",
                "event_month": 3,
                "event_year": 1403,
                "agenda": agenda_text,
                "organizer": "انجمن علمی ریه کودکان ایران",
                "target_audience": "فوق‌تخصصان ریه، متخصصان کودکان و پزشکان عمومی",
                "speakers": speakers_text,
                "contact_info": "تلفن واحد مجری: ۰۲۱-۸۸۸۷۴۸۸۵ | کد شناسه: ۲۱۲۳۶۴",
                "file_path": None,
                "cover_image": None
            }
            news_items.append(event)
    
    except Exception as e:
        print(f"⚠️  خطا در پردازش other.txt: {e}")
    
    return news_items

def validate_and_clean_data(data_list, data_type):
    """اعتبارسنجی و پاکسازی داده‌ها"""
    cleaned = []
    seen_slugs = set()
    
    for item in data_list:
        # بررسی وجود فیلدهای اجباری
        content_field = item.get("content") or item.get("description")
        if not item.get("title") or not item.get("slug") or not content_field:
            print(f"⚠️  هشدار: {data_type} با عنوان '{item.get('title', 'بدون عنوان')}' فیلدهای اجباری ندارد و حذف شد.")
            continue
        
        # بررسی یکتایی اسلاگ
        slug = item["slug"]
        if slug in seen_slugs:
            counter = 1
            while f"{slug}-{counter}" in seen_slugs:
                counter += 1
            slug = f"{slug}-{counter}"
            item["slug"] = slug
        seen_slugs.add(slug)
        
        # پاکسازی محتوا
        if item.get("content"):
            item["content"] = re.sub(r'\s+', ' ', item["content"]).strip()
        if item.get("description"):
            item["description"] = re.sub(r'\s+', ' ', item["description"]).strip()
        
        # محدود کردن طول عنوان
        if len(item["title"]) > 200:
            item["title"] = item["title"][:197] + "..."
        
        cleaned.append(item)
    
    return cleaned

def main():
    """تابع اصلی - پردازش همه فایل‌ها"""
    print("شروع استخراج و پردازش محتوا...")
    print("=" * 60)
    
    result = {
        "news": [],
        "announcements": [],
        "events": [],
        "metadata": {
            "extracted_at": datetime.now().isoformat(),
            "total_news": 0,
            "total_announcements": 0,
            "total_events": 0,
            "version": "3.0"
        }
    }
    
    # لیست همه فایل‌ها
    all_files = list(CONTENT_DIR.iterdir())
    
    print(f"📁 تعداد کل فایل‌ها: {len(all_files)}")
    print()
    
    # پردازش هر فایل
    for file_path in all_files:
        if file_path.is_file():
            filename = file_path.name.lower()
            
            # پردازش فایل HTML
            if filename.endswith('.html'):
                print(f"📄 پردازش HTML: {file_path.name}")
                item = process_html_file(file_path)
                if item:
                    if item["type"] == "news":
                        result["news"].append(item)
                    elif item["type"] == "event":
                        result["events"].append(item)
                print(f"   ✓ پردازش شد")
            
            # پردازش فایل PDF
            elif filename.endswith('.pdf'):
                print(f"📄 پردازش PDF: {file_path.name}")
                item = process_pdf_file(file_path)
                if item:
                    if item["type"] == "news":
                        result["news"].append(item)
                    elif item["type"] == "event":
                        result["events"].append(item)
                print(f"   ✓ پردازش شد")
            
            # پردازش فایل Word
            elif filename.endswith('.docx'):
                print(f"📄 پردازش Word: {file_path.name}")
                item = process_docx_file(file_path)
                if item:
                    if item["type"] == "news":
                        result["news"].append(item)
                print(f"   ✓ پردازش شد")
            
            # پردازش فایل تصویر - تبدیل به خبر
            elif filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                print(f"🖼️  پردازش تصویر و تبدیل به خبر: {file_path.name}")
                news_item = create_news_from_image(file_path)
                result["news"].append(news_item)
                print(f"   ✓ تبدیل به خبر شد: {news_item['title']}")
            
            # پردازش فایل other.txt (چند محتوا)
            elif filename == 'other.txt':
                print(f"📄 پردازش other.txt (چند محتوا):")
                items = process_other_txt()
                for item in items:
                    if item["type"] == "news":
                        result["news"].append(item)
                    elif item["type"] == "event":
                        result["events"].append(item)
                print(f"   ✓ {len(items)} محتوا استخراج شد")
    
    # اعتبارسنجی و پاکسازی
    print("\n🔍 اعتبارسنجی و پاکسازی داده‌ها...")
    result["news"] = validate_and_clean_data(result["news"], "خبر")
    result["events"] = validate_and_clean_data(result["events"], "رویداد")
    
    # اضافه کردن فیلدهای اجباری
    for item in result["news"]:
        item["is_published"] = True
        item["author"] = 1
        item["views"] = 0
        if "file_path" not in item:
            item["file_path"] = None
    
    for item in result["events"]:
        item["is_published"] = True
        item["is_featured"] = True
        item["created_by"] = 1
        item["price"] = 0
        item["views"] = 0
        if "cover_image" not in item:
            item["cover_image"] = None
    
    # مرتبط کردن تصاویر رویداد با رویدادها (برای cover_image)
    print("\n🔗 مرتبط کردن تصاویر با رویدادها...")
    event_news = [n for n in result["news"] if n.get("category") == "همایش" and n.get("image")]
    
    if result["events"] and event_news:
        # استفاده از اولین تصویر همایش به عنوان کاور
        result["events"][0]["cover_image"] = event_news[0]["image"]
        print(f"   ✓ تصویر کاور به رویداد اضافه شد")
    
    # ایجاد اطلاعیه‌ها
    print("\n📢 ایجاد اطلاعیه‌ها...")
    announcements = [
        {
            "title": "برگزاری کنگره بیماری‌های ریوی کودکان ۱۴۰۳",
            "slug": "bargozari-kongreh-bimarihaye-riuye-kudakan-1403",
            "content": "به اطلاع می‌رساند کنگره بیماری‌های ریوی کودکان ۱۴۰۳ در تاریخ ۳۱ خرداد لغایت ۲ تیر ماه ۱۴۰۳ در بیمارستان کودکان مفید تهران برگزار می‌گردد.",
            "is_published": True,
            "is_important": True,
            "author": 1,
            "image": None,
            "views": 0
        },
        {
            "title": "هشدار: مصرف دخانیات در میان نوجوانان نگران‌کننده است",
            "slug": "hoshdar-masraf-dokhaniyat-dar-mian-nojavanan",
            "content": "رئیس انجمن ریه کودکان هشدار داد: مصرف دخانیات در میان نوجوانان نگران‌کننده است.",
            "is_published": True,
            "is_important": True,
            "author": 1,
            "image": None,
            "views": 0
        }
    ]
    result["announcements"] = validate_and_clean_data(announcements, "اطلاعیه")
    
    # به‌روزرسانی آمار
    result["metadata"]["total_news"] = len(result["news"])
    result["metadata"]["total_announcements"] = len(result["announcements"])
    result["metadata"]["total_events"] = len(result["events"])
    
    # ذخیره فایل JSON
    print(f"\n💾 در حال ذخیره فایل JSON...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print("=" * 60)
    print(f"✅ استخراج با موفقیت انجام شد!")
    print(f"\n📊 آمار نهایی:")
    print(f"   📰 اخبار: {result['metadata']['total_news']}")
    print(f"   📢 اطلاعیه‌ها: {result['metadata']['total_announcements']}")
    print(f"   📅 رویدادها: {result['metadata']['total_events']}")
    print(f"\n📁 فایل خروجی: {OUTPUT_FILE}")
    print("=" * 60)

if __name__ == "__main__":
    main()
