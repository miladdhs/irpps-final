# ✅ چک‌لیست نهایی - آماده برای استقرار

## 🎯 وضعیت کلی

**همه چیز آماده است!** ✅

تمام تنظیمات لازم برای اتصال حرفه‌ای فرانت به بکند و دیتابیس انجام شده است.

---

## 📋 چک‌لیست تنظیمات

### Frontend Configuration

- [x] `vite.config.ts` - Proxy و build settings
- [x] `.env.production` - API URL برای production
- [x] `src/services/api.ts` - Base URL و axios config
- [x] `package.json` - Script `build:prod`
- [x] `nginx.conf` - Proxy rules
- [x] `Dockerfile` - Build و nginx setup

### Backend Configuration

- [x] `settings.py` - CORS, CSRF, Cookies
- [x] `settings.py` - Database connection
- [x] `accounts/views.py` - API endpoints
- [x] `accounts/urls.py` - URL routing
- [x] `urls.py` - Main URLs
- [x] `Dockerfile` - Django و gunicorn

### Docker Configuration

- [x] `docker-compose.yaml` - Services
- [x] Frontend container - Vue + Nginx
- [x] Backend container - Django + Gunicorn
- [x] MySQL container - Database
- [x] Networks - app-network
- [x] Volumes - data persistence
- [x] Health checks - همه سرویس‌ها

### Documentation

- [x] `DEPLOYMENT_GUIDE.md` - راهنمای استقرار
- [x] `TEST_CONNECTION.md` - راهنمای تست
- [x] `INTEGRATION_COMPLETE.md` - جزئیات کامل
- [x] `راهنمای_اتصال.md` - راهنمای فارسی
- [x] `CHANGES_SUMMARY.md` - خلاصه تغییرات
- [x] `FINAL_CHECKLIST.md` - این فایل
- [x] `test-connection.sh` - اسکریپت تست

---

## 🔗 چک‌لیست اتصالات

### Frontend → Backend

- [x] Vite proxy در development
- [x] Nginx proxy در production
- [x] API base URL صحیح
- [x] Axios withCredentials
- [x] CSRF token handling
- [x] Cookie handling

### Backend → Database

- [x] MySQL connection
- [x] Database settings
- [x] Connection pooling
- [x] UTF-8 encoding
- [x] Migrations ready

### Nginx → Backend

- [x] `/api/*` proxy
- [x] `/media/*` proxy
- [x] `/static/*` proxy
- [x] CORS headers
- [x] SPA fallback

---

## 🔐 چک‌لیست امنیت

### CORS

- [x] `CORS_ALLOW_CREDENTIALS = True`
- [x] `CORS_ALLOWED_ORIGINS` تنظیم شده
- [x] `CORS_ALLOW_METHODS` تنظیم شده
- [x] `CORS_ALLOW_HEADERS` تنظیم شده

### CSRF

- [x] `CSRF_TRUSTED_ORIGINS` تنظیم شده
- [x] `CSRF_COOKIE_SECURE` برای production
- [x] `CSRF_COOKIE_SAMESITE = "None"`
- [x] `CSRF_COOKIE_DOMAIN = ".irpps.org"`

### Cookies

- [x] `SESSION_COOKIE_SECURE` برای production
- [x] `SESSION_COOKIE_SAMESITE = "None"`
- [x] `SESSION_COOKIE_DOMAIN = ".irpps.org"`
- [x] `SESSION_COOKIE_AGE = 86400`

### SSL/TLS

- [x] `SECURE_PROXY_SSL_HEADER` تنظیم شده
- [ ] SSL certificate (باید در سرور نصب شود)

---

## 📊 چک‌لیست API Endpoints

### Authentication

- [x] `POST /api/accounts/login/`
- [x] `POST /api/accounts/register/`
- [x] `POST /api/accounts/logout/`
- [x] `GET /api/accounts/profile/`
- [x] `PUT /api/accounts/profile/update/`
- [x] `POST /api/accounts/profile/image/upload/`
- [x] `POST /api/accounts/profile/image/delete/`
- [x] `POST /api/accounts/profile/resume/update/`

### Members

- [x] `GET /api/accounts/members/`
- [x] `GET /api/accounts/members/pending/`
- [x] `POST /api/accounts/members/:id/approve/`
- [x] `POST /api/accounts/members/:id/reject/`

### News

- [x] `GET /api/news/`
- [x] `GET /api/news/:slug/`
- [x] `POST /api/news/create/`
- [x] `PUT /api/news/:id/update/`
- [x] `DELETE /api/news/:id/delete/`

### Events

- [x] `GET /api/events/`
- [x] `GET /api/events/:slug/`
- [x] `POST /api/events/:id/register/`
- [x] `POST /api/events/create/`

---

## 🧪 چک‌لیست تست

### قبل از استقرار

- [ ] تست local development
  ```bash
  cd backend && python manage.py runserver
  cd frontend && npm run dev
  ```

- [ ] تست Docker build
  ```bash
  docker-compose build
  ```

- [ ] تست Docker run
  ```bash
  docker-compose up -d
  ```

- [ ] تست اتصالات
  ```bash
  ./test-connection.sh
  ```

### بعد از استقرار

- [ ] تست Backend health
  ```bash
  curl https://api.irpps.org/
  ```

- [ ] تست Frontend
  ```bash
  curl https://irpps.org/
  ```

- [ ] تست API
  ```bash
  curl https://irpps.org/api/accounts/members/
  ```

- [ ] تست Login در مرورگر
  - باز کردن `https://irpps.org/login`
  - وارد کردن نام کاربری و رمز عبور
  - بررسی انتقال به Dashboard

