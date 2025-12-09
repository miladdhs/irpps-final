# 📖 راهنمای اجرای کامندهای مدیریتی

این راهنما نحوه اجرای کامندهای مدیریتی برای بررسی دیتابیس و وارد کردن محتوا را توضیح می‌دهد.

---

## 🔍 کامند 1: بررسی و مشاهده دیتابیس (`inspect_database`)

### نحوه اجرا:

```bash
# رفتن به پوشه backend
cd backend

# نمایش همه اطلاعات (News, Announcements, Events, Users)
python manage.py inspect_database

# نمایش فقط اخبار
python manage.py inspect_database --model news

# نمایش فقط اطلاعیه‌ها
python manage.py inspect_database --model announcements

# نمایش فقط رویدادها
python manage.py inspect_database --model events

# نمایش فقط کاربران
python manage.py inspect_database --model users

# نمایش به صورت JSON
python manage.py inspect_database --format json

# نمایش فقط تعداد رکوردها
python manage.py inspect_database --format count

# محدود کردن تعداد رکوردها (مثلاً 10 تا)
python manage.py inspect_database --limit 10

# ترکیب گزینه‌ها
python manage.py inspect_database --model news --format json --limit 5
```

### مثال‌های عملی:

#### 1. بررسی تعداد کل رکوردها:
```bash
cd backend
python manage.py inspect_database --format count
```

**خروجی نمونه:**
```
=== Database Inspection Report ===

--- NEWS ---
Total News: 3

--- ANNOUNCEMENTS ---
Total Announcements: 1

--- EVENTS ---
Total Events: 8

--- USERS ---
Total Users: 5
```

#### 2. نمایش همه اخبار:
```bash
cd backend
python manage.py inspect_database --model news
```

**خروجی نمونه:**
```
Total News: 3

ID    Title                                               Category            Published  Views   
----------------------------------------------------------------------------------------------------
1     رئیس انجمن ریه کودکان هشدار داد...                بیماری‌های تنفسی   ✓         0       
2     افزایش چشمگیر بیماری‌های تنفسی در کودکان          بیماری‌های تنفسی   ✓         0       
3     تاریخچه انجمن علمی ریه کودکان ایران                تاریخچه            ✓         0       
```

#### 3. نمایش به صورت JSON:
```bash
cd backend
python manage.py inspect_database --model news --format json
```

**خروجی نمونه:**
```json
[
  {
    "id": 1,
    "title": "رئیس انجمن ریه کودکان هشدار داد: مصرف دخانیات در میان نوجوانان نگران‌کننده است",
    "slug": "hoshdar-masraf-dokhaniyat-noghavanan",
    "category": "بیماری‌های تنفسی",
    "source": "شفقنا",
    "is_published": true,
    "views": 0,
    "author": "admin",
    "created_at": "2025-01-15T10:00:00Z"
  }
]
```

---

## 📥 کامند 2: وارد کردن محتوا از JSON (`import_content_from_json`)

### نحوه اجرا:

```bash
# رفتن به پوشه backend
cd backend

# استفاده از مسیر پیش‌فرض (frontend/public/Content/structured_content_complete.json)
python manage.py import_content_from_json

# استفاده از مسیر دلخواه
python manage.py import_content_from_json --file "D:\Desktop\path\to\file.json"

# تعیین نویسنده (User ID)
python manage.py import_content_from_json --author-id 1

# بروزرسانی رکوردهای موجود
python manage.py import_content_from_json --update

# ترکیب گزینه‌ها
python manage.py import_content_from_json --author-id 1 --update
```

### مراحل کامل وارد کردن محتوا:

#### مرحله 1: بررسی کاربران موجود
```bash
cd backend
python manage.py inspect_database --model users
```

**خروجی نمونه:**
```
Total Users: 5

ID    Username            Email                          Staff    Active   
----------------------------------------------------------------------------------------------------
1     admin               admin@example.com              ✓        ✓       
2     user1               user1@example.com               ✗        ✓       
```

#### مرحله 2: وارد کردن محتوا
```bash
cd backend
python manage.py import_content_from_json --author-id 1
```

**خروجی نمونه:**
```
Loading data from: D:\Desktop\PRG\Cursor\ISPP\Final\OLD\frontend\public\Content\structured_content_complete.json
Using author: admin (ID: 1)

Importing 3 news items...
  + Created: رئیس انجمن ریه کودکان هشدار داد: مصرف دخانیات در میان نوجوانان نگران‌کننده است
  + Created: افزایش چشمگیر بیماری‌های تنفسی در کودکان
  + Created: تاریخچه انجمن علمی ریه کودکان ایران

Importing 1 announcements...
  + Created: کنگره بیماری‌های ریوی کودکان ۱۴۰۳

Import completed successfully!
  - News: 3 created, 0 updated
  - Announcements: 1 created, 0 updated
```

#### مرحله 3: بررسی نتیجه
```bash
cd backend
python manage.py inspect_database --model news
python manage.py inspect_database --model announcements
```

### بروزرسانی محتوا:

اگر فایل JSON را تغییر دادید و می‌خواهید رکوردهای موجود را بروزرسانی کنید:

```bash
cd backend
python manage.py import_content_from_json --author-id 1 --update
```

