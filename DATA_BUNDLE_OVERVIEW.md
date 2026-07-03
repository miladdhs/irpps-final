# Data Bundle Overview

این فایل خلاصه می‌کند که بسته‌ی import فعلی پروژه چه داده‌هایی را وارد دیتابیس می‌کند.

## مسیر import اصلی

دستور اصلی:

```bash
docker compose exec -T backend python manage.py import_site_data_bundle
```

یا:

```bash
./restore_site_data.sh
```

## داده‌های موجود در بسته

### 1. اعضا و کاربران

منبع:

`backend/ispp_db.json`

محتوا:

- کاربران و اعضای ثبت‌شده
- ادمین اولیه
- بخشی از خبرها
- بخشی از اطلاعیه‌ها

تعداد فعلی داخل فایل:

- `accounts_customuser`: 78
- `news_news`: 1
- `news_announcement`: 1

### 2. اعضای هیئت‌مدیره

منبع:

`backend/add_board_members.py`

دوره‌های موجود:

- موسسین `1395`
- هیئت‌مدیره `1400`
- هیئت‌مدیره `1403`

عملکرد:

- اگر عضو وجود نداشته باشد ساخته می‌شود
- اگر وجود داشته باشد آپدیت می‌شود

### 3. اخبار، اطلاعیه‌ها و رویدادها

منبع:

`frontend/public/Content/structured_content_complete.json`

تعداد فعلی داخل فایل:

- `news`: 3
- `announcements`: 1
- `events`: 8

عملکرد:

- خبرها با `slug` وارد یا آپدیت می‌شوند
- اطلاعیه‌ها با `slug` وارد یا آپدیت می‌شوند
- رویدادها با `slug` وارد یا آپدیت می‌شوند

## فایل‌ها و اسکریپت‌های مرتبط

- `backend/accounts/management/commands/import_site_data_bundle.py`
- `backend/accounts/management/commands/import_ispp_json.py`
- `backend/news/management/commands/import_content_from_json.py`
- `restore_site_data.sh`

## نکته مهم

این بسته فقط داده‌هایی را برمی‌گرداند که داخل همین ریپو وجود دارند.  
اگر روی سرور داده‌های جدیدتری فقط داخل MySQL بوده و export نشده باشند، از این بسته برنمی‌گردند.
