# 🚀 دستورات نصب و اجرا

## مشکل حل شد! ✅

فایل‌های زیر ایجاد شدند:
- ✅ `package.json` - تنظیمات npm
- ✅ `vite.config.ts` - تنظیمات Vite
- ✅ `tsconfig.json` - تنظیمات TypeScript
- ✅ `tsconfig.node.json` - تنظیمات TypeScript برای Node
- ✅ `index.html` - فایل HTML اصلی

---

## مراحل نصب:

### مرحله 1: پاک کردن node_modules قدیمی
```powershell
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
```

### مرحله 2: نصب پکیج‌ها
```powershell
npm install
```

### مرحله 3: نصب Tailwind CSS
```powershell
npm install -D tailwindcss postcss autoprefixer
```

### مرحله 4: اجرای پروژه
```powershell
npm run dev
```

---

## اگر خطا داد:

### خطای ENOENT یا Cannot find module:
```powershell
# پاک کردن کامل
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json

# نصب مجدد
npm cache clean --force
npm install
```

### خطای Permission Denied:
```powershell
# اجرا با دسترسی Administrator
# یا
npm install --legacy-peer-deps
```

### خطای Vite:
```powershell
npm install -D vite @vitejs/plugin-vue
```

---

## دستورات کامل (کپی-پیست):

```powershell
# پاک کردن فایل‌های قدیمی
Remove-Item -Recurse -Force node_modules -ErrorAction SilentlyContinue
Remove-Item package-lock.json -ErrorAction SilentlyContinue

# نصب پکیج‌ها
npm install

# نصب Tailwind
npm install -D tailwindcss postcss autoprefixer

# اجرا
npm run dev
```

---

## بعد از نصب موفق:

سایت در آدرس زیر در دسترس خواهد بود:
```
http://localhost:5173/
```

دیزاین جدید:
```
http://localhost:5173/new
```

---

## نکات مهم:

1. ✅ Node.js نسخه 16 یا بالاتر نصب باشد
2. ✅ npm نسخه 8 یا بالاتر نصب باشد
3. ✅ اتصال اینترنت برای دانلود پکیج‌ها
4. ✅ فضای کافی روی دیسک (حدود 500MB)

---

## بررسی نسخه‌ها:

```powershell
node --version   # باید 16 یا بالاتر باشد
npm --version    # باید 8 یا بالاتر باشد
```

---

**موفق باشید! 🎉**
