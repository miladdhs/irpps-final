# راهنمای اجرای فرانت‌اند روی سیستم محلی

این راهنما به شما کمک می‌کند تا فقط فرانت‌اند پروژه را روی سیستم خودتان اجرا کنید بدون اینکه تغییری در سرور ایجاد شود.

## پیش‌نیازها

1. **Node.js** (نسخه 18 یا بالاتر)
   - دانلود از: https://nodejs.org/
   - بررسی نسخه: `node --version`

2. **npm** (معمولاً با Node.js نصب می‌شود)
   - بررسی نسخه: `npm --version`

## روش 1: اجرای ساده (بدون Docker)

### مرحله 1: نصب Dependencies

```bash
cd frontend
npm install
```

### مرحله 2: تنظیم API URL

فایل `.env.local` را بررسی کنید (اگر وجود ندارد، ایجاد شده است). این فایل به فرانت می‌گوید که به سرور production متصل شود:

```
VITE_API_BASE_URL=https://api.irpps.org
```

### مرحله 3: اجرای فرانت

```bash
npm run dev
```

فرانت روی آدرس زیر اجرا می‌شود:
- **Local:** http://localhost:5173
- **Network:** http://[YOUR_IP]:5173

### توقف سرور

در Terminal، `Ctrl + C` را بزنید.

---

## روش 2: اجرا با Docker (اختیاری)

اگر Docker نصب دارید و می‌خواهید با Docker اجرا کنید:

### مرحله 1: ساخت Dockerfile محلی

فایل `frontend/Dockerfile.local` را ایجاد کنید:

```dockerfile
FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Expose port
EXPOSE 5173

# Run dev server
CMD ["npm", "run", "dev", "--", "--host"]
```

### مرحله 2: ساخت و اجرا

```bash
cd frontend
docker build -f Dockerfile.local -t frontend-local .
docker run -p 5173:5173 --env-file .env.local frontend-local
```

---

## نکات مهم

### اتصال به سرور Production
- فرانت به طور پیش‌فرض به `https://api.irpps.org` متصل می‌شود
- هیچ تغییری در سرور ایجاد نمی‌شود
- تمام API calls به سرور واقعی می‌روند

### تغییر API URL (در صورت نیاز)

اگر می‌خواهید به API دیگری متصل شوید، فایل `.env.local` را ویرایش کنید:

```env
VITE_API_BASE_URL=https://your-api-url.com
```

سپس سرور dev را مجدداً راه‌اندازی کنید.

### Hot Reload
- تغییرات در کد به صورت خودکار اعمال می‌شوند
- نیازی به refresh دستی نیست

### مشکلات رایج

#### خطای Port در حال استفاده
اگر پورت 5173 استفاده شده:
```bash
# Windows
netstat -ano | findstr :5173
taskkill /PID [PID_NUMBER] /F

# Linux/Mac
lsof -ti:5173 | xargs kill -9
```

#### خطای npm install
```bash
# پاک کردن cache
npm cache clean --force

# حذف node_modules و نصب مجدد
rm -rf node_modules package-lock.json
npm install
```

#### خطای CORS
اگر با خطای CORS مواجه شدید، مطمئن شوید که `VITE_API_BASE_URL` در `.env.local` به درستی تنظیم شده است.

---

## بعد از تست موفق

وقتی مطمئن شدید همه چیز درست کار می‌کند:

1. تغییرات را commit کنید
2. به سرور production push کنید
3. سرور به طور خودکار build و deploy می‌شود

**هیچ تغییری در سرور برای تست محلی لازم نیست!**

