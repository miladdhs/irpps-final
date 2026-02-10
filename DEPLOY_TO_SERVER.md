# دستورات دیپلوی تغییرات به سرور

## مرحله 1: آپلود فایل‌های تغییر یافته به سرور

فایل‌های زیر باید به سرور آپلود شوند:

```
frontend/src/views/Contact.vue
frontend/src/App.vue
frontend/src/views/Home.vue
frontend/public/img/about us.webp
```

### با استفاده از SCP یا FTP:

```bash
# مثال با SCP (از کامپیوتر لوکال)
scp "frontend/src/views/Contact.vue" root@srv9461186756:/opt/irpps/src/frontend/src/views/
scp "frontend/src/App.vue" root@srv9461186756:/opt/irpps/src/frontend/src/
scp "frontend/src/views/Home.vue" root@srv9461186756:/opt/irpps/src/frontend/src/views/
scp "frontend/public/img/about us.webp" root@srv9461186756:/opt/irpps/src/frontend/public/img/
```

## مرحله 2: اتصال به سرور

```bash
ssh root@srv9461186756
```

## مرحله 3: رفتن به پوشه پروژه

```bash
cd /opt/irpps/src
```

## مرحله 4: ریبیلد داکر

```bash
# متوقف کردن کانتینرها
docker compose down

# حذف ایمیج‌های قدیمی
docker rmi irpps-frontend irpps-backend

# ریبیلد بدون کش
docker compose build --no-cache

# اجرای کانتینرها
docker compose up -d
```

## مرحله 5: چک کردن لاگ‌ها

```bash
# چک کردن وضعیت کانتینرها
docker compose ps

# دیدن لاگ‌های فرانت‌اند
docker compose logs frontend

# دیدن لاگ‌های بک‌اند
docker compose logs backend
```

## مرحله 6: تست در مرورگر

1. پاک کردن کش مرورگر: `Ctrl+Shift+Delete`
2. Hard Refresh: `Ctrl+F5`
3. چک کردن تغییرات:
   - صفحه تماس: فرم حذف شده، فقط FAQ
   - نوبار: لینک "اعضا" اضافه شده، سرچ حذف شده
   - فوتر: "راهنمای سایت" و "پرسش‌های متداول" حذف شده
   - صفحه اصلی: تصویر "about us.webp" در بخش درباره ما

---

## راه حل سریع‌تر: استفاده از Git

اگر پروژه روی Git هست:

```bash
# روی لوکال
git add .
git commit -m "UI cleanup: removed form, added team link, removed search, updated footer"
git push

# روی سرور
cd /opt/irpps/src
git pull
docker compose down
docker rmi irpps-frontend irpps-backend
docker compose build --no-cache
docker compose up -d
```

---

## نکات مهم:

1. **حتماً** ایمیج‌های قدیمی رو حذف کن (`docker rmi`)
2. **حتماً** با `--no-cache` ریبیلد کن
3. بعد از ریبیلد، کش مرورگر رو پاک کن
4. اگر باز هم تغییری ندیدی، چک کن که فایل‌ها درست آپلود شدن
