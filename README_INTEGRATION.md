# 🔗 Frontend-Backend Integration - ISPP Project

## 📌 خلاصه

این پروژه یک سیستم کامل برای **انجمن علمی ریه کودکان ایران** است که شامل:

- **Frontend**: Vue.js 3 + TypeScript + Tailwind CSS
- **Backend**: Django 4 + Django REST Framework
- **Database**: MySQL 8.3
- **Deployment**: Docker + Nginx + Gunicorn

تمام تنظیمات لازم برای اتصال حرفه‌ای فرانت به بکند انجام شده است.

---

## 🎯 وضعیت پروژه

✅ **آماده برای استقرار روی سرور**

- ✅ Frontend به Backend متصل شده
- ✅ Backend به Database متصل شده
- ✅ Authentication کامل
- ✅ API endpoints کامل
- ✅ CORS و CSRF تنظیم شده
- ✅ Docker configuration آماده
- ✅ Documentation کامل

---

## 🚀 شروع سریع

### روش 1: با Docker (توصیه می‌شود)

```bash
# Clone repository
git clone <repository-url>
cd ispp

# اجرای تمام سرویس‌ها
docker-compose up -d --build

# راه‌اندازی دیتابیس
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --noinput

# تست اتصال
chmod +x test-connection.sh
./test-connection.sh
```

سایت در `http://localhost` در دسترس است.

### روش 2: Development (Local)

```bash
# Terminal 1: Backend
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Terminal 2: Frontend
cd frontend
npm install
npm run dev
```

سایت در `http://localhost:5173` در دسترس است.

---

## 📁 ساختار پروژه

```
ispp/
├── frontend/                 # Vue.js Frontend
│   ├── src/
│   │   ├── components/      # کامپوننت‌های Vue
│   │   ├── views/           # صفحات
│   │   ├── stores/          # Pinia stores (auth, etc.)
│   │   ├── services/        # API services
│   │   └── router/          # Vue Router
│   ├── nginx.conf           # Nginx configuration
│   ├── Dockerfile           # Frontend Docker
│   ├── vite.config.ts       # Vite configuration
│   └── .env.production      # Production env vars
│
├── backend/                  # Django Backend
│   ├── accounts/            # User management
│   ├── news/                # News & Announcements
│   ├── events/              # Events management
│   ├── dashboard/           # Admin dashboard
│   ├── doctors/             # Doctors files
│   ├── ispp_project/        # Django settings
│   ├── Dockerfile           # Backend Docker
│   └── requirements.txt     # Python dependencies
│
├── mysql/                    # MySQL data (volume)
│
├── docker-compose.yaml       # Docker Compose config
│
└── Documentation/            # راهنماها
    ├── DEPLOYMENT_GUIDE.md
    ├── TEST_CONNECTION.md
    ├── INTEGRATION_COMPLETE.md
    ├── CHANGES_SUMMARY.md
    ├── FINAL_CHECKLIST.md
    ├── راهنمای_اتصال.md
    └── test-connection.sh
```

---

## 🔗 معماری اتصال

```
┌─────────────────────────────────────────┐
│           Browser (Client)              │
│         https://irpps.org               │
└──────────────────┬──────────────────────┘
                   │
                   │ HTTP/HTTPS
                   │
┌──────────────────▼──────────────────────┐
│         Nginx (Port 80/443)             │
│                                          │
│  ┌────────────────────────────────────┐ │
│  │  Static Files (Vue.js SPA)         │ │
│  │  - HTML, CSS, JS, Images           │ │
│  └────────────────────────────────────┘ │
│                                          │
│  ┌────────────────────────────────────┐ │
│  │  Proxy Rules:                      │ │
│  │  /api/*    → backend:8000          │ │
│  │  /media/*  → backend:8000          │ │
│  │  /static/* → backend:8000          │ │
│  └────────────────────────────────────┘ │
└──────────────────┬──────────────────────┘
                   │
                   │ Docker Network
                   │
┌──────────────────▼──────────────────────┐
│      Django Backend (Port 8000)         │
│                                          │
│  ┌────────────────────────────────────┐ │
│  │  API Endpoints                     │ │
│  │  - Authentication                  │ │
│  │  - News & Events                   │ │
│  │  - Members Management              │ │
│  │  - Dashboard                       │ │
│  └────────────────────────────────────┘ │
└──────────────────┬──────────────────────┘
                   │
                   │ MySQL Connection
                   │
┌──────────────────▼──────────────────────┐
│       MySQL Database (Port 3306)        │
│                                          │
│  - Users (accounts_customuser)          │
│  - News (news_news)                     │
│  - Events (events_event)                │
│  - Sessions (django_session)            │
└─────────────────────────────────────────┘
```

---

## 🔐 Authentication Flow

```
1. User fills login form
   ↓
2. Frontend: POST /api/accounts/login/
   ↓
3. Nginx: Proxy to Backend
   ↓
4. Backend: 
   - Authenticate user
   - Create session
   - Set cookies (sessionid, csrftoken)
   ↓
5. Response: {success: true, user: {...}}
   + Set-Cookie headers
   ↓
6. Frontend:
   - Save user in Pinia store
   - Redirect to /dashboard
   ↓
7. Subsequent requests:
   - Cookies sent automatically
   - CSRF token from cookie
   - Backend verifies session
```

---

## 📊 API Endpoints

### Authentication
- `POST /api/accounts/login/` - ورود کاربر
- `POST /api/accounts/register/` - ثبت نام کاربر
- `POST /api/accounts/logout/` - خروج کاربر
- `GET /api/accounts/profile/` - دریافت پروفایل
- `PUT /api/accounts/profile/update/` - بروزرسانی پروفایل

