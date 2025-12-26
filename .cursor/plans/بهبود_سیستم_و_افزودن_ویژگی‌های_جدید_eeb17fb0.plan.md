---
name: بهبود سیستم و افزودن ویژگی‌های جدید
overview: این پلان شامل رفع مشکل اتصال دیتابیس، ایجاد صفحه پزشکان، به‌روزرسانی انتشارات، حذف لینک English و پیاده‌سازی سیستم درخواست عضویت با تایید ادمین است.
todos:
  - id: db_connection_fix
    content: اضافه کردن retry logic و timeout handling برای اتصال دیتابیس
    status: pending
  - id: doctors_page
    content: ایجاد صفحه پزشکان با دسته‌بندی‌ها و API برای خواندن فایل‌ها
    status: pending
  - id: publications_update
    content: به‌روزرسانی صفحه انتشارات با دسته‌بندی‌های جدید
    status: pending
  - id: remove_english_link
    content: حذف لینک English از navbar
    status: pending
  - id: membership_request_backend
    content: تغییر register_view و اضافه کردن API های تایید/رد کاربران
    status: pending
  - id: membership_request_frontend
    content: اضافه کردن فرم درخواست عضویت به modal لاگین و تب مدیریت در داشبورد
    status: pending
    dependencies:
      - membership_request_backend
---

# بهبود سیستم و افزودن ویژگی‌های جدید

## 1. رفع مشکل اتصال دیتابیس

### Backend Changes

- **فایل**: `backend/ispp_project/settings.py`
- اضافه کردن `CONN_MAX_AGE` برای connection pooling
- اضافه کردن timeout options به `OPTIONS`
- اضافه کردن retry logic در middleware
- **فایل**: `backend/ispp_project/middleware.py` (یا ایجاد جدید)
- پیاده‌سازی middleware برای retry logic در صورت خطای اتصال
- اضافه کردن timeout handling

## 2. ایجاد صفحه پزشکان

### Frontend Changes

- **فایل جدید**: `frontend/src/views/Doctors.vue`
- صفحه اصلی با دسته‌بندی‌ها:
- اسکای روم (SkyRoom - لینک‌های خارجی)
- ویدیو (فایل‌های ویدیویی یا لینک‌ها)
- اسلایدها (فایل‌های PDF/PPT)
- کتاب (خواندن از `Content/Books/` با زیرپوشه‌ها)
- بروشور (خواندن از `Content/Broshour/`)
- منابع و مدارک (فایل‌های PDF)
- هر دسته به صورت کارت‌های قابل کلیک با دانلود فایل
- استفاده از API endpoint برای لیست کردن فایل‌ها

### Backend Changes

- **فایل جدید**: `backend/doctors/views.py`
- API endpoint: `GET /api/doctors/files/` برای لیست کردن فایل‌ها
- پشتیبانی از دسته‌بندی‌ها (category parameter)
- خواندن ساختار پوشه‌ها از `Content/Books/` و `Content/Broshour/`
- **فایل جدید**: `backend/doctors/urls.py`
- **به‌روزرسانی**: `backend/ispp_project/urls.py` - اضافه کردن route برای doctors

### Router Changes

- **فایل**: `frontend/src/router/index.ts`
- اضافه کردن route `/doctors`

### Navigation Changes

- **فایل**: `frontend/src/App.vue`
- اضافه کردن لینک "پزشکان" به navbar

## 3. به‌روزرسانی صفحه انتشارات

### Frontend Changes

- **فایل**: `frontend/src/views/Publications.vue`
- به‌روزرسانی UI با دسته‌بندی‌های جدید:
- خبرنامه‌ها (Newsletters)
- کتابچه کنگره‌ها و همایش‌ها (Congress booklets)
- مجله انجمن (لینک به https://brieflands.com/journals/jcp)
- سایر محصولات (Other products)
- تحقیقات و پژوهش (Research)
- هر دسته به صورت کارت با امکان دسترسی/دانلود

## 4. حذف لینک English از Navbar

### Frontend Changes

- **فایل**: `frontend/src/App.vue`
- حذف خط: `<li class="nav-item"><a class="nav-link" href="/english">{{ $t('nav.english') }}</a></li>`

## 5. سیستم درخواست عضویت با تایید ادمین

### Backend Changes

- **فایل**: `backend/accounts/views.py`
- تغییر `register_view`:
- ایجاد کاربر با `is_active=False` به جای `True`
- عدم login خودکار بعد از ثبت نام
- پیام مناسب به کاربر
- **API جدید**: `approve_member_view(request, user_id)`
- تایید کاربر (set `is_active=True`)
- **API جدید**: `reject_member_view(request, user_id)`
- رد کاربر (حذف یا mark as rejected)
- **API جدید**: `pending_members_view(request)`
- لیست کاربران در انتظار تایید (`is_active=False`)
- **فایل**: `backend/accounts/urls.py`
- اضافه کردن routes:
- `members/pending/` - لیست درخواست‌ها
- `members/<int:user_id>/approve/` - تایید
- `members/<int:user_id>/reject/` - رد
- **Migration**: ایجاد migration برای اطمینان از `is_active=False` برای کاربران جدید

### Frontend Changes

- **فایل**: `frontend/src/App.vue`
- اضافه کردن تب "درخواست عضویت" به modal لاگین
- فرم درخواست عضویت (مشابه Register.vue اما با پیام انتظار تایید)
- بعد از submit، نمایش پیام "در انتظار تایید مدیریت"
- **فایل**: `frontend/src/views/Dashboard.vue`
- اضافه کردن تب جدید "درخواست‌های عضویت" برای ادمین‌ها