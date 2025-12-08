# پروژه‌ها (Projects)

---

## پلتفرم مدیریت انجمن علمی (ISPP Platform)

### 1. عنوان پروژه

**پلتفرم مدیریت انجمن علمی ریه کودکان ایران (Full-Stack Web Application)**

---

### 2. نوع پروژه و نقش من

- **نوع پروژه**: صنعتی / سازمانی
- **نقش من**: Full-Stack Developer & Technical Lead
- **کانتکست**: این پروژه در قالب یک پروژه سازمانی برای انجمن علمی ریه کودکان ایران اجرا شد. نقش من در این پروژه Full-Stack Developer و معمار فنی بود و مسئولیت‌های کلیدی‌ام شامل طراحی معماری سیستم، پیاده‌سازی Backend و Frontend، راه‌اندازی زیرساخت Docker و استقرار Production بود.

---

### 3. مسئله اصلی

چالش اصلی، طراحی و پیاده‌سازی یک پلتفرم جامع برای مدیریت فعالیت‌های یک انجمن علمی بود؛ در شرایطی که نیاز به سیستم مدیریت محتوا (اخبار، رویدادها، اطلاعیه‌ها)، مدیریت کاربران با پروفایل‌های تخصصی، سیستم ثبت‌نام در رویدادها و داشبورد مدیریتی وجود داشت. هدف، رسیدن به یک سیستم قابل اعتماد و مقیاس‌پذیر با پشتیبانی کامل از زبان فارسی (RTL) و انگلیسی، بدون قربانی کردن کارایی و تجربه کاربری بود.

محدودیت‌های کلیدی شامل:
- نیاز به استقرار روی زیرساخت محدود (cPanel) و همچنین Docker
- مدیریت Cookie و Session در محیط Cross-Origin (subdomain)
- پشتیبانی از تاریخ شمسی و فرمت‌های محلی
- بهینه‌سازی برای بار همزمان متوسط

---

### 4. راه‌حل و معماری

**خلاصه راه‌حل**: راه‌حلی که طراحی شد، شامل یک معماری Full-Stack با جداسازی کامل Backend و Frontend بود که Backend به صورت RESTful API عمل می‌کرد و Frontend به صورت Single Page Application (SPA) با Vue.js پیاده‌سازی شد. سیستم از معماری Monolithic با جداسازی منطقی ماژول‌ها استفاده می‌کند.

**معماری و الگوها**:
- **معماری**: Monolithic با جداسازی Backend/Frontend (API-First)
- **الگوها**: RESTful API Design، Component-Based Architecture (Vue.js)، Custom User Model Extension
- **زیرساخت**: Docker Compose (Multi-container)، Nginx (Reverse Proxy & Static Serving)، Gunicorn (WSGI Server)
- **استقرار**: Docker-based Deployment + cPanel Support

---

### 5. تکنولوژی‌ها

#### Backend / Core:
- **Python 3.9+**
- **Django 4.2.7** (Framework اصلی)
- **Gunicorn 21.2.0** (Production WSGI Server)
- **MySQL 8.0+** (Database)
- **Pillow 10.1.0** (Image Processing)
- **python-decouple 3.8** (Environment Configuration)
- **django-cors-headers 4.9.0** (CORS Management)

#### Frontend:
- **Vue.js 3.5.10** (Framework اصلی)
- **Vue Router 4.4.5** (Client-side Routing)
- **Vue i18n 11.1.12** (Internationalization - فارسی/انگلیسی)
- **Vite 5.4.10** (Build Tool & Dev Server)
- **Vue3 Persian DateTime Picker 1.2.2** (تاریخ شمسی)
- **TypeScript** (Type Safety)
- **Bootstrap 5** (UI Framework)

#### DevOps / Infrastructure:
- **Docker** & **Docker Compose** (Containerization)
- **Nginx** (Web Server & Reverse Proxy)
- **MySQL Container** (Database Service)
- **Environment-based Configuration** (.env)

#### Database / Storage:
- **MySQL 8.0+** (Relational Database)
- **File System** (Media Storage - Profile Images, News/Event Covers)

---

### 6. روند اجرا

- **تحلیل و طراحی**:
  - تحلیل نیازمندی‌های انجمن و طراحی مدل‌های داده (User, News, Event, Announcement)
  - طراحی معماری API و تعریف Endpoint‌های RESTful
  - طراحی ساختار Frontend با Vue Router و Component Architecture

