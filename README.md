# انجمن علمی ریه کودکان - ISPP

پروژه وب‌سایت انجمن علمی ریه کودکان ایران - یک اپلیکیشن Full-Stack با Django و Vue.js

## 📋 فهرست مطالب

- [معرفی پروژه](#معرفی-پروژه)
- [تکنولوژی‌های استفاده شده](#تکنولوژی‌های-استفاده-شده)
- [ساختار پروژه](#ساختار-پروژه)
- [نصب و راه‌اندازی](#نصب-و-راه‌اندازی)
- [اجرای پروژه](#اجرای-پروژه)
- [استقرار با Docker](#استقرار-با-docker)
- [استقرار روی cPanel](#استقرار-روی-cpanel)
- [ویژگی‌ها](#ویژگی‌ها)
- [API Endpoints](#api-endpoints)
- [تنظیمات](#تنظیمات)
- [مشارکت](#مشارکت)

---

## معرفی پروژه

این پروژه یک وب‌سایت کامل برای انجمن علمی ریه کودکان ایران است که شامل مدیریت اخبار، رویدادها، کاربران و داشبورد مدیریتی می‌باشد. پروژه به صورت Full-Stack با استفاده از Django در بک‌اند و Vue.js در فرانت‌اند پیاده‌سازی شده است.

**API Base URL:** `https://api.irpps.org`

---

## تکنولوژی‌های استفاده شده

### Backend
- **Django 4.2.7** - فریمورک اصلی بک‌اند
- **Gunicorn 21.2.0** - WSGI HTTP Server برای Production
- **MySQL 8.0+** - پایگاه داده
- **Pillow** - پردازش تصاویر
- **python-decouple** - مدیریت تنظیمات از طریق `.env`
- **django-cors-headers** - مدیریت CORS

### Frontend
- **Vue.js 3.5.10** - فریمورک اصلی فرانت‌اند
- **Vue Router 4.4.5** - مسیریابی
- **Vue i18n 11.1.12** - پشتیبانی چندزبانه (فارسی/انگلیسی)
- **Vite 5.4.10** - Build tool و Development server
- **Vue3 Persian DateTime Picker** - انتخابگر تاریخ شمسی
- **Nginx** - Web Server برای Production (در Docker)

### Infrastructure
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **MySQL** - Database container

---

## ساختار پروژه

```
├── backend/                 # Django Backend
│   ├── accounts/            # اپلیکیشن مدیریت کاربران
│   ├── news/                # اپلیکیشن مدیریت اخبار
│   ├── events/              # اپلیکیشن مدیریت رویدادها
│   ├── dashboard/           # اپلیکیشن داشبورد
│   ├── ispp_project/        # تنظیمات اصلی Django
│   ├── templates/           # قالب‌های Django
│   ├── media/               # فایل‌های آپلود شده
│   ├── Dockerfile           # Dockerfile برای Backend
│   ├── requirements.txt     # وابستگی‌های Python
│   ├── manage.py            # فایل مدیریت Django
│   ├── passenger_wsgi.py   # WSGI config برای cPanel
│   └── .env                 # تنظیمات محیطی (ایجاد کنید)
│
├── frontend/                # Vue.js Frontend
│   ├── src/                 # کدهای منبع Vue.js
│   │   ├── views/           # صفحات Vue
│   │   ├── router/          # تنظیمات Router
│   │   ├── i18n/            # فایل‌های ترجمه
│   │   ├── utils/           # توابع کمکی
│   │   └── assets/          # فایل‌های استاتیک
│   ├── public/              # فایل‌های استاتیک عمومی
│   ├── dist/                # خروجی Build شده (تولید می‌شود)
│   ├── Dockerfile           # Dockerfile برای Frontend
│   ├── nginx.conf           # تنظیمات Nginx
│   ├── package.json         # وابستگی‌های Node.js
│   └── vite.config.ts       # تنظیمات Vite
│
├── docker-compose.yaml      # تنظیمات Docker Compose
├── .dockerignore            # فایل‌های ignore برای Docker
├── .gitignore               # فایل‌های ignore برای Git
└── README.md                # این فایل
```

---

## نصب و راه‌اندازی

### پیش‌نیازها

- **Python 3.9+**
- **Node.js 16+** و **npm**
- **MySQL 8.0+**
- **Docker** و **Docker Compose** (برای استقرار با Docker)

### مراحل نصب (Development)

#### 1. کلون کردن پروژه

```bash
git clone <repository-url>
cd ISPP-Final-OLD
```

#### 2. راه‌اندازی Backend

```bash
# ورود به پوشه backend
cd backend

# ایجاد محیط مجازی
python -m venv venv

# فعال‌سازی محیط مجازی
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# نصب وابستگی‌ها
pip install -r requirements.txt
```

#### 3. تنظیم فایل `.env`

فایل `.env` را در پوشه `backend/` ایجاد کنید (از `env.example.txt` استفاده کنید):

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
```

برای تولید `SECRET_KEY`:

```bash
python generate_secret_key.py
```

#### 4. راه‌اندازی پایگاه داده

```sql
CREATE DATABASE your_database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

#### 5. اجرای Migration ها

```bash
python manage.py migrate
```

#### 6. ایجاد کاربر ادمین

```bash
python manage.py createsuperuser
```

#### 7. راه‌اندازی Frontend

```bash
# بازگشت به root و ورود به frontend
cd ../frontend

# نصب وابستگی‌ها
npm install
```

---

## اجرای پروژه

### حالت توسعه (Development)

#### اجرای Backend (Django)

```bash
cd backend
python manage.py runserver
```

Backend در آدرس `http://127.0.0.1:8000` اجرا می‌شود.

#### اجرای Frontend (Vue.js)

در ترمینال دیگری:

```bash
cd frontend
npm run dev
```

Frontend در آدرس `http://localhost:5173` اجرا می‌شود.

> **نکته:** در حالت توسعه، Vite به صورت خودکار API های Django در پورت 8000 را proxy می‌کند.

### ساخت نسخه تولید (Production Build)

```bash
cd frontend
npm run build:prod
```

این دستور:
1. پروژه Vue.js را Build می‌کند
2. فایل‌های Build شده را در پوشه `dist` قرار می‌دهد
3. فایل `backend/templates/index.html` را به‌روزرسانی می‌کند

### جمع‌آوری فایل‌های استاتیک Django

```bash
cd backend
python manage.py collectstatic --noinput
```

---

## استقرار با Docker

### پیش‌نیازها

- Docker و Docker Compose نصب شده باشد
- فایل `.env` در `backend/` تنظیم شده باشد

### مراحل استقرار

#### 1. تنظیم فایل `.env`

فایل `.env` را در `backend/` ایجاد/ویرایش کنید:

```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=your-domain.com,api.your-domain.com

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=mysql
DB_PORT=3306
```

**نکته مهم:** در Docker، `DB_HOST` باید `mysql` باشد (نام service در docker-compose).

#### 2. تنظیم Environment Variables برای Docker Compose

می‌توانید یک فایل `.env` در root پروژه ایجاد کنید یا مستقیماً در `docker-compose.yaml` تنظیم کنید:

```env
DB_NAME=irporg_DB
DB_USER=irporg_admin
DB_PASSWORD=your_password
MYSQL_ROOT_PASSWORD=your_root_password
```

#### 3. Build و اجرای Container ها

```bash
# Build و اجرای همه services
docker-compose up -d --build

# مشاهده لاگ‌ها
docker-compose logs -f

# توقف services
docker-compose down

# توقف و حذف volumes (دقت کنید!)
docker-compose down -v
```

#### 4. اجرای Migration ها

```bash
# اجرای migration در container
docker-compose exec backend python manage.py migrate

# ایجاد superuser
docker-compose exec backend python manage.py createsuperuser

# جمع‌آوری static files
docker-compose exec backend python manage.py collectstatic --noinput
```

#### 5. دسترسی به پروژه

- **Frontend:** `http://localhost` (پورت 80)
- **Backend API:** `http://localhost:8000`
- **Admin Panel:** `http://localhost/admin`

### ساختار Docker

- **Frontend Container:** Vue.js + Nginx (پورت 80)
- **Backend Container:** Django + Gunicorn (پورت 8000)
- **MySQL Container:** Database (پورت داخلی)

### دستورات مفید Docker

```bash
# مشاهده وضعیت containers
docker-compose ps

# مشاهده لاگ‌های یک service
docker-compose logs frontend
docker-compose logs backend
docker-compose logs mysql

# ورود به shell یک container
docker-compose exec backend bash
docker-compose exec frontend sh

# Restart یک service
docker-compose restart backend

# Rebuild یک service
docker-compose build --no-cache backend
```

---

## استقرار روی cPanel

برای استقرار روی cPanel، به فایل‌های زیر مراجعه کنید:

- `CPANEL_DEPLOY_CHECKLIST.md` - چک‌لیست کامل استقرار
- `DEPLOY_CHECKLIST.md` - چک‌لیست عمومی
- `DEPLOY.md` - راهنمای استقرار

### مراحل کلی

1. **Build کردن Frontend:**
   ```bash
   cd frontend
   npm run build:prod
   ```

2. **تنظیم فایل `.env` در `backend/`:**
   ```env
   DEBUG=False
   SECRET_KEY=your-production-secret-key
   ALLOWED_HOSTS=api.irpps.org,irpps.org
   ```

3. **آپلود فایل‌ها به `public_html/`**

4. **تنظیم Python App در cPanel**

5. **اجرای Migration ها و collectstatic**

---

## ویژگی‌ها

### ✨ ویژگی‌های اصلی

- ✅ **احراز هویت کاربران** - سیستم کامل ثبت نام و ورود
- ✅ **مدیریت اخبار** - ایجاد، ویرایش و انتشار اخبار
- ✅ **مدیریت رویدادها** - ایجاد رویدادها و ثبت نام کاربران
- ✅ **داشبورد کاربری** - پنل مدیریت برای کاربران
- ✅ **پشتیبانی چندزبانه** - فارسی و انگلیسی
- ✅ **واکنش‌گرا (Responsive)** - سازگار با تمام دستگاه‌ها
- ✅ **Admin Panel** - پنل مدیریت Django
- ✅ **مدیریت تصاویر** - آپلود و مدیریت تصاویر پروفایل و محتوا
- ✅ **API کامل** - RESTful API برای تمام عملیات

### 📱 صفحات وب‌سایت

- `/` - صفحه اصلی
- `/about` - درباره ما
- `/services` - رویدادها و اطلاعیه‌ها
- `/team` - تیم
- `/contact` - تماس با ما
- `/register` - ثبت نام
- `/news/:slug` - جزئیات خبر
- `/events/:slug` - جزئیات رویداد
- `/dashboard` - داشبورد کاربر (نیاز به ورود)

---

## API Endpoints

**Base URL:** `https://api.irpps.org`

### احراز هویت (`/api/accounts/`)

- `POST /api/accounts/register/` - ثبت نام کاربر جدید
- `POST /api/accounts/login/` - ورود کاربر
- `POST /api/accounts/logout/` - خروج کاربر
- `GET /api/accounts/profile/` - دریافت پروفایل کاربر
- `PUT /api/accounts/profile/update/` - به‌روزرسانی پروفایل
- `POST /api/accounts/profile/image/upload/` - آپلود تصویر پروفایل
- `GET /api/accounts/members/` - لیست اعضا

### اخبار (`/api/news/`)

- `GET /api/news/` - لیست اخبار (با pagination)
- `GET /api/news/:slug/` - جزئیات خبر
- `GET /api/news/announcements/` - لیست اطلاعیه‌ها
- `POST /api/news/create/` - ایجاد خبر (نیاز به login)
- `POST /api/news/announcements/create/` - ایجاد اطلاعیه (نیاز به login)

### رویدادها (`/api/events/`)

- `GET /api/events/` - لیست رویدادها (با pagination)
- `GET /api/events/:slug/` - جزئیات رویداد
- `POST /api/events/:id/register/` - ثبت نام در رویداد
- `GET /api/events/my-registrations/` - رویدادهای ثبت نام شده کاربر
- `POST /api/events/create/` - ایجاد رویداد (نیاز به login)

### داشبورد (`/api/dashboard/`)

- `GET /api/dashboard/admin/stats/` - آمار کلی (فقط برای admin)
- `GET /api/dashboard/my-news/` - اخبار کاربر
- `GET /api/dashboard/my-events/` - رویدادهای کاربر

---

## تنظیمات

### Environment Variables

فایل `.env` در `backend/` باید شامل موارد زیر باشد:

```env
# Django Settings
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=api.irpps.org,irpps.org,www.irpps.org

# Database
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost  # یا mysql برای Docker
DB_PORT=3306

# Optional: Email
EMAIL_HOST=smtp.yourdomain.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@yourdomain.com
EMAIL_HOST_PASSWORD=your-email-password
```

### CORS Settings

CORS در `settings.py` برای دامنه‌های زیر تنظیم شده:
- `https://irpps.org`
- `https://api.irpps.org`

### Static Files

- **STATIC_URL:** `/assets/`
- **STATIC_ROOT:** `backend/staticfiles/`
- **MEDIA_URL:** `/media/`
- **MEDIA_ROOT:** `backend/media/`

---

## پایگاه داده

### مدل‌های اصلی

#### CustomUser
- اطلاعات کاربری کامل
- پروفایل تصویری
- اطلاعات تخصصی (تخصص، سابقه کار، امتیاز)
- رزومه (تحصیلات، مقالات، جوایز، گواهینامه‌ها)

#### News
- عنوان، محتوا، تصویر
- نویسنده، دسته‌بندی، برچسب‌ها
- وضعیت انتشار، تعداد بازدید

#### Announcement
- اطلاعیه‌های مهم
- وضعیت مهم بودن

#### Event
- اطلاعات کامل رویداد
- نوع رویداد (کنفرانس، کارگاه، سمینار، کنگره)
- تاریخ و مکان
- مهلت ثبت نام، قیمت
- اطلاعات سخنرانان و برنامه

#### EventRegistration
- ثبت نام کاربران در رویدادها
- وضعیت تأیید

---

## دستورات مدیریتی Django

```bash
# ایجاد migration جدید
python manage.py makemigrations

# اجرای migration ها
python manage.py migrate

# ایجاد superuser
python manage.py createsuperuser

# جمع‌آوری static files
python manage.py collectstatic --noinput

# دستورات سفارشی
python manage.py add_sample_users
python manage.py set_default_profile_image
python manage.py clear_all_profile_images
```

---

## عیب‌یابی

### مشکلات رایج

#### مشکل: Static files لود نمی‌شوند
- بررسی کنید که `collectstatic` اجرا شده باشد
- بررسی کنید که `STATIC_ROOT` و `STATIC_URL` درست تنظیم شده باشند

#### مشکل: خطای CORS
- بررسی کنید که دامنه در `CORS_ALLOWED_ORIGINS` موجود باشد
- بررسی کنید که `CORS_ALLOW_CREDENTIALS=True` است

#### مشکل: خطای اتصال به دیتابیس
- بررسی کنید که اطلاعات دیتابیس در `.env` درست باشد
- در Docker، `DB_HOST` باید `mysql` باشد

#### مشکل: Frontend به API متصل نمی‌شود
- بررسی کنید که `getApiUrl()` در frontend درست کار می‌کند
- در Development، Vite proxy باید به `http://localhost:8000` اشاره کند
- در Production، باید به `https://api.irpps.org` اشاره کند

---

## مشارکت

برای مشارکت در پروژه:

1. پروژه را Fork کنید
2. یک Branch جدید ایجاد کنید (`git checkout -b feature/AmazingFeature`)
3. تغییرات خود را Commit کنید (`git commit -m 'Add some AmazingFeature'`)
4. Branch را Push کنید (`git push origin feature/AmazingFeature`)
5. یک Pull Request ایجاد کنید

---

## مجوز

این پروژه برای انجمن علمی ریه کودکان ایران توسعه یافته است.

---

## تماس و پشتیبانی

برای سوالات و پشتیبانی، لطفاً با تیم توسعه تماس بگیرید.

---

**توسعه یافته با ❤️ برای انجمن علمی ریه کودکان ایران**
