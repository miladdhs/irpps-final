# ✅ اتصال کامل Frontend به Backend و Database

## 🎯 خلاصه تغییرات

تمام تغییرات لازم برای اتصال حرفه‌ای فرانت به بکند و دیتابیس انجام شده است.

## 📋 فایل‌های تغییر یافته

### Frontend

1. **`frontend/vite.config.ts`**
   - اضافه شدن proxy برای development
   - تنظیمات build optimization برای production
   - تنظیم manual chunks برای بهبود performance

2. **`frontend/.env.production`** (جدید)
   - تنظیم `VITE_API_URL=/api` برای production
   - استفاده از relative path برای API calls

3. **`frontend/src/services/api.ts`**
   - تغییر base URL به `/api` برای production
   - حفظ `withCredentials: true` برای cookies
   - CSRF token handling

4. **`frontend/package.json`**
   - اضافه شدن script `build:prod` برای build production

### Backend

تمام تنظیمات backend از قبل صحیح بوده و نیازی به تغییر نداشته:

- ✅ CORS تنظیم شده
- ✅ CSRF تنظیم شده  
- ✅ Cookie settings صحیح
- ✅ Database connection به MySQL
- ✅ API endpoints کامل

### Nginx

تنظیمات nginx از قبل صحیح بوده:

- ✅ Proxy به backend برای `/api/`
- ✅ Proxy به backend برای `/media/`
- ✅ CORS headers
- ✅ SPA fallback

### Docker

تنظیمات docker-compose از قبل صحیح بوده:

- ✅ Frontend container (Vue + Nginx)
- ✅ Backend container (Django + Gunicorn)
- ✅ MySQL container
- ✅ Health checks
- ✅ Networks و volumes

## 🔗 نحوه اتصال

### Development (Local)

```bash
# Terminal 1: Backend
cd backend
python manage.py runserver

# Terminal 2: Frontend  
cd frontend
npm run dev
```

در development، Vite proxy می‌کند:
- `http://localhost:5173/api/*` → `http://localhost:8000/api/*`
- `http://localhost:5173/media/*` → `http://localhost:8000/media/*`

### Production (Docker)

```bash
# اجرای تمام سرویس‌ها
docker-compose up -d --build
```

در production، Nginx proxy می‌کند:
- `http://irpps.org/api/*` → `http://backend:8000/api/*`
- `http://irpps.org/media/*` → `http://backend:8000/media/*`

## 🎨 معماری اتصال

```
┌─────────────────────────────────────────────────────────┐
│                        Browser                          │
│                    (irpps.org)                          │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ HTTP Request
                     │
┌────────────────────▼────────────────────────────────────┐
│                  Nginx (Port 80)                        │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Static Files (Vue.js SPA)                       │  │
│  │  - HTML, CSS, JS                                 │  │
│  │  - Images, Fonts                                 │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Proxy Rules:                                    │  │
│  │  /api/*    → http://backend:8000/api/*          │  │
│  │  /media/*  → http://backend:8000/media/*        │  │
│  │  /static/* → http://backend:8000/static/*       │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ Proxy
                     │
┌────────────────────▼────────────────────────────────────┐
│              Django Backend (Port 8000)                 │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  API Endpoints:                                  │  │
│  │  - /api/accounts/*  (Login, Register, Profile)  │  │
│  │  - /api/news/*      (News, Announcements)       │  │
│  │  - /api/events/*    (Events, Registration)      │  │
│  │  - /api/dashboard/* (Admin Dashboard)           │  │
│  │  - /api/doctors/*   (Doctors Files)             │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Authentication:                                 │  │
│  │  - Session-based (Django sessions)              │  │
│  │  - CSRF protection                               │  │
│  │  - Cookie-based (httpOnly, secure)              │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ MySQL Connection
                     │
┌────────────────────▼────────────────────────────────────┐
│              MySQL Database (Port 3306)                 │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Database: irporg_DB                             │  │
│  │  User: irporg_admin                              │  │
│  │                                                   │  │
│  │  Tables:                                         │  │
│  │  - accounts_customuser (Users)                   │  │
│  │  - news_news (News)                              │  │
│  │  - news_announcement (Announcements)             │  │
│  │  - events_event (Events)                         │  │
│  │  - events_eventregistration (Registrations)      │  │
│  │  - django_session (Sessions)                     │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

## 🔐 Authentication Flow

```
1. کاربر فرم login را پر می‌کند
   ↓
2. Frontend: POST /api/accounts/login/
   {username, password}
   ↓
3. Nginx: Proxy به Backend
   ↓
4. Backend: 
   - Authenticate user
   - Create session
   - Set cookies (sessionid, csrftoken)
   ↓
5. Response: 
   {success: true, user: {...}}
   + Set-Cookie headers
   ↓
6. Frontend:
   - ذخیره user در Pinia store
   - Redirect به /dashboard
   ↓
7. درخواست‌های بعدی:
   - Cookies به صورت خودکار ارسال می‌شوند
   - CSRF token از cookie خوانده می‌شود
   - Backend session را verify می‌کند
