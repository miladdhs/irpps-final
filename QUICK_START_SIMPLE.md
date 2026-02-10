# راهنمای سریع اجرای پروژه

## وضعیت فعلی

✅ **MySQL**: در حال اجرا با Docker  
✅ **Frontend**: در حال اجرا روی http://localhost:5174  
❌ **Backend**: نیاز به اجرا دارد

## مشکل

Backend نمیتونه به MySQL داخل Docker وصل بشه چون MySQL فقط از داخل Docker network قابل دسترسیه.

## راه حل: اجرای Backend با Docker

### گزینه 1: اجرای همه چیز با Docker (توصیه میشه)

```powershell
# توقف سرویس‌های فعلی
docker-compose down

# اجرای همه سرویس‌ها
docker-compose up -d

# مشاهده لاگ‌ها
docker-compose logs -f
```

بعد از اجرا:
- Frontend: http://localhost:80
- Backend: http://localhost:8000
- MySQL: داخل Docker network

### گزینه 2: اجرای Backend داخل Docker، Frontend local

```powershell
# اجرای MySQL و Backend
docker-compose up -d mysql backend

# در ترمینال جدید - اجرای Frontend
cd frontend
npm run dev
```

بعد از اجرا:
- Frontend: http://localhost:5174
- Backend: http://localhost:8000
- MySQL: داخل Docker network

### گزینه 3: فقط MySQL با Docker، بقیه local (پیچیده‌تر)

برای این کار باید:
1. کاربر MySQL رو برای localhost تنظیم کنی
2. یا از `127.0.0.1` به جای `localhost` استفاده کنی

```powershell
# اتصال به MySQL
docker-compose exec mysql mysql -u root -p
# Password: tHPXArRfwrX3WH!*j

# ایجاد کاربر برای localhost
CREATE USER 'irporg_admin'@'%' IDENTIFIED BY 'tHPXArRfwrX3WH!*j';
GRANT ALL PRIVILEGES ON irporg_DB.* TO 'irporg_admin'@'%';
FLUSH PRIVILEGES;
EXIT;
```

بعد از این کار میتونی Backend رو local اجرا کنی.

## توصیه من

از **گزینه 1** استفاده کن - همه چیز با Docker اجرا بشه. ساده‌تر و مطمئن‌تره.

## دستورات مفید

```powershell
# مشاهده وضعیت
docker-compose ps

# مشاهده لاگ‌ها
docker-compose logs -f backend
docker-compose logs -f mysql

# ری‌استارت یک سرویس
docker-compose restart backend

# توقف همه
docker-compose down

# پاک کردن همه چیز (با احتیاط!)
docker-compose down -v
```

## اگر میخوای فقط روی Frontend کار کنی

```powershell
# اجرای Backend و MySQL با Docker
docker-compose up -d mysql backend

# Frontend رو local اجرا کن
cd frontend
npm run dev
```

این بهترین حالته برای توسعه Frontend!
