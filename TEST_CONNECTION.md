# تست اتصال Frontend به Backend

این فایل برای تست سریع اتصال فرانت به بکند و دیتابیس است.

## 🧪 تست‌های سریع

### 1. تست Backend API

```bash
# تست health check
curl http://localhost:8000/

# تست لیست اعضا
curl http://localhost:8000/api/accounts/members/

# تست لیست اخبار
curl http://localhost:8000/api/news/

# تست لیست رویدادها
curl http://localhost:8000/api/events/
```

### 2. تست Frontend Proxy

```bash
# تست صفحه اصلی
curl http://localhost:80/

# تست API از طریق nginx proxy
curl http://localhost:80/api/accounts/members/

# تست media files
curl http://localhost:80/media/
```

### 3. تست Login از Frontend

باز کردن Developer Tools در مرورگر (F12) و اجرای:

```javascript
// تست login
fetch('/api/accounts/login/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  credentials: 'include',
  body: JSON.stringify({
    username: 'admin',
    password: 'your_password'
  })
})
.then(r => r.json())
.then(data => console.log(data))

// تست profile (بعد از login)
fetch('/api/accounts/profile/', {
  credentials: 'include'
})
.then(r => r.json())
.then(data => console.log(data))
```

### 4. تست Database Connection

```bash
# اتصال به MySQL
docker-compose exec mysql mysql -u irporg_admin -p irporg_DB

# در MySQL shell:
SHOW TABLES;
SELECT COUNT(*) FROM accounts_customuser;
SELECT id, username, first_name, last_name FROM accounts_customuser LIMIT 5;
```

## ✅ چک‌لیست اتصالات

### Backend به Database
- [ ] Backend می‌تواند به MySQL متصل شود
- [ ] Migrations با موفقیت اجرا شده
- [ ] داده‌ها در دیتابیس ذخیره می‌شوند

### Frontend به Backend
- [ ] Nginx به Backend proxy می‌کند
- [ ] API endpoints در دسترس هستند
- [ ] CORS headers صحیح هستند
- [ ] Cookies ارسال می‌شوند

### Authentication Flow
- [ ] Login کار می‌کند
- [ ] Session cookie ذخیره می‌شود
- [ ] CSRF token صحیح است
- [ ] Profile API کار می‌کند
- [ ] Logout کار می‌کند

### Media Files
- [ ] عکس‌های پروفایل نمایش داده می‌شوند
- [ ] آپلود فایل کار می‌کند
- [ ] Nginx media files را proxy می‌کند

## 🔍 بررسی تنظیمات

### 1. بررسی Environment Variables

```bash
# بررسی متغیرهای backend
docker-compose exec backend env | grep -E "DB_|DEBUG|SECRET_KEY"

# بررسی متغیرهای frontend
docker-compose exec frontend env | grep VITE
```

### 2. بررسی Nginx Config

```bash
# مشاهده تنظیمات nginx
docker-compose exec frontend cat /etc/nginx/conf.d/default.conf

# تست nginx config
docker-compose exec frontend nginx -t
```

### 3. بررسی Django Settings

```bash
# اجرای Django shell
docker-compose exec backend python manage.py shell

# در Django shell:
from django.conf import settings
print(settings.DATABASES)
print(settings.CORS_ALLOWED_ORIGINS)
print(settings.CSRF_TRUSTED_ORIGINS)
```

## 🐛 عیب‌یابی رایج

### خطا: "CSRF token missing or incorrect"

**راه حل:**
1. بررسی کنید `withCredentials: true` در axios تنظیم شده
2. بررسی کنید `CSRF_COOKIE_DOMAIN` صحیح است
3. در مرورگر Cookies را پاک کنید و دوباره login کنید

```javascript
// در Developer Tools > Application > Cookies
// باید csrftoken و sessionid را ببینید
```

### خطا: "CORS policy blocked"

**راه حل:**
1. بررسی کنید دامنه در `CORS_ALLOWED_ORIGINS` وجود دارد
2. بررسی کنید nginx CORS headers را اضافه می‌کند
3. بررسی کنید `CORS_ALLOW_CREDENTIALS = True`

```bash
# تست CORS headers
curl -H "Origin: https://irpps.org" \
     -H "Access-Control-Request-Method: POST" \
     -H "Access-Control-Request-Headers: Content-Type" \
     -X OPTIONS \
     http://localhost:80/api/accounts/login/ \
     -v
```

### خطا: "Database connection failed"

**راه حل:**
1. بررسی کنید MySQL container در حال اجراست
2. بررسی کنید `DB_HOST=mysql` (نام سرویس در docker-compose)
3. بررسی کنید رمز عبور صحیح است

```bash
# تست اتصال از backend به mysql
docker-compose exec backend python manage.py dbshell
```

### خطا: "404 Not Found" برای API

**راه حل:**
1. بررسی کنید nginx proxy صحیح تنظیم شده
2. بررسی کنید backend در حال اجراست
3. بررسی کنید URL صحیح است (`/api/` نه `api/`)

```bash
# تست مستقیم backend
curl http://localhost:8000/api/accounts/members/

# تست از طریق nginx
curl http://localhost:80/api/accounts/members/
```

## 📊 مانیتورینگ Real-time

### Terminal 1: Backend Logs
```bash
docker-compose logs -f backend
```

### Terminal 2: Frontend Logs
```bash
docker-compose logs -f frontend
```

### Terminal 3: Database Logs
```bash
docker-compose logs -f mysql
```

### Terminal 4: Test Commands
```bash
# اجرای تست‌ها
```

## 🎯 تست کامل Flow

### 1. ثبت نام کاربر جدید

1. باز کردن `http://localhost/register`
2. پر کردن فرم ثبت نام
3. ارسال فرم
4. بررسی پیام موفقیت

### 2. تایید کاربر توسط Admin

```bash
# دریافت لیست کاربران در انتظار
curl http://localhost:8000/api/accounts/members/pending/ \
  -H "Cookie: sessionid=YOUR_ADMIN_SESSION"

# تایید کاربر
curl -X POST http://localhost:8000/api/accounts/members/1/approve/ \
  -H "Cookie: sessionid=YOUR_ADMIN_SESSION"
```

### 3. ورود کاربر

1. باز کردن `http://localhost/login`
2. وارد کردن نام کاربری و رمز عبور
3. کلیک روی ورود
4. انتقال به Dashboard

### 4. بروزرسانی پروفایل

1. باز کردن `http://localhost/profile`
2. ویرایش اطلاعات
3. آپلود عکس پروفایل
4. ذخیره تغییرات

### 5. مشاهده اعضا

1. باز کردن `http://localhost/team`
2. بررسی لیست اعضا
3. بررسی نمایش عکس‌های پروفایل

## ✨ نتیجه موفقیت

اگر تمام موارد زیر کار کنند، اتصال موفق است:

✅ Backend به Database متصل است
✅ Frontend به Backend متصل است  
✅ Login/Register کار می‌کند
✅ Dashboard نمایش داده می‌شود
✅ Profile update کار می‌کند
✅ Media files نمایش داده می‌شوند
✅ CORS و CSRF مشکلی ندارند
✅ Cookies صحیح ذخیره می‌شوند

---

**نکته**: برای تست در production، `localhost` را با دامنه واقعی (`irpps.org`) جایگزین کنید.
