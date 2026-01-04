# راهنمای استفاده از اسکریپت‌های اجرای دستورات

این اسکریپت‌ها برای اجرای دستور `add_new_events` و سایر دستورات Django در شرایط مختلف طراحی شده‌اند.

## اسکریپت‌های موجود

### 1. `run_add_events_docker.sh` (پیشنهادی برای سرور)
**ساده‌ترین روش برای اجرا روی سرور**

این اسکریپت دستور را داخل کانتینر Docker اجرا می‌کند که در آن hostname `mysql` به درستی کار می‌کند.

**استفاده:**
```bash
cd /opt/irpps/src/backend
chmod +x run_add_events_docker.sh
./run_add_events_docker.sh
```

**مزایا:**
- ساده و بدون نیاز به تنظیمات اضافی
- استفاده از تنظیمات docker-compose.yaml
- اتصال خودکار به MySQL

---

### 2. `run_add_events_server.sh` (اجرا روی سرور خارج از Docker)
**برای زمانی که می‌خواهید دستور را خارج از Docker اجرا کنید**

این اسکریپت IP کانتینر MySQL را پیدا می‌کند و متغیرهای محیطی را تنظیم می‌کند.

**استفاده:**
```bash
cd /opt/irpps/src/backend
chmod +x run_add_events_server.sh
./run_add_events_server.sh
```

**نیازمندی‌ها:**
- کانتینر MySQL باید در حال اجرا باشد
- Python3 و PyMySQL باید نصب باشند
- Virtual environment باید فعال باشد (اگر وجود دارد)

**نحوه کار:**
1. پیدا کردن کانتینر MySQL
2. دریافت IP کانتینر از Docker network
3. تنظیم متغیرهای محیطی
4. تست اتصال به دیتابیس
5. اجرای دستور

---

### 3. `run_add_events_local.sh` (اجرا روی PC محلی)
**برای اجرای دستور از PC محلی با اتصال به دیتابیس سرور**

این اسکریپت می‌تواند از SSH Tunnel یا اتصال مستقیم استفاده کند.

**استفاده:**

**مرحله 1: ایجاد فایل تنظیمات**
```bash
cd backend
cp .env.local.example .env.local
# ویرایش .env.local و وارد کردن اطلاعات دیتابیس
```

**مرحله 2: ایجاد SSH Tunnel (پیشنهادی)**
در یک ترمینال جداگانه:
```bash
ssh -L 3307:localhost:3306 root@api.irpps.org
```

**مرحله 3: اجرای اسکریپت**
در ترمینال دیگر:
```bash
cd backend
chmod +x run_add_events_local.sh
./run_add_events_local.sh
```

**تنظیمات .env.local:**
```env
DB_NAME=irporg_DB
DB_USER=irporg_admin
DB_PASSWORD=your-password
DB_HOST=127.0.0.1  # برای SSH Tunnel
DB_PORT=3307       # پورت تونل SSH
```

**گزینه اتصال مستقیم:**
اگر MySQL از خارج قابل دسترسی باشد:
```env
DB_HOST=api.irpps.org
DB_PORT=3306
```

---

## مقایسه روش‌ها

| روش | محل اجرا | پیچیدگی | امنیت | پیشنهاد |
|-----|----------|---------|-------|---------|
| Docker | سرور | ⭐ ساده | ✅ بالا | ⭐⭐⭐⭐⭐ |
| Server Script | سرور | ⭐⭐ متوسط | ✅ بالا | ⭐⭐⭐⭐ |
| Local + SSH Tunnel | PC محلی | ⭐⭐⭐ متوسط | ✅✅ خیلی بالا | ⭐⭐⭐⭐ |
| Local + Direct | PC محلی | ⭐⭐ ساده | ⚠️ نیاز به فایروال | ⭐⭐ |

---

## عیب‌یابی

### خطا: "Can't connect to MySQL server on 'mysql'"
**راه‌حل:** از `run_add_events_docker.sh` استفاده کنید یا `run_add_events_server.sh` را اجرا کنید.

### خطا: "Container MySQL پیدا نشد"
**راه‌حل:** ابتدا کانتینرها را اجرا کنید:
```bash
cd /opt/irpps/src
docker compose up -d mysql backend
```

### خطا: "PyMySQL نصب نشده"
**راه‌حل:** نصب PyMySQL:
```bash
pip install PyMySQL
```

### خطا در SSH Tunnel
**راه‌حل:** 
1. مطمئن شوید تونل SSH در حال اجرا است
2. پورت تونل را در `.env.local` بررسی کنید
3. از `netstat -an | grep 3307` برای بررسی استفاده از پورت استفاده کنید

---

## نکات مهم

1. **امنیت:** هرگز پسورد دیتابیس را در کد commit نکنید
2. **Backup:** قبل از اجرای دستورات مهم، از دیتابیس backup بگیرید
3. **Virtual Environment:** مطمئن شوید virtual environment فعال است
4. **Permissions:** اسکریپت‌ها باید executable باشند: `chmod +x *.sh`

---

## مثال‌های استفاده

### اجرای دستورات دیگر
می‌توانید این اسکریپت‌ها را برای دستورات دیگر هم استفاده کنید:

```bash
# در run_add_events_docker.sh خط آخر را تغییر دهید:
docker compose exec -T backend python manage.py <your-command>
```

یا از اسکریپت‌های موجود استفاده کنید:
```bash
./run_commands_in_docker.sh 'inspect_database'
./run_command_temporary.sh 'your_command'
```

