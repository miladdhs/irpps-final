# 🧪 تست API Endpoints

## مشکل احتمالی: عدم لاگین

اگر 404 می‌گیرید، احتمالاً به این دلایل است:

### 1. **لاگین نکرده‌اید**
API های زیر نیاز به لاگین دارند:
- `/api/accounts/profile/`
- `/api/accounts/profile/update/`
- `/api/accounts/profile/image/upload/`
- `/api/accounts/profile/image/delete/`
- `/api/accounts/profile/resume/update/`

### 2. **Session منقضی شده**
اگر قبلاً لاگین کرده بودید ولی backend restart شده، session از بین رفته.

### 3. **CORS یا Cookie مشکل دارد**
Browser نمی‌تونه cookie های session رو ارسال کنه.

---

## 🔍 تست‌های لازم

### تست 1: بررسی Backend
```bash
# در سرور اجرا کنید:
docker logs irpps-backend --tail 50
```

باید ببینید که backend بدون خطا راه‌اندازی شده.

### تست 2: تست API بدون لاگین
```bash
curl http://localhost:8000/api/accounts/members/
```

این باید کار کنه چون نیاز به لاگین نداره.

### تست 3: تست لاگین
```bash
curl -X POST http://localhost:8000/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"YOUR_USERNAME","password":"YOUR_PASSWORD"}' \
  -c cookies.txt
```

### تست 4: تست Profile با Session
```bash
curl http://localhost:8000/api/accounts/profile/ \
  -b cookies.txt
```

---

## 🔧 راه‌حل‌های احتمالی

### راه‌حل 1: مطمئن شوید لاگین کرده‌اید
1. به صفحه Login بروید
2. با کد ملی و کد نظام پزشکی لاگین کنید
3. بعد به Dashboard بروید

### راه‌حل 2: پاک کردن Cache و Cookie
1. F12 را بزنید
2. Application → Storage → Clear site data
3. صفحه را Refresh کنید
4. دوباره لاگین کنید

### راه‌حل 3: بررسی Network Tab
1. F12 را بزنید
2. به تب Network بروید
3. فیلتر را روی "Fetch/XHR" بگذارید
4. عملیات را انجام دهید (مثلاً آپلود عکس)
5. ببینید دقیقاً چه URL ای صدا زده می‌شود و چه خطایی می‌دهد

---

## 📋 چک‌لیست دیباگ

- [ ] Backend container در حال اجراست: `docker ps | grep backend`
- [ ] Backend بدون خطا راه‌اندازی شده: `docker logs irpps-backend`
- [ ] لاگین کرده‌اید
- [ ] Cookie ها ذخیره شده‌اند (F12 → Application → Cookies)
- [ ] URL های API درست هستند
- [ ] CORS تنظیم شده (در settings.py)

---

## 🎯 URL های صحیح

مطمئن شوید که Dashboard از این URL ها استفاده می‌کند:

```javascript
// دریافت پروفایل
GET /api/accounts/profile/

// به‌روزرسانی اطلاعات شخصی
PUT /api/accounts/profile/update/

// آپلود عکس
POST /api/accounts/profile/image/upload/

// حذف عکس
DELETE /api/accounts/profile/image/delete/

// به‌روزرسانی رزومه
POST /api/accounts/profile/resume/update/
```

---

## 💡 نکته مهم

اگر در Console این پیام را می‌بینید:
```
Failed to load resource: the server responded with a status of 404
```

**احتمالاً یکی از این مشکلات است:**

1. **لاگین نکرده‌اید** → برگردید و لاگین کنید
2. **URL اشتباه است** → بررسی کنید که Dashboard از URL های بالا استفاده می‌کند
3. **Backend خطا دارد** → لاگ backend را چک کنید

---

## 🚨 اگر هنوز کار نکرد

لطفاً این اطلاعات را بفرستید:

1. **لاگ Backend:**
   ```bash
   docker logs irpps-backend --tail 100
   ```

2. **لاگ Frontend:**
   ```bash
   docker logs irpps-frontend --tail 50
   ```

3. **Screenshot از Network Tab** (F12 → Network)
   - فیلتر روی XHR/Fetch
   - کلیک روی درخواست 404
   - تب Headers و Response را نشان دهید

4. **Screenshot از Console** (F12 → Console)
   - تمام خطاها را نشان دهید

