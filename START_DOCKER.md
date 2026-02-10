# راهنمای اجرای Docker و دیتابیس

## مرحله 1: اجرای Docker Desktop

Docker نصب هست ولی Docker Desktop باید اجرا بشه:

1. **Windows**: از Start Menu برو به `Docker Desktop` و اجراش کن
2. منتظر بمون تا Docker Desktop کاملاً بالا بیاد (آیکون Docker در System Tray سبز بشه)
3. بعد از اجرا، این دستور رو تست کن:
   ```bash
   docker ps
   ```

## مرحله 2: اجرای کانتینرها

بعد از اینکه Docker Desktop اجرا شد، این دستورات رو اجرا کن:

### گزینه 1: اجرای فقط MySQL (توصیه میشه)
```bash
docker-compose up -d mysql
```

این فقط MySQL رو اجرا میکنه و backend و frontend رو نه.

### گزینه 2: اجرای همه سرویس‌ها
```bash
docker-compose up -d
```

این همه سرویس‌ها رو اجرا میکنه (MySQL + Backend + Frontend)

## مرحله 3: چک کردن وضعیت

```bash
# مشاهده کانتینرهای در حال اجرا
docker-compose ps

# مشاهده لاگ‌ها
docker-compose logs -f mysql

# چک کردن MySQL
docker-compose exec mysql mysql -u irporg_admin -p irporg_DB
# Password: tHPXArRfwrX3WH!*j
```

## مرحله 4: اجرای Backend به صورت Local (بدون Docker)

اگر فقط MySQL رو با Docker اجرا کردی، میتونی Backend رو به صورت local اجرا کنی:

```bash
cd backend

# نصب dependencies
pip install -r requirements.txt

# اجرای migrations
python manage.py migrate

# اجرای سرور
python manage.py runserver 0.0.0.0:8000
```

## مرحله 5: اجرای Frontend به صورت Local

```bash
cd frontend

# نصب dependencies (اگر نصب نکردی)
npm install

# اجرای dev server
npm run dev
```

## پورت‌ها

- **Frontend**: http://localhost:5174 (development) یا http://localhost:80 (Docker)
- **Backend**: http://localhost:8000
- **MySQL**: localhost:3306 (اگر پورت رو uncomment کنی در docker-compose.yaml)

## دستورات مفید Docker

```bash
# متوقف کردن همه سرویس‌ها
docker-compose down

# متوقف کردن و حذف volumes
docker-compose down -v

# ری‌استارت یک سرویس
docker-compose restart mysql

# مشاهده لاگ‌های یک سرویس
docker-compose logs -f backend

# اجرای دستور در کانتینر
docker-compose exec backend python manage.py migrate
docker-compose exec mysql mysql -u root -p
```

## اتصال به MySQL از خارج Docker

اگر میخوای از خارج Docker به MySQL وصل بشی (مثلاً با MySQL Workbench):

1. در `docker-compose.yaml` این خطوط رو uncomment کن:
   ```yaml
   ports:
     - "3306:3306"
   ```

2. ری‌استارت کن:
   ```bash
   docker-compose restart mysql
   ```

3. اطلاعات اتصال:
   - Host: `localhost`
   - Port: `3306`
   - User: `irporg_admin`
   - Password: `tHPXArRfwrX3WH!*j`
   - Database: `irporg_DB`

## توجه

- فایل‌های Docker تغییر نکردم
- دیتابیس موجود در پوشه `mysql/` حفظ میشه
- اگر فقط میخوای روی کد کار کنی، بهتره فقط MySQL رو با Docker اجرا کنی و Backend/Frontend رو local اجرا کنی
