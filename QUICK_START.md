# راهنمای سریع استقرار ISPP

## مراحل سریع (5 دقیقه)

### 1. تنظیم فایل‌های Environment

```bash
# در root پروژه
cp .env.example .env
nano .env  # مقادیر را تنظیم کنید

# در پوشه backend
cd backend
cp .env.example .env
nano .env  # مقادیر را تنظیم کنید
cd ..
```

### 2. ساخت و اجرا

```bash
docker-compose up -d --build
```

### 3. ایجاد کاربر ادمین

```bash
docker-compose exec backend python manage.py createsuperuser
```

### 4. بررسی وضعیت

```bash
docker-compose ps
```

همه کانتینرها باید `Up (healthy)` باشند.

---

## دسترسی به پروژه

- **Frontend:** http://localhost
- **Backend API:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin

---

## دستورات مفید

```bash
# مشاهده لاگ‌ها
docker-compose logs -f

# Restart
docker-compose restart

# توقف
docker-compose down

# توقف کامل (با حذف volumes)
docker-compose down -v
```

---

## مشکلات رایج

### کانتینرها start نمی‌شوند
- بررسی کنید فایل‌های `.env` وجود دارند
- بررسی کنید پورت‌های 80 و 8000 آزاد هستند

### Backend به دیتابیس متصل نمی‌شود
- در `backend/.env` مطمئن شوید `DB_HOST=mysql` است
- بررسی کنید MySQL healthy است: `docker-compose ps mysql`

### Static files لود نمی‌شوند
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```

---

برای راهنمای کامل، به فایل `DEPLOY.md` مراجعه کنید.

