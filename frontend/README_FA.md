# 🎨 دیزاین جدید سایت انجمن علمی ریه کودکان ایران

## 📖 معرفی

این پروژه شامل تبدیل کامل UI سایت از دیزاین قدیمی به دیزاین مدرن و حرفه‌ای با استفاده از **Tailwind CSS** و **Material Design 3** است.

## ✨ ویژگی‌های دیزاین جدید

### 🎨 طراحی
- **مدرن و حرفه‌ای**: استفاده از اصول Material Design 3
- **Glassmorphism**: افکت‌های شیشه‌ای و blur
- **انیمیشن‌های روان**: Smooth transitions و hover effects
- **رنگ‌بندی یکپارچه**: پالت رنگ آبی (#137fec) به عنوان رنگ اصلی

### 📱 Responsive Design
- **موبایل**: بهینه‌سازی کامل برای صفحات کوچک
- **تبلت**: Layout مناسب برای صفحات متوسط
- **دسکتاپ**: استفاده کامل از فضای صفحه بزرگ

### 🌙 Dark Mode
- پشتیبانی کامل از تم تاریک
- تغییر خودکار رنگ‌ها
- حفظ خوانایی در هر دو حالت

### ⚡ Performance
- بهینه‌سازی شده برای سرعت بالا
- Lazy loading برای تصاویر
- Code splitting برای بهبود زمان بارگذاری

## 🚀 نصب و راه‌اندازی

### پیش‌نیازها
- Node.js 16 یا بالاتر
- npm یا yarn

### مرحله 1: نصب پکیج‌ها

```bash
cd frontend
npm install
```

### مرحله 2: نصب Tailwind CSS

```bash
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
```

### مرحله 3: اجرای اسکریپت نصب

**برای Windows:**
```powershell
.\install-new-design.ps1
```

**برای Linux/Mac:**
```bash
chmod +x install-new-design.sh
./install-new-design.sh
```

### مرحله 4: اجرای پروژه

```bash
npm run dev
```

سایت در آدرس `http://localhost:5173` در دسترس خواهد بود.

## 📁 ساختار فایل‌ها

```
frontend/
├── src/
│   ├── assets/
│   │   └── tailwind.css          # استایل‌های Tailwind
│   ├── views/
│   │   ├── HomeNew.vue           # صفحه اصلی جدید ✅
│   │   ├── AboutNew.vue          # درباره ما جدید ✅
│   │   ├── NewsNew.vue           # اخبار جدید ✅
│   │   ├── EventsNew.vue         # رویدادها جدید ✅
│   │   ├── ServicesNew.vue       # خدمات جدید ✅
│   │   └── ...
│   ├── AppNew.vue                # Layout اصلی جدید ✅
│   └── main.ts                   # Entry point
├── tailwind.config.js            # تنظیمات Tailwind
├── postcss.config.js             # تنظیمات PostCSS
├── install-new-design.ps1        # اسکریپت نصب Windows
├── install-new-design.sh         # اسکریپت نصب Linux/Mac
├── NEW_DESIGN_MIGRATION.md       # راهنمای کامل مهاجرت
├── QUICK_START.md                # راهنمای سریع
├── IMPLEMENTATION_SUMMARY.md     # خلاصه پیاده‌سازی
└── README_FA.md                  # این فایل
```

## 🎯 صفحات پیاده‌سازی شده

### ✅ کامل شده:
1. **Home** - صفحه اصلی با Hero، Stats، Services
2. **About** - درباره ما با Mission، Vision، Skills، Founders
3. **News** - اخبار با Sidebar، Categories، Search
4. **Events** - رویدادها با Tabs، Filters، Cards
5. **Services** - خدمات با Grid Layout و CTA
6. **App Layout** - Header و Footer مدرن

### ⏳ در انتظار تبدیل:
7. EventDetail - جزئیات رویداد
8. NewsDetail - جزئیات خبر
9. History - تاریخچه
10. Gallery - گالری تصاویر
11. Board Pages - صفحات هیئت مدیره
12. Contact - تماس با ما
13. Team - تیم ما
14. Dashboard - داشبورد

## 🎨 راهنمای استفاده از Tailwind

### کلاس‌های رنگ:
```html
<!-- رنگ اصلی -->
<div class="bg-primary text-white">محتوا</div>

<!-- رنگ‌های خاکستری -->
<div class="bg-slate-100 text-slate-900">محتوا</div>

<!-- Dark mode -->
<div class="bg-white dark:bg-slate-900">محتوا</div>
```

### کلاس‌های Layout:
```html
<!-- Container -->
<div class="max-w-7xl mx-auto px-4">محتوا</div>

<!-- Grid -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  <div>آیتم 1</div>
  <div>آیتم 2</div>
  <div>آیتم 3</div>
</div>

<!-- Flex -->
<div class="flex items-center justify-between gap-4">
  <div>چپ</div>
  <div>راست</div>
</div>
```

### کلاس‌های Typography:
```html
<!-- عناوین -->
<h1 class="text-4xl font-black">عنوان اصلی</h1>
<h2 class="text-3xl font-bold">عنوان فرعی</h2>

<!-- متن -->
<p class="text-lg leading-relaxed">متن عادی</p>
<p class="text-sm text-slate-500">متن کوچک</p>
```

### Material Icons:
```html
<span class="material-symbols-outlined">home</span>
<span class="material-symbols-outlined text-primary text-4xl">favorite</span>
```

## 🔧 تنظیمات

### تغییر رنگ اصلی:
در فایل `tailwind.config.js`:
```javascript
colors: {
  'primary': '#137fec',  // رنگ دلخواه خود را قرار دهید
}
```

### اضافه کردن فونت جدید:
در فایل `src/assets/tailwind.css`:
```css
@import url('https://fonts.googleapis.com/css2?family=YourFont&display=swap');
```

سپس در `tailwind.config.js`:
```javascript
fontFamily: {
  'display': ['YourFont', 'sans-serif'],
}
```

## 🌐 چندزبانه (i18n)

### ساختار فایل ترجمه:
```javascript
// src/i18n/locales/fa.json
{
  "nav": {
    "home": "خانه",
    "about": "درباره ما",
    "services": "خدمات"
  },
  "home": {
    "title": "انجمن علمی ریه کودکان ایران",
    "subtitle": "پیشرو در ارائه خدمات تخصصی"
  }
}
```

### استفاده در کامپوننت:
```vue
<template>
  <h1>{{ $t('home.title') }}</h1>
</template>
```

## 🐛 رفع مشکلات

### مشکل 1: Tailwind کار نمی‌کند
**راه حل:**
```bash
# پاک کردن cache
rm -rf node_modules .nuxt dist
npm install
npm run dev
```

### مشکل 2: فونت‌ها نمایش داده نمی‌شوند
**راه حل:**
- اتصال اینترنت را بررسی کنید
- VPN را روشن کنید (برای دسترسی به Google Fonts)

### مشکل 3: Dark Mode کار نمی‌کند
**راه حل:**
در `tailwind.config.js` مطمئن شوید:
```javascript
darkMode: 'class',
```

### مشکل 4: Material Icons نمایش داده نمی‌شوند
**راه حل:**
در `index.html` این خط را اضافه کنید:
```html
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
```

## 📚 منابع مفید

### مستندات:
- [Tailwind CSS](https://tailwindcss.com/docs)
- [Vue 3](https://vuejs.org/)
- [Material Symbols](https://fonts.google.com/icons)
- [TypeScript](https://www.typescriptlang.org/)

### ابزارها:
- [Vue DevTools](https://devtools.vuejs.org/)
- [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)

## 🤝 مشارکت

برای مشارکت در پروژه:
1. فایل‌های HTML موجود در `UI/` را مطالعه کنید
2. آن‌ها را به فرمت Vue تبدیل کنید
3. از الگوی فایل‌های موجود پیروی کنید
4. تست کنید و Pull Request ارسال کنید

## 📝 چک‌لیست تبدیل صفحات

برای تبدیل هر صفحه HTML به Vue:

- [ ] کپی کردن HTML از فایل `code.html`
- [ ] تبدیل `<a href="#">` به `<router-link to="/">`
- [ ] جایگزینی متن‌های ثابت با `{{ $t('key') }}`
- [ ] اضافه کردن `<script setup lang="ts">`
- [ ] تست Responsive در موبایل، تبلت، دسکتاپ
- [ ] تست Dark Mode
- [ ] بررسی Performance
- [ ] تست در مرورگرهای مختلف

## 🎉 نتیجه

با اجرای این مراحل، شما یک سایت کاملاً مدرن، responsive و حرفه‌ای خواهید داشت که:
- ✅ سرعت بالا
- ✅ UX عالی
- ✅ کد تمیز و قابل نگهداری
- ✅ SEO بهینه
- ✅ Accessibility کامل

---

**ساخته شده با ❤️ برای انجمن علمی ریه کودکان ایران**
