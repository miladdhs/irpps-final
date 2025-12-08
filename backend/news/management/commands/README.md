# مدیریت کامندهای News App

این پوشه شامل کامندهای مدیریتی Django برای کار با مدل‌های News و Announcement است.

## 📁 ساختار فایل‌ها

```
backend/news/
├── management/
│   ├── __init__.py
│   └── commands/
│       ├── __init__.py
│       ├── inspect_database.py      # بررسی و پرینت دیتابیس
│       ├── import_content_from_json.py  # وارد کردن محتوا از JSON
│       └── README.md                # این فایل
```

---

## 🔍 کامند: `inspect_database`

این کامند برای بررسی و نمایش محتوای دیتابیس استفاده می‌شود.

### نحوه استفاده:

```bash
# نمایش همه مدل‌ها (News, Announcements, Events, Users)
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

# محدود کردن تعداد رکوردهای نمایش داده شده
python manage.py inspect_database --limit 10
```

### گزینه‌های کامند:

- `--model`: انتخاب مدل برای بررسی
  - گزینه‌ها: `news`, `announcements`, `events`, `users`, `all` (پیش‌فرض: `all`)
  
- `--format`: فرمت خروجی
  - گزینه‌ها: `table` (پیش‌فرض), `json`, `count`
  
- `--limit`: محدود کردن تعداد رکوردهای نمایش داده شده

### مثال‌های استفاده:

```bash
# نمایش همه اخبار به صورت جدول
python manage.py inspect_database --model news

# نمایش 5 اطلاعیه آخر به صورت JSON
python manage.py inspect_database --model announcements --format json --limit 5

# نمایش تعداد کل رکوردها
python manage.py inspect_database --format count
```

---

## 📥 کامند: `import_content_from_json`

این کامند برای وارد کردن محتوا از فایل `structured_content_complete.json` به دیتابیس استفاده می‌شود.

### نحوه استفاده:

```bash
# استفاده از مسیر پیش‌فرض (frontend/public/Content/structured_content_complete.json)
python manage.py import_content_from_json

# استفاده از مسیر دلخواه
python manage.py import_content_from_json --file path/to/your/file.json

# تعیین نویسنده (User ID)
python manage.py import_content_from_json --author-id 1

# بروزرسانی رکوردهای موجود (بر اساس slug)
python manage.py import_content_from_json --update
```

### گزینه‌های کامند:

- `--file`: مسیر فایل JSON (پیش‌فرض: `frontend/public/Content/structured_content_complete.json`)
- `--author-id`: شناسه کاربر برای استفاده به عنوان نویسنده
  - اگر مشخص نشود، از اولین کاربر staff استفاده می‌شود
  - اگر کاربر staff وجود نداشته باشد، از اولین superuser استفاده می‌شود
  - اگر هیچ کدام وجود نداشته باشد، از اولین کاربر استفاده می‌شود
- `--update`: بروزرسانی رکوردهای موجود (اگر slug تکراری باشد)

### ساختار فایل JSON مورد انتظار:

```json
{
  "news": [
    {
      "title": "عنوان خبر",
      "slug": "slug-news",
      "content": "محتوا...",
      "short_content": "خلاصه...",
      "category": "دسته‌بندی",
      "tags": "تگ1, تگ2",
      "source": "منبع",
      "is_published": true,
      "views": 0,
      "image": null,
      "author": null,
      "created_at": "2025-01-15T10:00:00Z",
      "updated_at": "2025-01-15T10:00:00Z"
    }
  ],
  "announcements": [
    {
      "title": "عنوان اطلاعیه",
      "slug": "slug-announcement",
      "content": "محتوا...",
      "is_published": true,
      "is_important": false,
      "views": 0,
      "image": null,
      "author": null,
      "created_at": "2025-01-15T10:00:00Z",
      "updated_at": "2025-01-15T10:00:00Z"
    }
  ]
}
```

### نکات مهم:

1. **فیلد `author`**: در JSON می‌تواند `null` باشد. کامند به صورت خودکار یک نویسنده پیدا می‌کند.

2. **فیلد `slug`**: باید یکتا باشد. اگر رکوردی با همان slug وجود داشته باشد:
   - بدون `--update`: رکورد نادیده گرفته می‌شود
   - با `--update`: رکورد موجود بروزرسانی می‌شود

