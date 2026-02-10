# راهنمای استقرار پروژه روی سرور با Docker

این راهنما مراحل کامل استقرار پروژه ISPP روی سرور با استفاده از Docker را شرح می‌دهد.

## ✅ پیش‌نیازها

1. Docker و Docker Compose نصب شده باشد
2. دسترسی به سرور با SSH
3. دامنه‌های زیر به IP سرور متصل باشند:
   - `irpps.org`
   - `www.irpps.org`
   - `api.irpps.org`

## 📦 ساختار پروژه

```
.
├── frontend/          # Vue.js + Nginx
├── backend/           # Django + Gunicorn
├── mysql/             # MySQL Database
└── docker-compose.yaml
```

## 🚀 مراحل استقرار

### 1. آپلود پروژه به سرور

```bash
# روی سرور
cd /var/www
git clone <repository-url> ispp
cd ispp
```

### 2. تنظیم متغیرهای محیطی

فایل `.env` در ریشه پروژه وجود دارد، اما اگر نیاز به تغییر دارید:

```bash
# ویرایش تنظیمات دیتابیس در docker-compose.yaml
nano docker-compose.yaml
```

متغیرهای مهم:
- `DB_NAME`: نام دیتابیس (پیش‌فرض: `irporg_DB`)
- `DB_USER`: نام کاربری دیتابیس (پیش‌فرض: `irporg_admin`)
- `DB_PASSWORD`: رمز عبور دیتابیس
- `SECRET_KEY`: کلید امنیتی Django
- `DEBUG`: حالت دیباگ (باید `False` باشد)

### 3. ساخت و اجرای کانتینرها

```bash
# ساخت و اجرای تمام سرویس‌ها
docker-compose up -d --build

# مشاهده لاگ‌ها
docker-compose logs -f

# بررسی وضعیت کانتینرها
docker-compose ps
```

### 4. راه‌اندازی دیتابیس

```bash
# اجرای migrations
docker-compose exec backend python manage.py migrate

# ایجاد superuser
docker-compose exec backend python manage.py createsuperuser

# جمع‌آوری فایل‌های استاتیک
docker-compose exec backend python manage.py collectstatic --noinput
```

### 5. بررسی اتصال

پس از اجرا، سرویس‌ها روی پورت‌های زیر در دسترس هستند:

- **Frontend (Nginx)**: `http://localhost:80`
- **Backend (Django)**: `http://localhost:8000`
- **MySQL**: داخل شبکه Docker (پورت 3306 expose نشده)

## 🔗 اتصال Frontend به Backend

### تنظیمات انجام شده:

#### 1. Frontend Configuration

**فایل: `frontend/.env.production`**
```env
VITE_API_URL=/api
```

**فایل: `frontend/vite.config.ts`**
- Proxy برای development تنظیم شده
- Build optimization برای production

**فایل: `frontend/src/services/api.ts`**
- Base URL به `/api` تغییر کرده
- `withCredentials: true` برای ارسال cookies

#### 2. Nginx Configuration

**فایل: `frontend/nginx.conf`**
```nginx
# Proxy API requests به backend
location /api/ {
    proxy_pass http://backend:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    # ... CORS headers
}

# Proxy media files از backend
location /media/ {
    proxy_pass http://backend:8000;
    # ... headers
}
```

#### 3. Backend Configuration

**فایل: `backend/ispp_project/settings.py`**

```python
# CORS Settings
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "https://irpps.org",
    "https://www.irpps.org",
    "https://api.irpps.org",
]

# CSRF Settings
CSRF_TRUSTED_ORIGINS = [
    "https://irpps.org",
    "https://www.irpps.org",
    "https://api.irpps.org",
]

# Cookie Settings (Production)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SAMESITE = "None"
SESSION_COOKIE_DOMAIN = ".irpps.org"
CSRF_COOKIE_DOMAIN = ".irpps.org"

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'irporg_DB',
        'USER': 'irporg_admin',
        'PASSWORD': 'tHPXArRfwrX3WH!*j',
        'HOST': 'mysql',  # نام سرویس در docker-compose
        'PORT': '3306',
    }
}
```

## 🔐 احراز هویت و Dashboard

### API Endpoints

تمام endpoint های احراز هویت و مدیریت کاربران فعال هستند:

```
POST   /api/accounts/login/              # ورود کاربر
POST   /api/accounts/register/           # ثبت نام کاربر
POST   /api/accounts/logout/             # خروج کاربر
GET    /api/accounts/profile/            # دریافت پروفایل
PUT    /api/accounts/profile/update/     # بروزرسانی پروفایل
POST   /api/accounts/profile/image/upload/   # آپلود عکس پروفایل
POST   /api/accounts/profile/image/delete/   # حذف عکس پروفایل
POST   /api/accounts/profile/resume/update/  # بروزرسانی رزومه
GET    /api/accounts/members/            # لیست اعضا
GET    /api/accounts/members/pending/    # اعضای در انتظار تایید (admin)
POST   /api/accounts/members/:id/approve/    # تایید عضو (admin)
POST   /api/accounts/members/:id/reject/     # رد عضو (admin)
```

### Frontend Routes

```
/login          # صفحه ورود
/register       # صفحه ثبت نام
/dashboard      # داشبورد کاربر
/profile        # پروفایل کاربر
/admin/members  # مدیریت اعضا (فقط admin)
/admin/news     # مدیریت اخبار (فقط admin)
/admin/events   # مدیریت رویدادها (فقط admin)
```

### Auth Store (Pinia)

**فایل: `frontend/src/stores/auth.ts`**

