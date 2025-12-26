# راهنمای سریع اجرای فرانت روی سیستم محلی

## روش ساده (بدون Docker) ⚡

### 1. نصب Dependencies
```bash
cd frontend
npm install
```

### 2. اجرا
```bash
npm run dev
```

### 3. باز کردن مرورگر
- به آدرس زیر بروید: **http://localhost:5173**

---

## نکته مهم 🔑

فرانت به صورت خودکار به سرور production (`https://api.irpps.org`) متصل می‌شود.

اگر می‌خواهید API URL را تغییر دهید، فایل `.env.local` را ویرایش کنید:
```env
VITE_API_BASE_URL=https://api.irpps.org
```

---

## توقف سرور
در Terminal: `Ctrl + C`

---

## بعد از تست موفق ✅

وقتی مطمئن شدید همه چیز درست کار می‌کند، تغییرات را commit و push کنید.
هیچ تغییری در سرور لازم نیست!

