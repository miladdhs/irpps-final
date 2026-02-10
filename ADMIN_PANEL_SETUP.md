# راهنمای فعال‌سازی پنل مدیریت

## مشکل
یوزر `admin` وارد سایت شده ولی دسترسی به پنل مدیریت اخبار، اطلاعیه‌ها و رویدادها رو نداره.

## علت
برای دسترسی به پنل مدیریت، یوزر باید `is_staff = True` باشه.

## راه‌حل

### روش 1: اجرای اسکریپت روی سرور (توصیه می‌شه)

1. به سرور SSH کنید
2. به پوشه backend بروید:
```bash
cd /path/to/your/project/backend
```

3. اسکریپت رو اجرایی کنید:
```bash
chmod +x make_user_staff_server.sh
```

4. اسکریپت رو اجرا کنید:
```bash
./make_user_staff_server.sh admin
```

یا اگر می‌خواید یوزر دیگه‌ای رو staff کنید:
```bash
./make_user_staff_server.sh username
```

### روش 2: استفاده از Django Shell

1. به سرور SSH کنید
2. به پوشه backend بروید
3. Django shell رو باز کنید:
```bash
python3 manage.py shell
```

4. کدهای زیر رو اجرا کنید:
```python
from django.contrib.auth import get_user_model

User = get_user_model()

# پیدا کردن یوزر admin
user = User.objects.get(username='admin')

# تبدیل به staff
user.is_staff = True
user.is_active = True
user.save()

print(f"✓ User {user.username} is now staff!")
print(f"is_staff: {user.is_staff}")
print(f"is_active: {user.is_active}")
```

5. از shell خارج شوید:
```python
exit()
```

### روش 3: استفاده از Django Admin Panel

اگر یک superuser دارید:

1. به آدرس `/admin/` بروید
2. وارد شوید با یوزر superuser
3. به بخش Users بروید
4. یوزر `admin` رو پیدا کنید
5. چک‌باکس `Staff status` رو فعال کنید
6. ذخیره کنید

## بعد از فعال‌سازی

بعد از اینکه یوزر `admin` رو staff کردید:

1. از سایت خارج شوید (Logout)
2. دوباره وارد شوید
3. حالا در پنل کاربری باید این بخش‌ها رو ببینید:
   - **مدیریت اخبار**: افزودن، ویرایش و حذف اخبار
   - **مدیریت اطلاعیه‌ها**: افزودن، ویرایش و حذف اطلاعیه‌ها
   - **مدیریت رویدادها**: افزودن، ویرایش و حذف رویدادها
   - **مدیریت اعضا**: تایید و رد درخواست‌های عضویت

## دسترسی به پنل مدیریت

بعد از فعال‌سازی، می‌تونید از این آدرس‌ها استفاده کنید:

- **پنل اصلی مدیریت**: `/admin`
- **مدیریت اخبار**: `/admin/news`
- **مدیریت اطلاعیه‌ها**: `/admin/announcements`
- **مدیریت رویدادها**: `/admin/events`
- **مدیریت اعضا**: `/admin/members`

## توضیحات تکمیلی

### تفاوت is_staff و is_superuser

- **is_staff**: دسترسی به پنل مدیریت فرانت‌اند (اخبار، رویدادها، اطلاعیه‌ها)
- **is_superuser**: دسترسی کامل به Django Admin Panel و تمام بخش‌ها

### امنیت

- فقط به افرادی که واقعاً نیاز دارند دسترسی `is_staff` بدید
- برای مدیران ارشد از `is_superuser` استفاده کنید
- رمزهای عبور قوی استفاده کنید

## عیب‌یابی

### اگر بعد از فعال‌سازی هنوز پنل مدیریت رو نمی‌بینید:

1. مطمئن شوید که از سایت خارج شدید و دوباره وارد شدید
2. Cache مرورگر رو پاک کنید
3. بررسی کنید که یوزر `is_active = True` هم هست:
```bash
python3 manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(username='admin')
print(f"is_staff: {user.is_staff}")
print(f"is_active: {user.is_active}")
```

### اگر خطای Permission Denied می‌گیرید:

مطمئن شوید که:
- یوزر `is_staff = True` هست
- یوزر `is_active = True` هست
- از سایت خارج شدید و دوباره وارد شدید

## پشتیبانی

اگر مشکلی داشتید، لاگ‌های سرور رو بررسی کنید:
```bash
# Backend logs
tail -f backend/logs/django.log

# Docker logs (اگر از Docker استفاده می‌کنید)
docker logs irpps-backend
```