**خروجی نمونه:**
```
Loading data from: D:\Desktop\PRG\Cursor\ISPP\Final\OLD\frontend\public\Content\structured_content_complete.json
Using author: admin (ID: 1)

Importing 3 news items...
  ✓ Updated: رئیس انجمن ریه کودکان هشدار داد: مصرف دخانیات در میان نوجوانان نگران‌کننده است
  ⊗ Skipped (exists): افزایش چشمگیر بیماری‌های تنفسی در کودکان
  ✓ Updated: تاریخچه انجمن علمی ریه کودکان ایران

Import completed successfully!
  - News: 0 created, 2 updated
  - Announcements: 0 created, 1 updated
```

---

## 🖥️ اجرا در Windows (PowerShell)

### 1. باز کردن PowerShell:
- کلید `Win + X` را بزنید
- `Windows PowerShell` یا `Terminal` را انتخاب کنید

### 2. رفتن به پوشه پروژه:
```powershell
cd "D:\Desktop\PRG\Cursor\ISPP\Final\OLD\backend"
```

### 3. فعال کردن محیط مجازی (اگر دارید):
```powershell
.\venv\Scripts\Activate.ps1
```

### 4. اجرای کامند:
```powershell
# بررسی دیتابیس
python manage.py inspect_database

# وارد کردن محتوا
python manage.py import_content_from_json --author-id 1
```

---

## 🐧 اجرا در Linux/Mac (Terminal)

### 1. باز کردن Terminal

### 2. رفتن به پوشه پروژه:
```bash
cd /path/to/project/backend
```

### 3. فعال کردن محیط مجازی (اگر دارید):
```bash
source venv/bin/activate
```

### 4. اجرای کامند:
```bash
# بررسی دیتابیس
python3 manage.py inspect_database

# وارد کردن محتوا
python3 manage.py import_content_from_json --author-id 1
```

### ⚠️ نکته مهم برای سرور لینوکس:
- در سرور لینوکس معمولاً باید از `python3` استفاده کنید (نه `python`)
- اگر خطای "ModuleNotFoundError: No module named 'django'" می‌گیرید:
  ```bash
  # فعال کردن محیط مجازی
  source venv/bin/activate
  
  # یا نصب requirements
  pip install -r requirements.txt
  ```
  
  برای جزئیات بیشتر: `SERVER_COMMANDS.md`

---

## ⚠️ نکات مهم

### 1. مسیر فایل JSON:
- **پیش‌فرض**: `frontend/public/Content/structured_content_complete.json`
- اگر فایل در جای دیگری است، از `--file` استفاده کنید:
  ```bash
  python manage.py import_content_from_json --file "C:\path\to\file.json"
  ```

### 2. انتخاب نویسنده:
- اگر `--author-id` مشخص نشود، کامند به ترتیب از:
  1. اولین کاربر Staff
  2. اولین کاربر Superuser
  3. اولین کاربر موجود
  استفاده می‌کند.

### 3. بروزرسانی رکوردها:
- بدون `--update`: رکوردهای موجود نادیده گرفته می‌شوند
- با `--update`: رکوردهای موجود (بر اساس slug) بروزرسانی می‌شوند

### 4. پشتیبان‌گیری:
قبل از وارد کردن داده‌های جدید، از دیتابیس پشتیبان بگیرید:
```bash
cd backend
python manage.py dumpdata > backup.json
```

---

## 🐛 عیب‌یابی

### خطا: "No author found"
**راه حل:**
```bash
# ایجاد کاربر جدید
python manage.py createsuperuser

# یا استفاده از --author-id
python manage.py import_content_from_json --author-id 1
```

### خطا: "File not found"
**راه حل:**
```bash
# بررسی مسیر فایل
python manage.py import_content_from_json --file "D:\Desktop\path\to\file.json"
```

### خطا: "Invalid JSON file"
**راه حل:**
- فایل JSON را با یک JSON validator بررسی کنید
- اطمینان حاصل کنید که فایل UTF-8 است

### خطا: "Module not found"
**راه حل:**
```bash
# نصب requirements
pip install -r requirements.txt

# یا فعال کردن محیط مجازی
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # Linux/Mac
```

---

## 📋 چک‌لیست سریع

### قبل از وارد کردن محتوا:
- [ ] از دیتابیس پشتیبان گرفته‌اید
- [ ] فایل JSON را بررسی کرده‌اید
- [ ] کاربر مناسب (author) را شناسایی کرده‌اید
- [ ] migrations اجرا شده‌اند (`python manage.py migrate`)

### بعد از وارد کردن محتوا:
- [ ] بررسی تعداد رکوردها: `python manage.py inspect_database --format count`
- [ ] بررسی محتوا: `python manage.py inspect_database --model news`
- [ ] بررسی در پنل ادمین Django

---

## 🎯 مثال کامل (از ابتدا تا انتها)

```bash
# 1. رفتن به پوشه backend
cd backend

# 2. بررسی وضعیت فعلی
python manage.py inspect_database --format count

# 3. بررسی کاربران
python manage.py inspect_database --model users

# 4. وارد کردن محتوا
python manage.py import_content_from_json --author-id 1

# 5. بررسی نتیجه
python manage.py inspect_database --model news
python manage.py inspect_database --model announcements

# 6. نمایش جزئیات به صورت JSON
python manage.py inspect_database --model news --format json --limit 5
```

---

**تاریخ ایجاد**: 1403/10/18  
**نسخه**: 1.0

