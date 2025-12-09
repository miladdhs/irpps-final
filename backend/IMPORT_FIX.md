# 🔧 رفع مشکل import_content_from_json در Docker

## ⚠️ مشکل: File not found

فایل JSON در Docker container پیدا نمی‌شود چون مسیرها متفاوت هستند.

---

## ✅ راه حل 1: استفاده از مسیر کامل (توصیه می‌شود)

```bash
docker exec -it irpps-backend-1 python3 manage.py import_content_from_json \
  --file /opt/irpps/src/frontend/public/Content/structured_content_complete.json \
  --author-id 1
```

---

## ✅ راه حل 2: کپی فایل به داخل Container

```bash
# کپی فایل به داخل container
docker cp /opt/irpps/src/frontend/public/Content/structured_content_complete.json \
  irpps-backend-1:/app/structured_content_complete.json

# اجرای کامند
docker exec -it irpps-backend-1 python3 manage.py import_content_from_json \
  --file /app/structured_content_complete.json \
  --author-id 1
```

---

## ✅ راه حل 3: Mount کردن Volume در docker-compose.yaml

در `docker-compose.yaml`، volume را اضافه کنید:

```yaml
backend:
  volumes:
    - ./backend:/app
    - ./frontend/public/Content:/app/content  # اضافه کنید
```

سپس:
```bash
docker compose restart backend
docker exec -it irpps-backend-1 python3 manage.py import_content_from_json \
  --file /app/content/structured_content_complete.json \
  --author-id 1
```

---

## 📋 دستورات کامل (راه حل 1 - توصیه می‌شود)

```bash
# بررسی وجود فایل در سرور
ls -la /opt/irpps/src/frontend/public/Content/structured_content_complete.json

# اجرای import با مسیر کامل
docker exec -it irpps-backend-1 python3 manage.py import_content_from_json \
  --file /opt/irpps/src/frontend/public/Content/structured_content_complete.json \
  --author-id 1

# بررسی نتیجه
docker exec -it irpps-backend-1 python3 manage.py inspect_database --model news
```

---

## 🔍 بررسی مسیر فایل

```bash
# در سرور
ls -la /opt/irpps/src/frontend/public/Content/structured_content_complete.json

# در container
docker exec -it irpps-backend-1 ls -la /opt/irpps/src/frontend/public/Content/structured_content_complete.json
```

---

**تاریخ ایجاد**: 1403/10/18

