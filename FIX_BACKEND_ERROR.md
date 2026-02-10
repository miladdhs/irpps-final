# 🔧 رفع خطای Backend - rest_framework

## ❌ مشکل:
```
ModuleNotFoundError: No module named 'rest_framework'
```

## ✅ راه‌حل:

### گزینه 1: Rebuild با requirements جدید (توصیه می‌شه)

```bash
cd /opt/irpps/src

# توقف همه سرویس‌ها
docker compose down

# Rebuild backend با --no-cache
docker compose build --no-cache backend

# شروع مجدد
docker compose up -d

# بررسی لاگ
docker logs irpps-backend -f
```

### گزینه 2: نصب دستی در کانتینر (موقت)

```bash
# ورود به کانتینر
docker exec -it irpps-backend bash

# نصب djangorestframework
pip install djangorestframework==3.14.0

# خروج
exit

# Restart backend
docker compose restart backend
```

### گزینه 3: اگر هنوز کار نکرد

```bash
# حذف کامل و rebuild
docker compose down
docker rmi irpps-backend
docker compose build --no-cache backend
docker compose up -d
```

---

## 📝 تغییرات انجام شده:

1. ✅ `djangorestframework==3.14.0` به `requirements.txt` اضافه شد
2. ✅ `services` app موقتاً غیرفعال شد تا سیستم بالا بیاد
3. ✅ بعد از نصب rest_framework، می‌تونیم services رو فعال کنیم

---

## 🚀 مراحل کامل (بعد از رفع مشکل):

### مرحله 1: بالا آوردن سیستم
```bash
cd /opt/irpps/src
docker compose down
docker compose build --no-cache backend
docker compose up -d
```

### مرحله 2: فعال کردن Services App

بعد از اینکه backend بالا اومد، این فایل‌ها رو آپدیت کن:

**backend/ispp_project/settings.py:**
```python
INSTALLED_APPS = [
    # ...
    'services',  # Uncomment this line
]
```

**backend/ispp_project/urls.py:**
```python
urlpatterns = [
    # ...
    path('api/services/', include('services.urls')),  # Uncomment this line
]
```

### مرحله 3: Migration و اضافه کردن داده

```bash
# ایجاد migration
docker exec -it irpps-backend python manage.py makemigrations services

# اجرای migration
docker exec -it irpps-backend python manage.py migrate

# اضافه کردن خدمات
docker exec -it irpps-backend python /app/add_services.py

# Restart
docker compose restart backend
```

---

## ✅ بررسی نهایی

```bash
# چک کردن وضعیت
docker ps

# چک کردن لاگ
docker logs irpps-backend --tail 50

# تست API
curl http://localhost:8000/api/

# تست سایت
curl -I http://localhost
```

---

## 🎯 نتیجه نهایی

بعد از اجرای این مراحل:
- ✅ Backend با موفقیت start می‌شه
- ✅ rest_framework نصب شده
- ✅ Services app آماده فعال‌سازی هست
- ✅ سایت کامل کار می‌کنه