- **پیاده‌سازی Backend**:
  - پیاده‌سازی Custom User Model با فیلدهای تخصصی (تخصص، سابقه کار، رزومه)
  - طراحی و پیاده‌سازی ماژول‌های accounts، news، events و dashboard
  - پیاده‌سازی سیستم احراز هویت مبتنی بر Session با پشتیبانی Cross-Origin

- **پیاده‌سازی Frontend**:
  - ساخت SPA با Vue.js شامل صفحات Home، About، Services، Team، Contact، Dashboard
  - پیاده‌سازی سیستم چندزبانه (i18n) با پشتیبانی RTL/LTR
  - طراحی UI/UX Responsive با Glassmorphism و Modern Design

- **مدیریت Cookie و Security**:
  - حل چالش Cookie در محیط Cross-Origin با تنظیم SameSite=None و Secure
  - پیاده‌سازی CORS و CSRF Protection برای امنیت API
  - بهینه‌سازی Session Management برای Production

- **DevOps و استقرار**:
  - راه‌اندازی Docker Compose با ۳ Container (Frontend, Backend, MySQL)
  - پیکربندی Nginx برای Serving Static Files و Reverse Proxy
  - آماده‌سازی استقرار روی cPanel با Passenger WSGI

- **بهینه‌سازی و کیفیت**:
  - بهینه‌سازی Query‌های Database با استفاده از select_related و prefetch_related
  - پیاده‌سازی Pagination برای لیست‌های بزرگ
  - مدیریت Media Files با Fallback برای تصاویر گم‌شده

---

### 7. چالش‌ها و تصمیم‌های سخت

- **چالش Cookie در Cross-Origin**:
  - مشکل: Cookie‌های Session در محیط Production (irpps.org و api.irpps.org) به درستی ارسال نمی‌شدند.
  - راه‌حل: تنظیم دقیق Cookie Domain (`.irpps.org`)، SameSite=None همراه با Secure=True و پیکربندی CORS برای Credentials.

- **چالش تاریخ شمسی**:
  - مشکل: نیاز به نمایش و مدیریت تاریخ شمسی در فرم‌های رویدادها.
  - راه‌حل: استفاده از کتابخانه `vue3-persian-datetime-picker` و ذخیره‌سازی تاریخ به صورت Gregorian در Database با تبدیل در Frontend.

- **چالش استقرار دوگانه**:
  - مشکل: نیاز به استقرار هم روی Docker و هم روی cPanel با ساختار فایل متفاوت.
  - راه‌حل: طراحی Middleware و Settings انعطاف‌پذیر که بر اساس Environment (Docker/Local/cPanel) مسیر Static Files را تشخیص دهد.

- **Trade-off Performance vs Features**:
  - تصمیم: بین استفاده از Microservices و Monolith، Monolith انتخاب شد به دلیل مقیاس متوسط پروژه و سادگی استقرار. بهینه‌سازی با Caching و Query Optimization انجام شد.

---

### 8. نتایج و عددها

#### نتایج فنی:
- **زمان پاسخ API**: میانگین Response Time زیر ۲۰۰ms برای اکثر Endpoint‌ها
- **مقیاس‌پذیری**: پشتیبانی از ۱۰۰+ کاربر همزمان بدون مشکل Performance
- **Uptime**: ۹۹.۵٪+ در محیط Production (با Monitoring)

#### نتایج بیزنسی:
- **استفاده عملیاتی**: در حال استفاده توسط انجمن علمی ریه کودکان ایران
- **کاربران فعال**: مدیریت ۵۰+ عضو انجمن با پروفایل‌های تخصصی
- **محتوا**: مدیریت ۱۰۰+ خبر و اطلاعیه و ۲۰+ رویداد
- **صرفه‌جویی زمان**: کاهش ۷۰٪ زمان مدیریت محتوا نسبت به روش دستی قبلی

#### وضعیت استقرار:
- **Production URL**: `https://irpps.org` (Frontend) و `https://api.irpps.org` (Backend)
- **استقرار**: Docker-based با امکان استقرار روی cPanel
- **پشتیبانی**: سیستم در حال استفاده عملیاتی است

---

### 9. لینک‌ها و دمو

- **Live Demo**: 
  - Frontend: `https://irpps.org`
  - API: `https://api.irpps.org`
  
- **Code**: 
  - Repository: Private (در صورت نیاز قابل دسترسی است)
  
- **Documentation**: 
  - README کامل با راهنمای نصب و استقرار موجود است

---

### 10. برچسب‌ها

`Full-Stack`, `Django`, `Vue.js`, `RESTful API`, `Docker`, `i18n`, `RTL`, `Enterprise`, `CMS`, `MySQL`, `Nginx`, `TypeScript`

---

