# راهنمای راه‌اندازی Docker

## مشکل فعلی
Docker Desktop در حال اجرا نیست و نمی‌توان به دیتابیس MySQL متصل شد.

## راه‌حل

### گام 1: راه‌اندازی Docker Desktop
1. Docker Desktop را باز کنید
2. منتظر بمانید تا Docker به طور کامل راه‌اندازی شود (آیکون Docker در system tray باید سبز باشد)

### گام 2: راه‌اندازی سرویس‌ها
```bash
# در پوشه اصلی پروژه
docker-compose up -d
```

این دستور سرویس‌های زیر را راه‌اندازی می‌کند:
- MySQL (دیتابیس)
- Backend (Django)
- Frontend (Vue.js)
- Nginx (وب سرور)

### گام 3: بررسی وضعیت سرویس‌ها
```bash
docker-compose ps
```

باید خروجی مشابه زیر را ببینید:
```
NAME                IMAGE               STATUS
backend             ...                 Up
frontend            ...                 Up
mysql               ...                 Up
nginx               ...                 Up
```

### گام 4: اضافه کردن داده‌های هیئت مدیره
```bash
cd backend
bash run_add_board_members.sh
```

یا:
```bash
docker-compose exec backend python add_board_members.py
```

### گام 5: تست API
```bash
# تست endpoint اعضا
curl http://localhost/api/accounts/members/

# تست endpoint هیئت مدیره
curl http://localhost/api/accounts/board-members/
```

### گام 6: باز کردن وب‌سایت
مرورگر خود را باز کنید و به آدرس زیر بروید:
```
http://localhost
```

## عیب‌یابی

### اگر Docker Desktop نصب نیست:
1. از [سایت رسمی Docker](https://www.docker.com/products/docker-desktop) دانلود کنید
2. نصب کنید و سیستم را restart کنید

### اگر خطای "port already in use" دریافت کردید:
```bash
# بررسی پورت‌های در حال استفاده
netstat -ano | findstr :80
netstat -ano | findstr :3306
netstat -ano | findstr :8000

# متوقف کردن سرویس‌ها
docker-compose down

# راه‌اندازی مجدد
docker-compose up -d
```

### اگر خطای دیتابیس دریافت کردید:
```bash
# پاک کردن volumes و راه‌اندازی مجدد
docker-compose down -v
docker-compose up -d

# اجرای migrations
docker-compose exec backend python manage.py migrate

# ایجاد superuser
docker-compose exec backend python manage.py createsuperuser
```

## دستورات مفید

```bash
# مشاهده لاگ‌ها
docker-compose logs -f

# مشاهده لاگ یک سرویس خاص
docker-compose logs -f backend

# متوقف کردن سرویس‌ها
docker-compose down

# متوقف کردن و پاک کردن volumes
docker-compose down -v

# rebuild کردن سرویس‌ها
docker-compose up -d --build

# اجرای دستور در کانتینر backend
docker-compose exec backend python manage.py <command>

# ورود به shell کانتینر
docker-compose exec backend bash
```
