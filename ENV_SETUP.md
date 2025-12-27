# راهنمای تنظیم فایل‌های Environment

## ⚠️ مهم: قبل از اجرا

قبل از اجرای `docker-compose up`، باید فایل‌های `.env` را تنظیم کنید.

---

## 1. فایل `.env` در root پروژه

در root پروژه (همان جایی که `docker-compose.yaml` است)، فایل `.env` ایجاد کنید:

```bash
# در root پروژه
touch .env
nano .env
```

محتوای فایل `.env`:

```env
# Database Configuration (برای docker-compose)
DB_NAME=irporg_DB
DB_USER=irporg_admin
DB_PASSWORD=your-strong-password-here
MYSQL_ROOT_PASSWORD=your-strong-root-password-here
MYSQL_PORT=3306

# Debug Mode (برای production باید False باشد)
DEBUG=False
```

---

## 2. فایل `.env` در پوشه backend

در پوشه `backend`، فایل `.env` ایجاد کنید:

```bash
# در پوشه backend
cd backend
cp env.example.txt .env
nano .env
```

محتوای فایل `backend/.env`:

```env
# Django Settings
DEBUG=False
SECRET_KEY=your-very-long-and-secure-secret-key-here-minimum-50-characters
ALLOWED_HOSTS=api.irpps.org,irpps.org,www.irpps.org,your-server-ip

# Database Configuration
DB_NAME=irporg_DB
DB_USER=irporg_admin
DB_PASSWORD=your-strong-password-here
DB_HOST=mysql
DB_PORT=3306

# MySQL Root Password (باید با MYSQL_ROOT_PASSWORD در root/.env یکسان باشد)
MYSQL_ROOT_PASSWORD=your-strong-root-password-here
```

### 🔑 تولید SECRET_KEY

برای تولید یک SECRET_KEY امن، می‌توانید از دستور زیر استفاده کنید:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

یا:

```bash
python backend/generate_secret_key.py
```

---

## 3. نکات مهم

### ✅ امنیت

1. **هرگز** فایل `.env` را در Git commit نکنید
2. از پسوردهای قوی استفاده کنید (حداقل 16 کاراکتر)
3. `SECRET_KEY` باید یک رشته تصادفی و طولانی باشد
4. در production، `DEBUG` باید `False` باشد

### ✅ هماهنگی فایل‌ها

مقادیر زیر باید در هر دو فایل `.env` یکسان باشند:
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `MYSQL_ROOT_PASSWORD`

### ✅ ALLOWED_HOSTS

در `backend/.env`، `ALLOWED_HOSTS` باید شامل:
- دامنه‌های شما (مثلاً `irpps.org`)
- IP سرور شما (اگر از IP استفاده می‌کنید)
- `localhost` (برای تست محلی)

مثال:
```env
ALLOWED_HOSTS=irpps.org,www.irpps.org,api.irpps.org,185.123.45.67
```

---

## 4. بررسی تنظیمات

بعد از تنظیم فایل‌ها، بررسی کنید:

```bash
# بررسی فایل root/.env
cat .env

# بررسی فایل backend/.env
cat backend/.env
```

---

## 5. مثال کامل

### root/.env
```env
DB_NAME=irporg_DB
DB_USER=irporg_admin
DB_PASSWORD=MyStr0ng!P@ssw0rd2024
MYSQL_ROOT_PASSWORD=MyStr0ng!R00tP@ssw0rd2024
MYSQL_PORT=3306
DEBUG=False
```

### backend/.env
```env
DEBUG=False
SECRET_KEY=django-insecure-abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ
ALLOWED_HOSTS=irpps.org,www.irpps.org,api.irpps.org,185.123.45.67
DB_NAME=irporg_DB
DB_USER=irporg_admin
DB_PASSWORD=MyStr0ng!P@ssw0rd2024
DB_HOST=mysql
DB_PORT=3306
MYSQL_ROOT_PASSWORD=MyStr0ng!R00tP@ssw0rd2024
```

---

## 6. بعد از تنظیم

بعد از تنظیم فایل‌های `.env`، می‌توانید پروژه را اجرا کنید:

```bash
docker-compose up -d --build
```

---

## 7. عیب‌یابی

اگر خطای مربوط به database connection دریافت کردید:

1. بررسی کنید که `DB_HOST=mysql` در `backend/.env` باشد
2. بررسی کنید که پسوردها در هر دو فایل یکسان باشند
3. بررسی کنید که `DB_NAME` و `DB_USER` در هر دو فایل یکسان باشند

اگر خطای `ALLOWED_HOSTS` دریافت کردید:

1. دامنه یا IP خود را به `ALLOWED_HOSTS` اضافه کنید
2. فایل را ذخیره کنید
3. کانتینر backend را restart کنید: `docker-compose restart backend`

