# 🐳 راهنمای اجرای کامندها در Docker

## ✅ دستورات صحیح

### استفاده از `docker compose` (بدون خط تیره):

```bash
# رفتن به پوشه root پروژه
cd /opt/irpps/src

# بررسی وضعیت containers
docker compose ps

# اجرای کامند inspect_database
docker compose exec backend python3 manage.py inspect_database

# اجرای کامند import_content_from_json
docker compose exec backend python3 manage.py import_content_from_json --author-id 1
```

---

## 📋 دستورات کامل

### 1. بررسی دیتابیس:
```bash
cd /opt/irpps/src
docker compose exec backend python3 manage.py inspect_database
```

### 2. وارد کردن محتوا:
```bash
cd /opt/irpps/src
docker compose exec backend python3 manage.py import_content_from_json --author-id 1
```

### 3. بررسی فقط اخبار:
```bash
docker compose exec backend python3 manage.py inspect_database --model news
```

### 4. بررسی به صورت JSON:
```bash
docker compose exec backend python3 manage.py inspect_database --format json
```

---

## 🔧 عیب‌یابی

### خطا: "env file not found"
اگر خطای `env file /opt/irpps/src/src/backend/.env not found` می‌گیرید:

1. بررسی کنید که فایل `.env` در `/opt/irpps/src/backend/.env` وجود دارد
2. مسیر در `docker-compose.yaml` باید `./backend/.env` باشد (نه `./src/backend/.env`)

### خطا: "DB_PASSWORD variable is not set"
اگر warning می‌گیرید:

1. بررسی کنید که در فایل `.env` مقدار `DB_PASSWORD` تنظیم شده است
2. بعد از تغییر `.env`، containers را restart کنید:
   ```bash
   docker compose restart backend
   ```

---

## 🚀 مثال کامل

```bash
# 1. رفتن به پوشه root
cd /opt/irpps/src

# 2. بررسی وضعیت
docker compose ps

# 3. بررسی دیتابیس
docker compose exec backend python3 manage.py inspect_database

# 4. وارد کردن محتوا
docker compose exec backend python3 manage.py import_content_from_json --author-id 1

# 5. بررسی نتیجه
docker compose exec backend python3 manage.py inspect_database --model news
```

---

**نکته**: در Docker جدید، از `docker compose` (بدون خط تیره) استفاده کنید، نه `docker-compose`.