3. **فیلدهای تاریخ**: اگر در JSON موجود باشند، استفاده می‌شوند. در غیر این صورت، تاریخ فعلی استفاده می‌شود.

4. **تصاویر**: اگر مسیر تصویر در JSON موجود باشد، باید مسیر نسبی از `media/` باشد.

### مثال‌های استفاده:

```bash
# وارد کردن با مسیر پیش‌فرض
python manage.py import_content_from_json

# وارد کردن با نویسنده مشخص
python manage.py import_content_from_json --author-id 1

# بروزرسانی رکوردهای موجود
python manage.py import_content_from_json --update --author-id 1

# استفاده از فایل دلخواه
python manage.py import_content_from_json --file /path/to/custom.json --author-id 1
```

---

## 🚀 نحوه اجرا

### پیش‌نیازها:

1. اطمینان حاصل کنید که در محیط مجازی Django هستید
2. اطمینان حاصل کنید که migrations اجرا شده‌اند:
   ```bash
   python manage.py migrate
   ```

### اجرای کامندها:

1. به پوشه `backend` بروید:
   ```bash
   cd backend
   ```

2. کامند را اجرا کنید:
   ```bash
   python manage.py inspect_database
   python manage.py import_content_from_json
   ```

### در محیط Windows:

```powershell
# فعال کردن محیط مجازی (اگر دارید)
.\venv\Scripts\Activate.ps1

# رفتن به پوشه backend
cd backend

# اجرای کامند
python manage.py inspect_database
python manage.py import_content_from_json
```

### در محیط Linux/Mac:

```bash
# فعال کردن محیط مجازی (اگر دارید)
source venv/bin/activate

# رفتن به پوشه backend
cd backend

# اجرای کامند
python manage.py inspect_database
python manage.py import_content_from_json
```

---

## 📝 مثال کامل کاربرد

### سناریو 1: بررسی وضعیت دیتابیس

```bash
# بررسی تعداد کل رکوردها
python manage.py inspect_database --format count

# نمایش همه اخبار
python manage.py inspect_database --model news

# نمایش 10 اطلاعیه آخر
python manage.py inspect_database --model announcements --limit 10
```

### سناریو 2: وارد کردن محتوا از JSON

```bash
# مرحله 1: بررسی کاربران موجود
python manage.py inspect_database --model users

# مرحله 2: وارد کردن محتوا با نویسنده مشخص
python manage.py import_content_from_json --author-id 1

# مرحله 3: بررسی نتیجه
python manage.py inspect_database --model news
python manage.py inspect_database --model announcements
```

### سناریو 3: بروزرسانی محتوا

```bash
# بروزرسانی فایل JSON
# ... (ویرایش فایل structured_content_complete.json)

# وارد کردن مجدد با گزینه --update
python manage.py import_content_from_json --update --author-id 1
```

---

## ⚠️ نکات امنیتی

1. **پشتیبان‌گیری**: قبل از وارد کردن داده‌های جدید، از دیتابیس پشتیبان بگیرید:
   ```bash
   python manage.py dumpdata > backup.json
   ```

2. **تست**: ابتدا در محیط توسعه تست کنید، سپس در محیط production اجرا کنید.

3. **اعتبارسنجی**: قبل از وارد کردن، فایل JSON را بررسی کنید تا از صحت ساختار آن اطمینان حاصل کنید.

---

## 🐛 عیب‌یابی

### خطا: "No author found"

**راه حل**: ابتدا یک کاربر ایجاد کنید:
```bash
python manage.py createsuperuser
```

یا از گزینه `--author-id` استفاده کنید:
```bash
python manage.py import_content_from_json --author-id 1
```

### خطا: "File not found"

**راه حل**: مسیر فایل را به درستی مشخص کنید:
```bash
python manage.py import_content_from_json --file "D:\Desktop\path\to\file.json"
```

### خطا: "Invalid JSON file"

**راه حل**: فایل JSON را با یک JSON validator بررسی کنید.

---

## 📚 منابع بیشتر

- [Django Management Commands Documentation](https://docs.djangoproject.com/en/stable/howto/custom-management-commands/)
- [استراکچر خبر و اطلاعیه](./../../../../استراکچر_خبر_و_اطلاعیه.md)

---

**تاریخ ایجاد**: 1403/10/18  
**نسخه**: 1.0

