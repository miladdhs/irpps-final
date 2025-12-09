# 🔧 رفع مشکل اتصال به دیتابیس MySQL

## ⚠️ مشکل: Can't connect to MySQL server on 'mysql'

این خطا زمانی رخ می‌دهد که:
- Django سعی می‌کند به hostname `mysql` متصل شود
- اما `mysql` فقط در Docker network کار می‌کند
- وقتی از خارج Docker اجرا می‌کنید، باید از `localhost` استفاده کنید

---

## ✅ راه حل 1: استفاده از Environment Variable موقت

```bash
# در سرور، قبل از اجرای کامند:
export DB_HOST=localhost

# حالا کامند را اجرا کنید:
cd /opt/irpps/src/backend
python3 manage.py inspect_database
```

---

## ✅ راه حل 2: بررسی و تغییر فایل .env

```bash
# بررسی فایل .env
cat /opt/irpps/src/backend/.env

# اگر DB_HOST=mysql است، تغییر دهید:
nano /opt/irpps/src/backend/.env
```

در فایل `.env` باید این باشد:
```env
DB_HOST=localhost
```

نه:
```env
DB_HOST=mysql
```

---

## ✅ راه حل 3: اجرای کامند با Environment Variable

```bash
cd /opt/irpps/src/backend

# اجرا با DB_HOST=localhost
DB_HOST=localhost python3 manage.py inspect_database

# یا برای import:
DB_HOST=localhost python3 manage.py import_content_from_json --author-id 1
```

---

## ✅ راه حل 4: بررسی تنظیمات Docker vs Direct

### برای Docker (docker-compose):
```env
DB_HOST=mysql
```

### برای اجرای مستقیم در سرور:
```env
DB_HOST=localhost
```

---

## 📋 دستورات کامل برای سرور شما

```bash
# 1. رفتن به پوشه backend
cd /opt/irpps/src/backend

# 2. فعال کردن venv (اگر نیست)
source venv/bin/activate

# 3. تنظیم DB_HOST برای اجرای مستقیم
export DB_HOST=localhost

# 4. بررسی دیتابیس
python3 manage.py inspect_database

# 5. وارد کردن محتوا
python3 manage.py import_content_from_json --author-id 1
```

---

## 🔍 بررسی وضعیت MySQL

```bash
# بررسی اینکه MySQL در حال اجرا است
docker ps | grep mysql

# بررسی اتصال به MySQL
mysql -h localhost -u fjjedatu_newdbb -p fjjedatu_newdbb

# یا اگر از Docker استفاده می‌کنید:
docker exec -it irpps-mysql-1 mysql -u fjjedatu_newdbb -p fjjedatu_newdbb
```

---

## 💡 راه حل دائمی: ایجاد دو فایل .env

### 1. `.env.docker` (برای Docker):
```env
DB_HOST=mysql
DB_NAME=fjjedatu_newdbb
DB_USER=fjjedatu_newdbb
DB_PASSWORD=fjjedatu_newdbb
DB_PORT=3306
```

### 2. `.env.local` (برای اجرای مستقیم):
```env
DB_HOST=localhost
DB_NAME=fjjedatu_newdbb
DB_USER=fjjedatu_newdbb
DB_PASSWORD=fjjedatu_newdbb
DB_PORT=3306
```

### استفاده:
```bash
# برای Docker (در docker-compose.yaml):
env_file:
  - .env.docker

# برای اجرای مستقیم:
cp .env.local .env
```

---

## 🎯 راه حل سریع (توصیه می‌شود)

```bash
cd /opt/irpps/src/backend

# تنظیم موقت برای این session
export DB_HOST=localhost

# اجرای کامند
python3 manage.py inspect_database
python3 manage.py import_content_from_json --author-id 1
```

---

**تاریخ ایجاد**: 1403/10/18