- [ ] تست Profile
  - باز کردن `https://irpps.org/profile`
  - ویرایش اطلاعات
  - آپلود عکس پروفایل

- [ ] تست Media files
  - بررسی نمایش عکس‌های پروفایل
  - بررسی نمایش تصاویر اخبار

---

## 🚀 چک‌لیست استقرار

### آماده‌سازی سرور

- [ ] Docker نصب شده
- [ ] Docker Compose نصب شده
- [ ] Git نصب شده
- [ ] دسترسی SSH به سرور
- [ ] Firewall تنظیم شده (پورت 80, 443)

### DNS

- [ ] `irpps.org` به IP سرور متصل شده
- [ ] `www.irpps.org` به IP سرور متصل شده
- [ ] `api.irpps.org` به IP سرور متصل شده

### آپلود پروژه

- [ ] Clone repository
  ```bash
  cd /var/www
  git clone <repository-url> ispp
  cd ispp
  ```

### اجرای Docker

- [ ] Build containers
  ```bash
  docker-compose build
  ```

- [ ] Start containers
  ```bash
  docker-compose up -d
  ```

- [ ] بررسی وضعیت
  ```bash
  docker-compose ps
  ```

### راه‌اندازی Database

- [ ] Run migrations
  ```bash
  docker-compose exec backend python manage.py migrate
  ```

- [ ] Create superuser
  ```bash
  docker-compose exec backend python manage.py createsuperuser
  ```

- [ ] Collect static files
  ```bash
  docker-compose exec backend python manage.py collectstatic --noinput
  ```

### SSL/TLS

- [ ] نصب Certbot
  ```bash
  apt-get install certbot python3-certbot-nginx
  ```

- [ ] دریافت گواهی
  ```bash
  certbot --nginx -d irpps.org -d www.irpps.org -d api.irpps.org
  ```

- [ ] تست تمدید خودکار
  ```bash
  certbot renew --dry-run
  ```

---

## 🔍 چک‌لیست عیب‌یابی

### اگر Backend به Database متصل نشد

- [ ] بررسی لاگ MySQL
  ```bash
  docker-compose logs mysql
  ```

- [ ] بررسی متغیرهای محیطی
  ```bash
  docker-compose exec backend env | grep DB_
  ```

- [ ] تست اتصال
  ```bash
  docker-compose exec backend python manage.py dbshell
  ```

### اگر Frontend به Backend متصل نشد

- [ ] بررسی nginx config
  ```bash
  docker-compose exec frontend cat /etc/nginx/conf.d/default.conf
  ```

- [ ] تست اتصال
  ```bash
  docker-compose exec frontend wget -O- http://backend:8000/
  ```

- [ ] بررسی لاگ nginx
  ```bash
  docker-compose logs frontend
  ```

### اگر CORS یا Cookie مشکل دارد

- [ ] بررسی `CORS_ALLOWED_ORIGINS`
- [ ] بررسی `CSRF_TRUSTED_ORIGINS`
- [ ] بررسی `SESSION_COOKIE_DOMAIN`
- [ ] بررسی cookies در مرورگر (F12 > Application > Cookies)

### اگر Static/Media files نمایش داده نمی‌شوند

- [ ] Collect static files
  ```bash
  docker-compose exec backend python manage.py collectstatic --noinput --clear
  ```

- [ ] بررسی permissions
  ```bash
  docker-compose exec backend ls -la /app/staticfiles
  docker-compose exec backend ls -la /app/media
  ```

---

## 📊 چک‌لیست مانیتورینگ

### لاگ‌ها

- [ ] Backend logs
  ```bash
  docker-compose logs -f backend
  ```

- [ ] Frontend logs
  ```bash
  docker-compose logs -f frontend
  ```

- [ ] Database logs
  ```bash
  docker-compose logs -f mysql
  ```

### وضعیت

- [ ] Container status
  ```bash
  docker-compose ps
  ```

- [ ] Resource usage
  ```bash
  docker stats
  ```

- [ ] Health checks
  ```bash
  docker inspect irpps-backend | grep -A 10 Health
  ```

### Backup

- [ ] Database backup
  ```bash
  docker-compose exec mysql mysqldump -u irporg_admin -p irporg_DB > backup.sql
  ```

- [ ] Media files backup
  ```bash
  tar -czf media-backup.tar.gz backend/media/
  ```

---

## 🎉 نتیجه نهایی

### ✅ آماده برای استقرار

همه چیز تنظیم شده و آماده است:

- ✅ Frontend configuration
- ✅ Backend configuration
- ✅ Database configuration
- ✅ Docker configuration
- ✅ Nginx configuration
- ✅ CORS & CSRF
- ✅ Authentication
- ✅ API endpoints
- ✅ Documentation
- ✅ Test scripts

### 📝 مراحل باقی‌مانده

فقط این مراحل باقی مانده:

1. آپلود پروژه به سرور
2. اجرای `docker-compose up -d --build`
3. اجرای migrations
4. ایجاد superuser
5. نصب SSL
6. تست نهایی

### 🚀 دستور نهایی

```bash
# روی سرور
cd /var/www/ispp
docker-compose up -d --build
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --noinput
./test-connection.sh
```

---

## 📞 پشتیبانی

در صورت نیاز به کمک:

1. مراجعه به `DEPLOYMENT_GUIDE.md`
2. مراجعه به `TEST_CONNECTION.md`
3. اجرای `./test-connection.sh`
4. بررسی لاگ‌ها: `docker-compose logs -f`

---

**وضعیت**: ✅ آماده برای استقرار
**تاریخ**: 2024
**نسخه**: 2.0.0

**موفق باشید!** 🎉
