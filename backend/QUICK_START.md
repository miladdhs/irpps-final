# ⚡ راهنمای سریع اجرای کامندها

## 🔍 بررسی دیتابیس

```bash
cd backend

# نمایش همه اطلاعات
python manage.py inspect_database

# نمایش فقط اخبار
python manage.py inspect_database --model news

# نمایش به صورت JSON
python manage.py inspect_database --format json
```

## 📥 وارد کردن محتوا

```bash
cd backend

# وارد کردن با نویسنده مشخص
python manage.py import_content_from_json --author-id 1

# بروزرسانی رکوردهای موجود
python manage.py import_content_from_json --author-id 1 --update
```

## 📋 چک‌لیست سریع

```bash
# 1. بررسی وضعیت
python manage.py inspect_database --format count

# 2. وارد کردن محتوا
python manage.py import_content_from_json --author-id 1

# 3. بررسی نتیجه
python manage.py inspect_database --model news
```

---

**برای جزئیات بیشتر**: `COMMANDS_GUIDE.md`

