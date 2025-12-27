# راهنمای کامل استقرار پروژه ISPP با Docker

این راهنما شامل تمام مراحل لازم برای استقرار پروژه روی سرور با Docker Compose است.

## 📋 فهرست مطالب

- [پیش‌نیازها](#پیش‌نیازها)
- [مراحل استقرار](#مراحل-استقرار)
- [تنظیمات اولیه](#تنظیمات-اولیه)
- [اجرای پروژه](#اجرای-پروژه)
- [مدیریت و نگهداری](#مدیریت-و-نگهداری)
- [عیب‌یابی](#عیب‌یابی)
- [به‌روزرسانی پروژه](#به‌روزرسانی-پروژه)

---

## پیش‌نیازها

### نرم‌افزارهای مورد نیاز

1. **Docker** (نسخه 20.10 یا بالاتر)
2. **Docker Compose** (نسخه 2.0 یا بالاتر)
3. **Git** (برای دریافت کد)

### بررسی نصب Docker

```bash
docker --version
docker-compose --version
```

اگر Docker نصب نیست، از [راهنمای نصب Docker](https://docs.docker.com/get-docker/) استفاده کنید.

---

## مراحل استقرار

### 1. دریافت کد پروژه

```bash
# کلون کردن پروژه (یا آپلود فایل‌ها به سرور)
git clone <repository-url>
cd ISPP-Final-OLD
```

### 2. تنظیم فایل‌های Environment

#### الف) ایجاد فایل `.env` در root پروژه

```bash
cp .env.example .env
nano .env  # یا از ویرایشگر مورد علاقه خود استفاده کنید
```

محتویات `.env`:

```env
DB_NAME=irporg_DB
DB_USER=irporg_admin
DB_PASSWORD=your-strong-password-here
MYSQL_ROOT_PASSWORD=your-strong-root-password-here
MYSQL_PORT=3306
```

#### ب) ایجاد فایل `.env` در پوشه `backend/`

```bash
cd backend
cp .env.example .env
nano .env
```

محتویات `backend/.env`:

```env
DEBUG=False
SECRET_KEY=your-very-long-and-secure-secret-key-here
ALLOWED_HOSTS=api.irpps.org,irpps.org,www.irpps.org,your-server-ip

DB_NAME=irporg_DB
DB_USER=irporg_admin
DB_PASSWORD=your-strong-password-here
DB_HOST=mysql
DB_PORT=3306

MYSQL_ROOT_PASSWORD=your-strong-root-password-here
```

**⚠️ مهم:** برای تولید `SECRET_KEY` امن:

```bash
cd backend
python generate_secret_key.py
```

### 3. ساخت و اجرای کانتینرها

```bash
# بازگشت به root پروژه
cd ..

# Build و اجرای همه services
docker-compose up -d --build
```

این دستور:
- تمام کانتینرها را build می‌کند
- MySQL را راه‌اندازی می‌کند
- Backend را راه‌اندازی می‌کند (migrations و collectstatic به صورت خودکار اجرا می‌شوند)
- Frontend را راه‌اندازی می‌کند

### 4. بررسی وضعیت کانتینرها

```bash
docker-compose ps
```

خروجی باید شبیه این باشد:

```
NAME              STATUS          PORTS
irpps-backend     Up (healthy)    0.0.0.0:8000->8000/tcp
irpps-frontend    Up (healthy)    0.0.0.0:80->80/tcp
irpps-mysql       Up (healthy)    0.0.0.0:3306->3306/tcp
```

### 5. ایجاد کاربر ادمین Django

```bash
docker-compose exec backend python manage.py createsuperuser
```

اطلاعات کاربر ادمین را وارد کنید.

---

## تنظیمات اولیه

### بررسی لاگ‌ها

```bash
# لاگ همه services
docker-compose logs -f

# لاگ یک service خاص
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f mysql
```

### بررسی Health Checks

```bash
# بررسی وضعیت health checks
docker-compose ps

# تست دستی backend
curl http://localhost:8000/api/accounts/profile/

# تست دستی frontend
curl http://localhost/
```

---

## مدیریت و نگهداری

### دستورات مفید Docker Compose

```bash
# مشاهده وضعیت
docker-compose ps

# مشاهده لاگ‌ها
docker-compose logs -f [service-name]

# Restart یک service
docker-compose restart backend

# Restart همه services
docker-compose restart

# توقف services
docker-compose stop

# توقف و حذف containers
docker-compose down

# توقف و حذف containers + volumes (⚠️ دقت کنید!)
docker-compose down -v

# Rebuild یک service
docker-compose build --no-cache backend

# Rebuild همه services
docker-compose build --no-cache
```

### دستورات مدیریتی Django

```bash
# اجرای migrations جدید
docker-compose exec backend python manage.py migrate

# ایجاد migrations جدید
docker-compose exec backend python manage.py makemigrations

# جمع‌آوری static files
docker-compose exec backend python manage.py collectstatic --noinput

# ایجاد superuser جدید
docker-compose exec backend python manage.py createsuperuser

# دسترسی به Django shell
docker-compose exec backend python manage.py shell

# دسترسی به bash container
docker-compose exec backend bash
```

### پشتیبان‌گیری از دیتابیس

```bash
# Backup
docker-compose exec mysql mysqldump -u root -p irporg_DB > backup_$(date +%Y%m%d_%H%M%S).sql

# Restore
docker-compose exec -T mysql mysql -u root -p irporg_DB < backup_file.sql
```

### مدیریت Volumes

```bash
# مشاهده volumes
docker volume ls | grep irpps

# بررسی حجم یک volume
docker system df -v

# حذف یک volume (⚠️ دقت کنید!)
docker volume rm irpps_mysql_data
```

---

## عیب‌یابی

### مشکل: کانتینرها start نمی‌شوند

**بررسی:**

```bash
# بررسی لاگ‌ها
docker-compose logs

# بررسی وضعیت
docker-compose ps -a

# بررسی network
docker network ls
docker network inspect irpps_app-network
```

**راه‌حل‌های رایج:**

1. **پورت 80 یا 8000 در حال استفاده است:**
   ```bash
   # بررسی پورت‌های استفاده شده
   sudo netstat -tulpn | grep :80
   sudo netstat -tulpn | grep :8000
   
   # تغییر پورت در docker-compose.yaml
   ports:
     - "8080:80"  # به جای 80:80
   ```

2. **فایل .env وجود ندارد یا نادرست است:**
   ```bash
   # بررسی وجود فایل
   ls -la backend/.env
   ls -la .env
   
   # بررسی محتویات
   cat backend/.env
   ```

### مشکل: Backend به دیتابیس متصل نمی‌شود

**بررسی:**

```bash
# بررسی وضعیت MySQL
docker-compose logs mysql

# تست اتصال از داخل backend container
docker-compose exec backend python -c "
from decouple import config
import pymysql
try:
    conn = pymysql.connect(
        host=config('DB_HOST'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        database=config('DB_NAME')
    )
    print('Connection successful!')
    conn.close()
except Exception as e:
    print(f'Error: {e}')
"
```

**راه‌حل‌ها:**

1. **اطمینان از صحت اطلاعات در `backend/.env`:**
   - `DB_HOST=mysql` (نه localhost)
   - `DB_NAME`, `DB_USER`, `DB_PASSWORD` باید با `docker-compose.yaml` مطابقت داشته باشند

2. **بررسی health check MySQL:**
   ```bash
   docker-compose ps mysql
   # باید healthy باشد
   ```

3. **Restart MySQL:**
   ```bash
   docker-compose restart mysql
   # صبر کنید تا healthy شود
   docker-compose restart backend
   ```

### مشکل: Static files لود نمی‌شوند

**راه‌حل:**

```bash
# اجرای collectstatic
docker-compose exec backend python manage.py collectstatic --noinput --clear

# بررسی وجود فایل‌ها
docker-compose exec backend ls -la /app/staticfiles/

# Restart backend
docker-compose restart backend
```

### مشکل: Frontend به API متصل نمی‌شود

**بررسی:**

1. **بررسی nginx.conf:**
   ```bash
   docker-compose exec frontend cat /etc/nginx/conf.d/default.conf
   ```

2. **بررسی proxy settings در nginx:**
   - باید `proxy_pass http://backend:8000;` باشد

3. **بررسی network:**
   ```bash
   docker network inspect irpps_app-network
   # باید backend و frontend در یک network باشند
   ```

**راه‌حل:**

```bash
# Rebuild frontend
docker-compose build --no-cache frontend
docker-compose up -d frontend
```

### مشکل: Health check failed

**بررسی:**

```bash
# بررسی health check status
docker inspect irpps-backend | grep -A 10 Health

# تست دستی health check
docker-compose exec backend python -c "import requests; requests.get('http://localhost:8000/api/accounts/profile/')"
```

**راه‌حل:**

1. **بررسی لاگ‌های backend:**
   ```bash
   docker-compose logs backend
   ```

2. **بررسی اتصال به دیتابیس:**
   ```bash
   docker-compose exec backend python manage.py check --database default
   ```

3. **Restart service:**
   ```bash
   docker-compose restart backend
   ```

### مشکل: خطای Permission Denied

**راه‌حل:**

```bash
# تنظیم permissions برای entrypoint script
chmod +x backend/docker-entrypoint.sh

# Rebuild backend
docker-compose build --no-cache backend
docker-compose up -d backend
```

---

## به‌روزرسانی پروژه

### روش 1: با Git (توصیه می‌شود)

```bash
# دریافت آخرین تغییرات
git pull origin master

# Rebuild و restart
docker-compose down
docker-compose up -d --build

# اجرای migrations جدید (اگر وجود دارد)
docker-compose exec backend python manage.py migrate
```

### روش 2: بدون Git

```bash
# توقف services
docker-compose down

# آپلود فایل‌های جدید به سرور
# (از طریق FTP, SCP, یا روش دیگر)

# Rebuild و restart
docker-compose up -d --build

# اجرای migrations
docker-compose exec backend python manage.py migrate
```

### به‌روزرسانی فقط یک Service

```bash
# مثال: فقط backend
docker-compose build --no-cache backend
docker-compose up -d backend

# مثال: فقط frontend
docker-compose build --no-cache frontend
docker-compose up -d frontend
```

---

## نکات امنیتی

1. **هرگز فایل `.env` را commit نکنید**
2. **از SECRET_KEY قوی استفاده کنید**
3. **DEBUG را در production روی False بگذارید**
4. **از پسوردهای قوی برای دیتابیس استفاده کنید**
5. **فایل‌های `.env` را با permissions مناسب تنظیم کنید:**
   ```bash
   chmod 600 backend/.env
   chmod 600 .env
   ```

---

## پشتیبانی

در صورت بروز مشکل:

1. ابتدا لاگ‌ها را بررسی کنید: `docker-compose logs`
2. این راهنما را مطالعه کنید
3. با تیم توسعه تماس بگیرید

---

**آخرین به‌روزرسانی:** 2025

