# راهنمای رفع مشکل Cookie و CORS

## مشکل
بعد از لاگین، کاربر به صفحه Home ریدایرکت می‌شود و خطای `TypeError: Failed to fetch` نمایش داده می‌شود.

## علت
کوکی‌های Session به دلیل تنظیمات نادرست در درخواست‌های cross-origin ارسال نمی‌شوند.

## راه‌حل اعمال شده
تنظیمات Cookie در `backend/ispp_project/settings.py` اصلاح شد.

## مراحل بعدی (روی سرور)

### 1. بررسی وضعیت Container ها
```bash
cd /opt/irpps
docker ps
```

### 2. Restart کردن Backend
```bash
docker-compose restart backend
```

### 3. بررسی لاگ‌های Backend (اگر هنوز مشکل دارید)
```bash
docker-compose logs backend
```

یا برای دیدن لاگ‌های زنده:
```bash
docker-compose logs -f backend
```

### 4. اگر Backend راه‌اندازی نمی‌شود
```bash
# بررسی خطاهای syntax
docker-compose logs backend | tail -50

# یا rebuild کامل
docker-compose down
docker-compose up -d --build
```

## تست کردن

### 1. لاگین کنید
- به سایت `https://irpps.org` بروید
- لاگین کنید

### 2. بررسی Cookie در مرورگر
1. DevTools را باز کنید (F12)
2. به تب **Application** بروید
3. در سمت چپ، **Cookies** → **https://irpps.org** را انتخاب کنید
4. باید یک کوکی به نام `sessionid` ببینید با این مشخصات:
   - **Domain**: `.irpps.org`
   - **Secure**: ✓ (تیک خورده)
   - **SameSite**: `None`

### 3. اگر Cookie وجود ندارد
- Backend را restart کنید
- Cache مرورگر را پاک کنید
- دوباره لاگین کنید

## اگر هنوز مشکل دارید

### بررسی لاگ‌های Backend
```bash
docker-compose logs backend | grep -i error
```

### بررسی تنظیمات Environment
```bash
docker exec irpps-backend-1 cat /app/.env
```

### تست دستی API
```bash
# از داخل container
docker exec -it irpps-backend-1 python manage.py shell
```

## نکات مهم

1. **همیشه بعد از تغییر settings.py باید backend را restart کنید**
2. **Cookie ها فقط روی HTTPS کار می‌کنند** (Secure=True)
3. **Domain باید با نقطه شروع شود** (`.irpps.org` نه `irpps.org`)