### Members
- `GET /api/accounts/members/` - لیست اعضا
- `GET /api/accounts/members/pending/` - اعضای در انتظار (admin)
- `POST /api/accounts/members/:id/approve/` - تایید عضو (admin)

### News
- `GET /api/news/` - لیست اخبار
- `GET /api/news/:slug/` - جزئیات خبر
- `POST /api/news/create/` - ایجاد خبر (admin)

### Events
- `GET /api/events/` - لیست رویدادها
- `GET /api/events/:slug/` - جزئیات رویداد
- `POST /api/events/:id/register/` - ثبت نام در رویداد

برای لیست کامل، به `INTEGRATION_COMPLETE.md` مراجعه کنید.

---

## 🧪 تست

### تست خودکار

```bash
./test-connection.sh
```

### تست دستی

```bash
# Backend
curl http://localhost:8000/api/accounts/members/

# Frontend
curl http://localhost:80/api/accounts/members/

# Database
docker-compose exec mysql mysql -u irporg_admin -p irporg_DB
```

### تست در مرورگر

1. باز کردن `http://localhost`
2. رفتن به `/login`
3. وارد شدن با نام کاربری و رمز عبور
4. بررسی Dashboard

---

## 📚 مستندات

### راهنماهای اصلی

1. **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)**
   - راهنمای کامل استقرار روی سرور
   - تنظیمات Docker
   - راه‌اندازی دیتابیس
   - SSL/TLS
   - عیب‌یابی

2. **[TEST_CONNECTION.md](TEST_CONNECTION.md)**
   - تست اتصالات
   - عیب‌یابی رایج
   - مانیتورینگ

3. **[INTEGRATION_COMPLETE.md](INTEGRATION_COMPLETE.md)**
   - جزئیات کامل اتصالات
   - معماری
   - API endpoints
   - چک‌لیست

4. **[راهنمای_اتصال.md](راهنمای_اتصال.md)**
   - راهنمای فارسی ساده
   - نحوه اجرا
   - تست سریع

5. **[CHANGES_SUMMARY.md](CHANGES_SUMMARY.md)**
   - خلاصه تغییرات
   - فایل‌های تغییر یافته
   - آمار

6. **[FINAL_CHECKLIST.md](FINAL_CHECKLIST.md)**
   - چک‌لیست کامل
   - مراحل استقرار
   - عیب‌یابی

---

## 🛠️ تکنولوژی‌ها

### Frontend
- Vue.js 3.4
- TypeScript 5.3
- Vite 5.0
- Vue Router 4.2
- Pinia 3.0
- Axios 1.13
- Tailwind CSS 3.4
- Vue I18n 9.8

### Backend
- Python 3.11
- Django 4.2
- Django CORS Headers
- MySQL Client
- Gunicorn
- Python Decouple

### Infrastructure
- Docker 24+
- Docker Compose 2+
- Nginx (Alpine)
- MySQL 8.3
- Node.js 20 (Alpine)

---

## 🔒 امنیت

### تنظیمات انجام شده

- ✅ CORS با `CORS_ALLOW_CREDENTIALS`
- ✅ CSRF با `CSRF_TRUSTED_ORIGINS`
- ✅ Secure cookies در production
- ✅ SameSite=None برای cross-origin
- ✅ HTTPS ready با `SECURE_PROXY_SSL_HEADER`
- ✅ Session-based authentication
- ✅ Password hashing با Django

### توصیه‌ها

1. تغییر `SECRET_KEY` در production
2. تغییر `DB_PASSWORD`
3. نصب SSL certificate
4. فعال کردن firewall
5. Backup منظم از دیتابیس

---

## 📊 Performance

### بهینه‌سازی‌های انجام شده

- ✅ Vite build optimization
- ✅ Code splitting (vendor chunks)
- ✅ Gzip compression در nginx
- ✅ Static file caching
- ✅ Database connection pooling
- ✅ Gunicorn workers
- ✅ Docker multi-stage builds

---

## 🐛 عیب‌یابی

### مشکلات رایج

#### 1. CORS Error
```
Access to fetch at 'http://localhost:8000/api/...' from origin 'http://localhost:5173' has been blocked by CORS policy
```

**راه حل**: بررسی `CORS_ALLOWED_ORIGINS` در `settings.py`

#### 2. CSRF Token Missing
```
CSRF token missing or incorrect
```

**راه حل**: بررسی `withCredentials: true` در axios و cookies در مرورگر

#### 3. Database Connection Failed
```
Can't connect to MySQL server
```

**راه حل**: بررسی `DB_HOST=mysql` و وضعیت MySQL container

برای جزئیات بیشتر، به `TEST_CONNECTION.md` مراجعه کنید.

---

## 🤝 مشارکت

برای مشارکت در پروژه:

1. Fork کنید
2. Branch جدید بسازید (`git checkout -b feature/amazing-feature`)
3. Commit کنید (`git commit -m 'Add amazing feature'`)
4. Push کنید (`git push origin feature/amazing-feature`)
5. Pull Request باز کنید

---

## 📝 License

این پروژه تحت لایسنس MIT است.

---

## 📞 پشتیبانی

- **Documentation**: مراجعه به فایل‌های راهنما
- **Issues**: باز کردن issue در GitHub
- **Email**: support@irpps.org

---

## 🎉 تشکر

از تمام کسانی که در توسعه این پروژه مشارکت داشتند، تشکر می‌کنیم.

---

**نسخه**: 2.0.0  
**تاریخ**: 2024  
**وضعیت**: ✅ Production Ready

**موفق باشید!** 🚀