Store مدیریت احراز هویت شامل:
- `login()` - ورود کاربر
- `register()` - ثبت نام کاربر
- `logout()` - خروج کاربر
- `fetchProfile()` - دریافت اطلاعات کاربر
- `updateProfile()` - بروزرسانی پروفایل
- `uploadProfileImage()` - آپلود عکس
- `updateResume()` - بروزرسانی رزومه

## 🧪 تست اتصالات

### 1. تست Backend

```bash
# بررسی health check
curl http://localhost:8000/

# تست API
curl http://localhost:8000/api/accounts/members/
```

### 2. تست Frontend

```bash
# بررسی nginx
curl http://localhost:80/

# تست proxy به backend
curl http://localhost:80/api/accounts/members/
```

### 3. تست Database

```bash
# اتصال به MySQL
docker-compose exec mysql mysql -u irporg_admin -p irporg_DB

# لیست جداول
SHOW TABLES;

# بررسی کاربران
SELECT id, username, first_name, last_name, is_active FROM accounts_customuser;
```

## 📊 مانیتورینگ

### مشاهده لاگ‌ها

```bash
# تمام سرویس‌ها
docker-compose logs -f

# فقط backend
docker-compose logs -f backend

# فقط frontend
docker-compose logs -f frontend

# فقط database
docker-compose logs -f mysql
```

### بررسی وضعیت

```bash
# وضعیت کانتینرها
docker-compose ps

# استفاده از منابع
docker stats

# بررسی health checks
docker inspect irpps-backend | grep -A 10 Health
docker inspect irpps-frontend | grep -A 10 Health
docker inspect irpps-mysql | grep -A 10 Health
```

## 🔄 بروزرسانی پروژه

```bash
# دریافت آخرین تغییرات
git pull

# ری‌بیلد و ری‌استارت
docker-compose down
docker-compose up -d --build

# اجرای migrations جدید
docker-compose exec backend python manage.py migrate

# جمع‌آوری فایل‌های استاتیک
docker-compose exec backend python manage.py collectstatic --noinput
```

## 🛠️ عیب‌یابی

### مشکل: Backend به Database متصل نمی‌شود

```bash
# بررسی لاگ‌های MySQL
docker-compose logs mysql

# بررسی اتصال از backend
docker-compose exec backend python manage.py dbshell
```

### مشکل: Frontend به Backend متصل نمی‌شود

```bash
# بررسی nginx config
docker-compose exec frontend cat /etc/nginx/conf.d/default.conf

# تست اتصال از frontend به backend
docker-compose exec frontend wget -O- http://backend:8000/
```

### مشکل: CORS یا Cookie Issues

1. بررسی کنید `CORS_ALLOWED_ORIGINS` در `settings.py` صحیح است
2. بررسی کنید `CSRF_TRUSTED_ORIGINS` شامل دامنه شماست
3. بررسی کنید `SESSION_COOKIE_DOMAIN` و `CSRF_COOKIE_DOMAIN` صحیح است
4. در مرورگر Developer Tools > Application > Cookies را بررسی کنید

### مشکل: Static Files یا Media Files نمایش داده نمی‌شوند

```bash
# جمع‌آوری مجدد static files
docker-compose exec backend python manage.py collectstatic --noinput --clear

# بررسی permissions
docker-compose exec backend ls -la /app/staticfiles
docker-compose exec backend ls -la /app/media
```

## 🔒 امنیت

### توصیه‌های امنیتی:

1. **تغییر رمزهای عبور**: حتماً `DB_PASSWORD` و `SECRET_KEY` را تغییر دهید
2. **فایروال**: فقط پورت‌های 80 و 443 را باز کنید
3. **SSL/TLS**: از Let's Encrypt برای HTTPS استفاده کنید
4. **Backup**: از دیتابیس backup منظم بگیرید
5. **Updates**: Docker images را به‌روز نگه دارید

### نصب SSL با Let's Encrypt

```bash
# نصب certbot
apt-get install certbot python3-certbot-nginx

# دریافت گواهی
certbot --nginx -d irpps.org -d www.irpps.org -d api.irpps.org

# تنظیم تمدید خودکار
certbot renew --dry-run
```

## 📝 نکات مهم

1. **Environment Variables**: همه متغیرهای محیطی در `docker-compose.yaml` تنظیم شده‌اند
2. **Volumes**: دیتابیس، media files و logs در volumes ذخیره می‌شوند
3. **Health Checks**: تمام سرویس‌ها health check دارند
4. **Restart Policy**: همه سرویس‌ها با `unless-stopped` تنظیم شده‌اند
5. **Network**: تمام سرویس‌ها در یک شبکه bridge قرار دارند

## 🎯 چک‌لیست نهایی

- [ ] Docker و Docker Compose نصب شده
- [ ] فایل‌های پروژه روی سرور آپلود شده
- [ ] متغیرهای محیطی تنظیم شده
- [ ] کانتینرها با موفقیت اجرا شده‌اند
- [ ] Migrations اجرا شده
- [ ] Superuser ایجاد شده
- [ ] Static files جمع‌آوری شده
- [ ] Frontend به Backend متصل است
- [ ] Login/Register کار می‌کند
- [ ] Dashboard در دسترس است
- [ ] Media files نمایش داده می‌شوند
- [ ] SSL نصب شده (برای production)

## 📞 پشتیبانی

در صورت بروز مشکل:
1. لاگ‌ها را بررسی کنید: `docker-compose logs -f`
2. Health checks را چک کنید: `docker-compose ps`
3. اتصالات شبکه را تست کنید

---

**نکته**: این راهنما برای استقرار با Docker طراحی شده است. برای استقرار بدون Docker، به فایل‌های `QUICK_START.md` مراجعه کنید.
