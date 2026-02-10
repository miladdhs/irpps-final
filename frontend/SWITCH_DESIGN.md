# 🔄 راهنمای جابجایی بین دیزاین قدیم و جدید

## وضعیت فعلی:

✅ **دیزاین قدیمی شما حفظ شده و از بین نرفته است!**

همه فایل‌های قدیمی شما همچنان موجود هستند:
- `src/App.vue` (قدیمی)
- `src/views/Home.vue` (قدیمی)
- `src/views/About.vue` (قدیمی)
- و بقیه...

فایل‌های جدید با پسوند `New` ایجاد شده‌اند:
- `src/AppNew.vue` (جدید)
- `src/views/HomeNew.vue` (جدید)
- `src/views/AboutNew.vue` (جدید)
- و بقیه...

---

## 🎯 سه روش برای استفاده:

### روش 1️⃣: تست دیزاین جدید بدون تغییر قدیمی (پیشنهادی)

**مزایا:**
- ✅ دیزاین قدیمی دست نخورده باقی می‌ماند
- ✅ می‌توانید هر دو را مقایسه کنید
- ✅ در صورت مشکل، راحت برمی‌گردید

**نحوه استفاده:**
```bash
# اجرای پروژه
npm run dev

# دیزاین قدیمی:
http://localhost:5173/

# دیزاین جدید:
http://localhost:5173/new
http://localhost:5173/new/about
http://localhost:5173/new/news
http://localhost:5173/new/events
http://localhost:5173/new/services
```

**این روش الان فعال است!** ✅

---

### روش 2️⃣: جایگزینی کامل با دیزاین جدید (با بکاپ)

اگر از دیزاین جدید راضی بودید و می‌خواهید آن را به عنوان دیزاین اصلی استفاده کنید:

**Windows PowerShell:**
```powershell
cd frontend

# بکاپ فایل‌های قدیمی
Copy-Item src/App.vue src/AppOld.vue
Copy-Item src/views/Home.vue src/views/HomeOld.vue
Copy-Item src/views/About.vue src/views/AboutOld.vue
Copy-Item src/views/News.vue src/views/NewsOld.vue
Copy-Item src/views/Events.vue src/views/EventsOld.vue
Copy-Item src/views/Services.vue src/views/ServicesOld.vue

# فعال‌سازی دیزاین جدید
Copy-Item src/AppNew.vue src/App.vue -Force
Copy-Item src/views/HomeNew.vue src/views/Home.vue -Force
Copy-Item src/views/AboutNew.vue src/views/About.vue -Force
Copy-Item src/views/NewsNew.vue src/views/News.vue -Force
Copy-Item src/views/EventsNew.vue src/views/Events.vue -Force
Copy-Item src/views/ServicesNew.vue src/views/Services.vue -Force
```

**Linux/Mac:**
```bash
cd frontend

# بکاپ فایل‌های قدیمی
cp src/App.vue src/AppOld.vue
cp src/views/Home.vue src/views/HomeOld.vue
cp src/views/About.vue src/views/AboutOld.vue
cp src/views/News.vue src/views/NewsOld.vue
cp src/views/Events.vue src/views/EventsOld.vue
cp src/views/Services.vue src/views/ServicesOld.vue

# فعال‌سازی دیزاین جدید
cp src/AppNew.vue src/App.vue
cp src/views/HomeNew.vue src/views/Home.vue
cp src/views/AboutNew.vue src/views/About.vue
cp src/views/NewsNew.vue src/views/News.vue
cp src/views/EventsNew.vue src/views/Events.vue
cp src/views/ServicesNew.vue src/views/Services.vue
```

---

### روش 3️⃣: برگشت به دیزاین قدیمی

اگر دیزاین جدید را فعال کردید و می‌خواهید به قدیمی برگردید:

**Windows PowerShell:**
```powershell
cd frontend

# بازگشت به دیزاین قدیمی
Copy-Item src/AppOld.vue src/App.vue -Force
Copy-Item src/views/HomeOld.vue src/views/Home.vue -Force
Copy-Item src/views/AboutOld.vue src/views/About.vue -Force
Copy-Item src/views/NewsOld.vue src/views/News.vue -Force
Copy-Item src/views/EventsOld.vue src/views/Events.vue -Force
Copy-Item src/views/ServicesOld.vue src/views/Services.vue -Force
```

**Linux/Mac:**
```bash
cd frontend

# بازگشت به دیزاین قدیمی
cp src/AppOld.vue src/App.vue
cp src/views/HomeOld.vue src/views/Home.vue
cp src/views/AboutOld.vue src/views/About.vue
cp src/views/NewsOld.vue src/views/News.vue
cp src/views/EventsOld.vue src/views/Events.vue
cp src/views/ServicesOld.vue src/views/Services.vue
```

---

## 📊 مقایسه دیزاین‌ها:

### دیزاین قدیمی:
- ✅ آشنا و تست شده
- ✅ تمام صفحات کامل
- ⚠️ ظاهر قدیمی‌تر
- ⚠️ کمتر responsive

### دیزاین جدید:
- ✅ مدرن و حرفه‌ای
- ✅ کاملاً responsive
- ✅ Dark mode
- ✅ انیمیشن‌های روان
- ✅ Material Design 3
- ⚠️ برخی صفحات هنوز تبدیل نشده

---

## 🗂️ ساختار فایل‌ها:

```
frontend/src/
├── App.vue                    # دیزاین قدیمی (فعال در /)
├── AppNew.vue                 # دیزاین جدید (فعال در /new)
├── AppOld.vue                 # بکاپ (بعد از جایگزینی)
│
└── views/
    ├── Home.vue               # قدیمی (/)
    ├── HomeNew.vue            # جدید (/new)
    ├── HomeOld.vue            # بکاپ
    │
    ├── About.vue              # قدیمی (/about)
    ├── AboutNew.vue           # جدید (/new/about)
    ├── AboutOld.vue           # بکاپ
    │
    └── ... (بقیه فایل‌ها)
```

---

## ✅ چک‌لیست تصمیم‌گیری:

قبل از جایگزینی کامل، این موارد را بررسی کنید:

- [ ] دیزاین جدید را در `/new` تست کردم
- [ ] در موبایل، تبلت و دسکتاپ بررسی کردم
- [ ] Dark mode را تست کردم
- [ ] تمام لینک‌ها کار می‌کنند
- [ ] فرم‌ها و API ها کار می‌کنند
- [ ] تصاویر به درستی نمایش داده می‌شوند
- [ ] از تیم بازخورد گرفتم
- [ ] بکاپ از فایل‌های قدیمی گرفتم

---

## 🆘 کمک سریع:

### چطور دیزاین جدید را ببینم؟
```
http://localhost:5173/new
```

### چطور به دیزاین قدیمی برگردم؟
```
http://localhost:5173/
```

### چطور هر دو را همزمان ببینم؟
دو تب مرورگر باز کنید:
- تب 1: `http://localhost:5173/` (قدیمی)
- تب 2: `http://localhost:5173/new` (جدید)

---

## 📞 پشتیبانی:

اگر مشکلی پیش آمد:
1. فایل‌های `*Old.vue` را نگه دارید
2. همیشه می‌توانید با کپی کردن آن‌ها برگردید
3. Git را برای version control استفاده کنید

---

**نکته مهم:** همیشه قبل از تغییرات بزرگ، از Git استفاده کنید:

```bash
git add .
git commit -m "Backup before switching to new design"
```

این کار اطمینان می‌دهد که همیشه می‌توانید به نسخه قبلی برگردید! 🔒