```

## 📊 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/accounts/login/` | ورود کاربر | ❌ |
| POST | `/api/accounts/register/` | ثبت نام کاربر | ❌ |
| POST | `/api/accounts/logout/` | خروج کاربر | ✅ |
| GET | `/api/accounts/profile/` | دریافت پروفایل | ✅ |
| PUT | `/api/accounts/profile/update/` | بروزرسانی پروفایل | ✅ |
| POST | `/api/accounts/profile/image/upload/` | آپلود عکس | ✅ |
| POST | `/api/accounts/profile/image/delete/` | حذف عکس | ✅ |
| POST | `/api/accounts/profile/resume/update/` | بروزرسانی رزومه | ✅ |

### Members

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/accounts/members/` | لیست اعضا | ❌ |
| GET | `/api/accounts/members/pending/` | اعضای در انتظار | ✅ Admin |
| POST | `/api/accounts/members/:id/approve/` | تایید عضو | ✅ Admin |
| POST | `/api/accounts/members/:id/reject/` | رد عضو | ✅ Admin |

### News

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/news/` | لیست اخبار | ❌ |
| GET | `/api/news/:slug/` | جزئیات خبر | ❌ |
| POST | `/api/news/create/` | ایجاد خبر | ✅ Admin |
| PUT | `/api/news/:id/update/` | بروزرسانی خبر | ✅ Admin |
| DELETE | `/api/news/:id/delete/` | حذف خبر | ✅ Admin |

### Events

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/events/` | لیست رویدادها | ❌ |
| GET | `/api/events/:slug/` | جزئیات رویداد | ❌ |
| POST | `/api/events/:id/register/` | ثبت نام در رویداد | ✅ |
| POST | `/api/events/create/` | ایجاد رویداد | ✅ Admin |

## 🧪 تست اتصال

### روش 1: اسکریپت خودکار

```bash
chmod +x test-connection.sh
./test-connection.sh
```

### روش 2: تست دستی

```bash
# تست Backend
curl http://localhost:8000/api/accounts/members/

# تست Frontend Proxy
curl http://localhost:80/api/accounts/members/

# تست Database
docker-compose exec mysql mysql -u irporg_admin -p irporg_DB
```

### روش 3: تست در مرورگر

1. باز کردن `http://localhost` یا `http://irpps.org`
2. باز کردن Developer Tools (F12)
3. رفتن به Console
4. اجرای:

```javascript
// تست API
fetch('/api/accounts/members/')
  .then(r => r.json())
  .then(data => console.log(data))

// تست Login
fetch('/api/accounts/login/', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  credentials: 'include',
  body: JSON.stringify({username: 'admin', password: 'pass'})
})
.then(r => r.json())
.then(data => console.log(data))
```

## 📁 فایل‌های راهنما

1. **`DEPLOYMENT_GUIDE.md`** - راهنمای کامل استقرار روی سرور
2. **`TEST_CONNECTION.md`** - راهنمای تست اتصالات
3. **`test-connection.sh`** - اسکریپت تست خودکار
4. **`INTEGRATION_COMPLETE.md`** - این فایل (خلاصه کامل)

## ✅ چک‌لیست نهایی

### Frontend
- [x] Vite config با proxy برای development
- [x] `.env.production` برای production
- [x] API service با base URL صحیح
- [x] Auth store با Pinia
- [x] Router guards برای صفحات محافظت شده
- [x] Axios interceptors برای CSRF token

### Backend
- [x] CORS تنظیم شده
- [x] CSRF تنظیم شده
- [x] Cookie settings صحیح
- [x] Database connection به MySQL
- [x] API endpoints کامل
- [x] Authentication views
- [x] Media file handling

### Nginx
- [x] Proxy به backend برای `/api/`
- [x] Proxy به backend برای `/media/`
- [x] CORS headers
- [x] SPA fallback
- [x] Static file serving

### Docker
- [x] Frontend container
- [x] Backend container
- [x] MySQL container
- [x] Health checks
- [x] Networks
- [x] Volumes
- [x] Environment variables

### Database
- [x] MySQL 8.3
- [x] UTF-8 encoding
- [x] User permissions
- [x] Migrations
- [x] Initial data

## 🚀 دستورات سریع

### Development

```bash
# Backend
cd backend
python manage.py runserver

# Frontend
cd frontend
npm run dev
```

### Production

```bash
# Build و اجرا
docker-compose up -d --build

# مشاهده لاگ‌ها
docker-compose logs -f

# تست اتصال
./test-connection.sh

# Restart
docker-compose restart

# Stop
docker-compose down
```

### Database

```bash
# Migrations
docker-compose exec backend python manage.py migrate

# Create superuser
docker-compose exec backend python manage.py createsuperuser

# Shell
docker-compose exec backend python manage.py shell

# Database shell
docker-compose exec mysql mysql -u irporg_admin -p irporg_DB
```

## 🎉 نتیجه

همه چیز آماده است! فرانت به صورت حرفه‌ای به بکند و دیتابیس متصل شده:

✅ **Frontend** → Nginx → **Backend** → **MySQL**
✅ Authentication کامل
✅ API endpoints کامل
✅ Media files handling
✅ CORS و CSRF صحیح
✅ Docker ready
✅ Production ready

## 📞 پشتیبانی

در صورت بروز مشکل:

1. لاگ‌ها را بررسی کنید: `docker-compose logs -f`
2. تست اتصال را اجرا کنید: `./test-connection.sh`
3. فایل `TEST_CONNECTION.md` را مطالعه کنید
4. فایل `DEPLOYMENT_GUIDE.md` را مطالعه کنید

---

**تاریخ**: 2024
**نسخه**: 2.0.0
**وضعیت**: ✅ آماده برای استقرار
