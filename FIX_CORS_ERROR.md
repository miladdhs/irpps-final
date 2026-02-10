# 🔧 رفع خطای CORS

## ❌ مشکل:
```
Access to fetch at 'https://api.irpps.org/api/accounts/members/' from origin 'http://localhost:5173' 
has been blocked by CORS policy
```

## ✅ راه‌حل انجام شده:

### تغییرات در `backend/ispp_project/settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "https://irpps.org",
    "https://www.irpps.org",
    "https://api.irpps.org",
    # Local development
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:5173",      # ✅ اضافه شد
    "http://127.0.0.1:5173",      # ✅ اضافه شد
]
```

---

## 🚀 اعمال تغییرات در سرور:

### روش 1: Rebuild Backend (توصیه می‌شه)

```bash
cd /opt/irpps/src

# Rebuild backend
docker compose build backend

# Restart
docker compose restart backend

# بررسی لاگ
docker logs irpps-backend --tail 50
```

### روش 2: Restart ساده (اگر فایل‌ها sync شدن)

```bash
cd /opt/irpps/src

# فقط restart
docker compose restart backend

# بررسی
docker logs irpps-backend --tail 20
```

---

## 🧪 تست CORS

### از مرورگر:
1. باز کردن Developer Tools (F12)
2. رفتن به Console
3. اجرای این کد:

```javascript
fetch('https://api.irpps.org/api/accounts/members/')
  .then(res => res.json())
  .then(data => console.log('✅ CORS کار می‌کنه:', data))
  .catch(err => console.error('❌ خطا:', err));
```

### از Terminal:

```bash
# تست با curl
curl -I https://api.irpps.org/api/accounts/members/

# باید این header رو ببینی:
# Access-Control-Allow-Origin: http://localhost:5173
```

---

## 📝 نکات مهم:

### 1. Development vs Production

**Development (localhost:5173):**
- ✅ حالا اضافه شده
- برای توسعه محلی

**Production (irpps.org):**
- ✅ قبلاً اضافه شده بود
- برای سایت اصلی

### 2. اگر هنوز کار نکرد:

#### الف) چک کردن تنظیمات Django:

```bash
docker exec -it irpps-backend python manage.py shell

# در shell:
from django.conf import settings
print(settings.CORS_ALLOWED_ORIGINS)
# باید localhost:5173 رو ببینی
```

#### ب) فعال کردن CORS برای همه (فقط برای تست):

در `settings.py` موقتاً این رو اضافه کن:

```python
CORS_ALLOW_ALL_ORIGINS = True  # ⚠️ فقط برای تست!
```

بعد از تست، حتماً حذفش کن و از لیست CORS_ALLOWED_ORIGINS استفاده کن.

#### ج) بررسی Nginx (اگر از Nginx استفاده می‌کنی):

```nginx
# در nginx.conf باید این header ها باشه:
add_header 'Access-Control-Allow-Origin' '$http_origin' always;
add_header 'Access-Control-Allow-Credentials' 'true' always;
add_header 'Access-Control-Allow-Methods' 'GET, POST, PUT, DELETE, OPTIONS' always;
add_header 'Access-Control-Allow-Headers' 'Accept,Authorization,Cache-Control,Content-Type,DNT,If-Modified-Since,Keep-Alive,Origin,User-Agent,X-Requested-With' always;
```

---

## 🎯 بررسی نهایی:

بعد از اعمال تغییرات:

1. ✅ Backend restart شده
2. ✅ CORS برای localhost:5173 فعال شده
3. ✅ صفحه Team بدون خطا لود می‌شه
4. ✅ لیست اعضا نمایش داده می‌شه

---

## 🔍 Debug اضافی:

اگر هنوز مشکل داری، این اطلاعات رو بفرست:

```bash
# 1. لاگ backend
docker logs irpps-backend --tail 100

# 2. تنظیمات CORS
docker exec -it irpps-backend python -c "from django.conf import settings; print(settings.CORS_ALLOWED_ORIGINS)"

# 3. تست API
curl -H "Origin: http://localhost:5173" -I https://api.irpps.org/api/accounts/members/
```
