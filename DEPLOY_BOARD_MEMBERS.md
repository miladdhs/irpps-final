# راهنمای اجرا روی سرور

## فایل‌های آماده شده برای آپلود

### 1. فایل‌های Backend
```
backend/add_board_members.py          # اسکریپت اضافه کردن داده‌ها
backend/run_add_board_members.sh      # اسکریپت اجرا
backend/accounts/views.py             # شامل API جدید
backend/accounts/urls.py              # شامل route جدید
```

### 2. فایل‌های Frontend
```
frontend/src/views/About.vue          # صفحه درباره ما (باید به‌روزرسانی شود)
```

## مراحل اجرا روی سرور

### گام 1: آپلود فایل‌ها
```bash
# آپلود فایل‌های backend
scp backend/add_board_members.py user@server:/path/to/backend/
scp backend/run_add_board_members.sh user@server:/path/to/backend/
scp backend/accounts/views.py user@server:/path/to/backend/accounts/
scp backend/accounts/urls.py user@server:/path/to/backend/accounts/

# یا استفاده از git
git add .
git commit -m "Add board members functionality"
git push
# سپس روی سرور:
git pull
```

### گام 2: اجرای اسکریپت روی سرور

#### روش 1: با Docker (اگر روی سرور Docker دارید)
```bash
cd /path/to/project
docker-compose exec backend python add_board_members.py
```

#### روش 2: بدون Docker (اجرای مستقیم)
```bash
cd /path/to/backend
source venv/bin/activate  # فعال‌سازی virtual environment
python add_board_members.py
```

#### روش 3: با manage.py
```bash
cd /path/to/backend
python manage.py shell < add_board_members.py
```

### گام 3: تست API
```bash
# تست از روی سرور
curl http://localhost:8000/api/accounts/board-members/

# تست از خارج سرور
curl http://your-domain.com/api/accounts/board-members/
```

### گام 4: Restart سرویس‌ها
```bash
# اگر از systemd استفاده می‌کنید
sudo systemctl restart gunicorn
sudo systemctl restart nginx

# اگر از Docker استفاده می‌کنید
docker-compose restart backend
docker-compose restart nginx
```

## خروجی مورد انتظار

بعد از اجرای اسکریپت باید خروجی مشابه زیر را ببینید:

```
شروع اضافه کردن اعضای هیئت مدیره...
================================================================================

================================================================================
دوره: founders_1395
================================================================================
✓ ایجاد شد: دکتر سهیلا خلیل زاده (رئیس انجمن)
✓ ایجاد شد: دکتر قمر تاج خانبابائی (نائب رئیس)
✓ ایجاد شد: دکتر محمد رضائی (دبیر انجمن)
...

================================================================================
خلاصه:
  - تعداد ایجاد شده: 27
  - تعداد به‌روزرسانی شده: 0
  - جمع کل: 27
================================================================================
```

## تست API Response

```bash
curl http://your-domain.com/api/accounts/board-members/ | jq
```

خروجی باید شبیه این باشد:
```json
{
  "success": true,
  "board_members": {
    "1395": [
      {
        "id": 1,
        "persian_name": "دکتر سهیلا خلیل زاده",
        "english_name": "Dr. Soheila Khalilzadeh",
        "display_name": "دکتر سهیلا خلیل زاده",
        "specialty": "فوق تخصص ریه کودکان",
        "bio": "رئیس انجمن - دوره 1395",
        "profile_image": ""
      }
    ]
  }
}
```

## عیب‌یابی

### خطا: Can't connect to MySQL
```bash
# بررسی وضعیت MySQL
sudo systemctl status mysql
# یا
docker-compose ps mysql

# بررسی تنظیمات دیتابیس در settings.py
cat backend/ispp_project/settings.py | grep DATABASES
```

### خطا: Module not found
```bash
# نصب مجدد requirements
pip install -r backend/requirements.txt
```

### خطا: Permission denied
```bash
# اضافه کردن مجوز اجرا
chmod +x backend/run_add_board_members.sh
```

## نکات امنیتی

1. اطمینان حاصل کنید که فایل `.env` شامل اطلاعات صحیح دیتابیس است
2. بعد از اجرا، لاگ‌ها را بررسی کنید
3. از backup دیتابیس قبل از اجرا اطمینان حاصل کنید

## Backup قبل از اجرا

```bash
# Backup دیتابیس
mysqldump -u username -p database_name > backup_before_board_members.sql

# یا با Docker
docker-compose exec mysql mysqldump -u root -p database_name > backup.sql
```

## بعد از اجرا

1. ✅ بررسی لاگ‌های Django
2. ✅ تست API endpoint
3. ✅ بررسی داده‌ها در دیتابیس
4. ✅ به‌روزرسانی Frontend
5. ✅ تست صفحه About در مرورگر
