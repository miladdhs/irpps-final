# 🔧 رفع مشکل Dashboard - Build جدید

## مشکل

Dashboard قدیمی (DashboardOld.vue) در حال اجراست چون:
1. Frontend build نشده
2. فایل‌های قدیمی در container هستند

**خطاهای مشاهده شده:**
```
api/accounts/update-resume/ → 404 (باید profile/resume/update/ باشد)
Axios error (Dashboard جدید از fetch استفاده می‌کند)
```

---

## ✅ راه‌حل: Build و Deploy مجدد

### مرحله 1: توقف containers
```bash
cd /opt/irpps/src
docker compose down
```

### مرحله 2: پاک کردن images قدیمی
```bash
docker rmi irpps-frontend irpps-backend
```

### مرحله 3: Build مجدد (بدون cache)
```bash
docker compose build --no-cache
```

### مرحله 4: اجرای containers
```bash
docker compose up -d
```

### مرحله 5: بررسی وضعیت
```bash
docker compose ps
```

باید همه containers "healthy" باشند.

### مرحله 6: مشاهده logs
```bash
# Frontend logs
docker logs irpps-frontend --tail 50

# Backend logs
docker logs irpps-backend --tail 50
```

---

## 🧪 تست Dashboard جدید

بعد از build:

1. **پاک کردن Cache مرورگر:**
   - F12 → Application → Storage → Clear site data
   - یا Ctrl+Shift+Delete

2. **Refresh صفحه:**
   - Ctrl+F5 (Hard refresh)

3. **لاگین مجدد:**
   - به `/login` بروید
   - لاگین کنید
   - به `/dashboard` بروید

4. **تست عملکرد:**
   - کلیک روی "رزومه و توضیحات" → Modal باز شود
   - کلیک روی "افزودن عکس" → Modal باز شود
   - کلیک روی "ویرایش" → فرم inline باز شود

---

## 🔍 بررسی Dashboard جدید

### در Console (F12):
```javascript
// باید fetch ببینید نه axios
// URL ها باید به این شکل باشند:
/api/accounts/profile/
/api/accounts/profile/update/
/api/accounts/profile/image/upload/
/api/accounts/profile/resume/update/
```

### در Network Tab:
- فیلتر روی "Fetch/XHR"
- باید درخواست‌های fetch ببینید
- URL ها باید با `/api/accounts/profile/` شروع شوند

---

## ⚠️ نکات مهم

### 1. Build کامل انجام شود
```bash
# اگر build سریع تمام شد، احتمالاً cache استفاده کرده
# حتماً از --no-cache استفاده کنید:
docker compose build --no-cache
```

### 2. Container های قدیمی پاک شوند
```bash
# لیست تمام containers
docker ps -a

# اگر container های stopped دیدید، پاکشان کنید:
docker rm irpps-frontend irpps-backend irpps-mysql
```

### 3. Volume ها حفظ شوند
```bash
# Volume های MySQL و media حفظ می‌شوند
# نگران از دست رفتن داده نباشید
docker volume ls
```

---

## 📋 چک‌لیست نهایی

بعد از build و deploy:

- [ ] همه containers "healthy" هستند
- [ ] Frontend logs خطا ندارد
- [ ] Backend logs خطا ندارد
- [ ] صفحه Dashboard باز می‌شود
- [ ] Modal "رزومه و توضیحات" باز می‌شود
- [ ] Modal "افزودن عکس" باز می‌شود
- [ ] فرم "ویرایش اطلاعات" باز می‌شود
- [ ] در Console خطای 404 نیست
- [ ] در Network Tab URL های صحیح هستند

---

## 🎯 دستورات کامل (یکجا)

```bash
# توقف و پاک کردن
cd /opt/irpps/src
docker compose down
docker rmi irpps-frontend irpps-backend

# Build و اجرا
docker compose build --no-cache
docker compose up -d

# بررسی
docker compose ps
docker logs irpps-frontend --tail 50
docker logs irpps-backend --tail 50
```

بعد از اجرا:
1. Cache مرورگر را پاک کنید (Ctrl+Shift+Delete)
2. صفحه را Hard Refresh کنید (Ctrl+F5)
3. دوباره لاگین کنید
4. به Dashboard بروید و تست کنید

---

## 🚀 انتظار می‌رود

بعد از این مراحل:
- ✅ Dashboard جدید با Modal ها کار می‌کند
- ✅ URL های API صحیح هستند
- ✅ خطای 404 برطرف می‌شود
- ✅ آپلود عکس کار می‌کند
- ✅ ویرایش رزومه کار می‌کند

