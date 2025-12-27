# ✅ چک‌لیست نهایی قبل از استقرار روی سرور

## 📋 قبل از اجرا

### 1. فایل‌های Environment
- [ ] فایل `.env` در root پروژه ایجاد شده و تنظیم شده
- [ ] فایل `backend/.env` ایجاد شده و تنظیم شده
- [ ] `SECRET_KEY` در `backend/.env` تولید و تنظیم شده
- [ ] `DB_PASSWORD` و `MYSQL_ROOT_PASSWORD` در هر دو فایل یکسان هستند
- [ ] `ALLOWED_HOSTS` شامل دامنه/IP سرور است
- [ ] `DEBUG=False` در هر دو فایل تنظیم شده

### 2. بررسی فایل‌های Docker
- [ ] `docker-compose.yaml` موجود است
- [ ] `backend/Dockerfile` موجود است
- [ ] `frontend/Dockerfile` موجود است
- [ ] `backend/docker-entrypoint.sh` موجود است و executable است

### 3. بررسی فایل‌های پروژه
- [ ] `backend/requirements.txt` موجود است
- [ ] `frontend/package.json` موجود است
- [ ] `frontend/nginx.conf` موجود است

---

## 🚀 مراحل اجرا

### مرحله 1: آپلود به سرور
```bash
# آپلود کل پروژه به سرور (مثلاً با scp یا git)
scp -r . user@server:/path/to/project
```

### مرحله 2: تنظیم فایل‌های Environment
```bash
# روی سرور
cd /path/to/project

# ایجاد فایل .env در root
nano .env
# (محتوا را از ENV_SETUP.md کپی کنید)

# ایجاد فایل .env در backend
cd backend
nano .env
# (محتوا را از ENV_SETUP.md کپی کنید)
cd ..
```

### مرحله 3: اجرای پروژه
```bash
# ساخت و اجرای کانتینرها
docker-compose up -d --build

# بررسی وضعیت
docker-compose ps

# مشاهده لاگ‌ها
docker-compose logs -f
```

### مرحله 4: ایجاد کاربر ادمین
```bash
docker-compose exec backend python manage.py createsuperuser
```

---

## ✅ بررسی بعد از اجرا

### 1. بررسی Health Checks
```bash
docker-compose ps
```
همه کانتینرها باید `Up (healthy)` باشند.

### 2. تست دسترسی
- [ ] Frontend: `http://your-server-ip` یا `http://your-domain`
- [ ] Backend API: `http://your-server-ip:8000` یا `http://api.your-domain:8000`
- [ ] Admin Panel: `http://your-server-ip:8000/admin`

### 3. بررسی لاگ‌ها
```bash
# لاگ همه سرویس‌ها
docker-compose logs

# لاگ backend
docker-compose logs backend

# لاگ frontend
docker-compose logs frontend

# لاگ database
docker-compose logs mysql
```

---

## 🔧 دستورات مفید

### مدیریت کانتینرها
```bash
# توقف
docker-compose stop

# شروع مجدد
docker-compose start

# Restart
docker-compose restart

# توقف و حذف
docker-compose down

# توقف کامل با حذف volumes (⚠️ دیتا پاک می‌شود)
docker-compose down -v
```

### دسترسی به کانتینرها
```bash
# دسترسی به backend
docker-compose exec backend bash

# دسترسی به frontend
docker-compose exec frontend sh

# دسترسی به database
docker-compose exec mysql mysql -u root -p
```

### مدیریت Database
```bash
# اجرای migrations
docker-compose exec backend python manage.py migrate

# ایجاد migrations جدید
docker-compose exec backend python manage.py makemigrations

# Collect static files
docker-compose exec backend python manage.py collectstatic --noinput
```

---

## ⚠️ مشکلات رایج و راه حل

### مشکل: کانتینر backend crash می‌کند
**راه حل:**
1. بررسی لاگ: `docker-compose logs backend`
2. بررسی فایل `backend/.env` - مطمئن شوید `DB_HOST=mysql` است
3. بررسی اتصال به database

### مشکل: خطای `ALLOWED_HOSTS`
**راه حل:**
1. IP یا دامنه سرور را به `ALLOWED_HOSTS` در `backend/.env` اضافه کنید
2. `docker-compose restart backend`

### مشکل: خطای database connection
**راه حل:**
1. بررسی کنید که `DB_HOST=mysql` در `backend/.env` باشد
2. بررسی کنید که پسوردها در هر دو فایل `.env` یکسان باشند
3. بررسی کنید که کانتینر mysql در حال اجرا است: `docker-compose ps`

### مشکل: Frontend به backend متصل نمی‌شود
**راه حل:**
1. بررسی `frontend/nginx-api.conf` - مطمئن شوید که proxy_pass به `http://backend:8000` است
2. بررسی network: `docker network inspect irpps_app-network`

---

## 📝 نکات مهم

1. **هرگز** فایل‌های `.env` را در Git commit نکنید
2. از پسوردهای قوی استفاده کنید
3. در production، `DEBUG` باید `False` باشد
4. به صورت منظم backup از database بگیرید
5. لاگ‌ها را به صورت منظم بررسی کنید

---

## 🎉 موفقیت!

اگر همه چیز درست کار می‌کند:
- ✅ همه کانتینرها `Up (healthy)` هستند
- ✅ Frontend در دسترس است
- ✅ Backend API پاسخ می‌دهد
- ✅ Admin panel کار می‌کند
- ✅ Database متصل است

**پروژه شما آماده استفاده است! 🚀**

