# راهنمای مهاجرت به دیزاین جدید

## مراحل انجام شده:

### 1. نصب و پیکربندی Tailwind CSS
- ✅ فایل `tailwind.config.js` ایجاد شد
- ✅ فایل `postcss.config.js` ایجاد شد  
- ✅ فایل `src/assets/tailwind.css` ایجاد شد
- ✅ فایل `main.ts` آپدیت شد

### 2. فایل‌های نمونه ایجاد شده:
- ✅ `AppNew.vue` - Header و Footer جدید با دیزاین مدرن
- ✅ `HomeNew.vue` - صفحه اصلی با دیزاین جدید

## مراحل باقی‌مانده:

### 3. نصب پکیج‌های مورد نیاز:
```bash
cd frontend
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
npm install
```

### 4. تبدیل فایل‌های باقی‌مانده:

#### فایل‌های اولویت‌دار:
1. **About.vue** - از `UI/درباره_ما_-_انجمن_علمی_ریه_کودکان/code.html`
2. **News.vue** - از `UI/اخبار_و_مقالات_علمی/code.html`
3. **Events.vue** - از `UI/رویدادها_و_کنگره‌ها/code.html`
4. **EventDetail.vue** - از `UI/جزئیات_رویداد_و_ثبت‌نام/code.html`
5. **Services.vue** - از `UI/خدمات_و_فعالیت‌های_انجمن/code.html`
6. **NewsDetail.vue** - از `UI/جزئیات_خبر_و_مقاله/code.html`
7. **History.vue** - از `UI/تاریخچه_فعالیت‌ها/code.html`
8. **Gallery.vue** - از `UI/گالری_تصاویر_انجمن/code.html`
9. **BoardFirst.vue** - از `UI/هیئت_مدیره_دوره_اول/code.html`

### 5. نکات مهم برای تبدیل:

#### الگوی تبدیل HTML به Vue:
```vue
<template>
  <!-- محتوای HTML را اینجا قرار دهید -->
  <!-- تگ‌های <a href="#"> را به <router-link to="/"> تبدیل کنید -->
  <!-- متن‌های ثابت را با {{ $t('key') }} جایگزین کنید -->
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
// import های مورد نیاز
</script>

<style scoped>
/* استایل‌های اختصاصی در صورت نیاز */
</style>
```

#### تبدیل کلاس‌های Tailwind:
- کلاس‌های Tailwind را همان‌طور که هستند نگه دارید
- `dir="rtl"` را حذف کنید (در App.vue تنظیم شده)
- `lang="fa"` را حذف کنید

#### تبدیل لینک‌ها:
```html
<!-- قبل -->
<a href="#" class="...">متن</a>

<!-- بعد -->
<router-link to="/" class="...">{{ $t('nav.home') }}</router-link>
```

#### تبدیل تصاویر:
```html
<!-- قبل -->
<img src="https://..." alt="..." />

<!-- بعد -->
<img src="/img/image-name.svg" :alt="$t('alt.imageName')" />
```

### 6. فعال‌سازی دیزاین جدید:

#### روش 1: جایگزینی تدریجی
```bash
# نام فایل‌های قدیمی را تغییر دهید
mv src/App.vue src/AppOld.vue
mv src/views/Home.vue src/views/HomeOld.vue

# نام فایل‌های جدید را تغییر دهید
mv src/AppNew.vue src/App.vue
mv src/views/HomeNew.vue src/views/Home.vue
```

#### روش 2: تست موازی
در `router/index.ts`:
```typescript
import HomeNew from '../views/HomeNew.vue';

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/new', name: 'home-new', component: HomeNew }, // تست
  // ...
];
```

### 7. اضافه کردن Material Symbols Icons:

در `index.html`:
```html
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
```

### 8. تنظیمات i18n:

کلیدهای جدید مورد نیاز در فایل‌های ترجمه:
```javascript
{
  nav: {
    search: 'جستجو...',
    services: 'خدمات',
    // ...
  },
  home: {
    stat1: 'متخصص ریه',
    stat2: 'بیمار تحت پوشش',
    stat3: 'انتشارات علمی',
    stat4: 'جایزه بین‌المللی',
    // ...
  },
  about: {
    verifiedBy: 'تایید شده توسط',
    ministry: 'وزارت بهداشت و درمان',
    // ...
  }
}
```

### 9. تست و بررسی:

```bash
# اجرای پروژه
npm run dev

# بررسی موارد زیر:
- [ ] Header و Navigation کار می‌کند
- [ ] Footer نمایش داده می‌شود
- [ ] Responsive است (موبایل، تبلت، دسکتاپ)
- [ ] Dark mode کار می‌کند
- [ ] لینک‌ها به درستی کار می‌کنند
- [ ] تصاویر نمایش داده می‌شوند
- [ ] فرم‌ها کار می‌کنند
- [ ] انیمیشن‌ها روان هستند
```

### 10. بهینه‌سازی نهایی:

- حذف فایل‌های CSS قدیمی که دیگر استفاده نمی‌شوند
- حذف فایل‌های قدیمی با پسوند `Old.vue`
- بررسی و حذف import های غیرضروری
- کامپایل و تست نهایی

## ساختار فایل‌های UI موجود:

```
frontend/UI/
├── خانه_-_انجمن_علمی_ریه_کودکان_1/code.html ✅ (تبدیل شد به HomeNew.vue)
├── درباره_ما_-_انجمن_علمی_ریه_کودکان/code.html ⏳
├── اخبار_و_مقالات_علمی/code.html ⏳
├── رویدادها_و_کنگره‌ها/code.html ⏳
├── جزئیات_رویداد_و_ثبت‌نام/code.html ⏳
├── خدمات_و_فعالیت‌های_انجمن/code.html ⏳
├── جزئیات_خبر_و_مقاله/code.html ⏳
├── تاریخچه_فعالیت‌ها/code.html ⏳
├── گالری_تصاویر_انجمن/code.html ⏳
└── هیئت_مدیره_دوره_اول/code.html ⏳
```

## نکات امنیتی:

1. همیشه از `getApiUrl()` برای API calls استفاده کنید
2. از `credentials: 'include'` برای authentication استفاده کنید
3. Input validation را فراموش نکنید
4. XSS protection را رعایت کنید

## پشتیبانی:

در صورت بروز مشکل:
1. Console browser را بررسی کنید
2. Network tab را برای API calls چک کنید
3. Tailwind classes را در DevTools بررسی کنید
4. Vue DevTools را نصب و استفاده کنید

---

**توجه**: این دیزاین کاملاً responsive و مدرن است و از بهترین practices Vue 3 + TypeScript + Tailwind CSS استفاده می‌کند.
