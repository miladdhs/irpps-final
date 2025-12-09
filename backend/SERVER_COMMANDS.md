# 🖥️ راهنمای اجرای کامندها در سرور لینوکس

## ⚠️ مشکل: ModuleNotFoundError: No module named 'django'

این خطا به این معنی است که:
1. محیط مجازی فعال نیست
2. یا Django نصب نشده است

---

## ✅ راه حل 1: فعال کردن محیط مجازی

### اگر محیط مجازی دارید:

```bash
# پیدا کردن محیط مجازی (معمولاً در یکی از این مسیرها است)
ls -la /opt/irpps/src/backend/venv
ls -la /opt/irpps/src/venv
ls -la ~/venv

# فعال کردن محیط مجازی
source /opt/irpps/src/backend/venv/bin/activate
# یا
source /opt/irpps/src/venv/bin/activate
# یا
source ~/venv/bin/activate

# بعد از فعال شدن، باید (venv) در ابتدای خط فرمان ظاهر شود
# حالا کامند را اجرا کنید:
cd /opt/irpps/src/backend
python3 manage.py inspect_database
```

---

## ✅ راه حل 2: نصب requirements

### اگر محیط مجازی ندارید یا می‌خواهید نصب کنید:

```bash
# رفتن به پوشه backend
cd /opt/irpps/src/backend

# ایجاد محیط مجازی (اگر ندارید)
python3 -m venv venv

# فعال کردن محیط مجازی
source venv/bin/activate

# نصب requirements
pip install -r requirements.txt

# حالا کامند را اجرا کنید:
python3 manage.py inspect_database
```

---

## ✅ راه حل 3: استفاده از Python سیستم (بدون venv)

⚠️ **توصیه نمی‌شود** اما اگر مجبور هستید:

```bash
cd /opt/irpps/src/backend

# نصب Django و requirements
pip3 install -r requirements.txt

# اجرای کامند
python3 manage.py inspect_database
```

---

## 📋 دستورات کامل (مرحله به مرحله)

### مرحله 1: بررسی وضعیت
```bash
# بررسی وجود Python3
python3 --version

# بررسی وجود pip
pip3 --version

# بررسی وجود محیط مجازی
ls -la /opt/irpps/src/backend/ | grep venv
```

### مرحله 2: فعال کردن یا ایجاد محیط مجازی
```bash
cd /opt/irpps/src/backend

# اگر venv وجود دارد:
source venv/bin/activate

# اگر venv وجود ندارد:
python3 -m venv venv
source venv/bin/activate
```

### مرحله 3: نصب requirements
```bash
# اطمینان از فعال بودن venv (باید (venv) در ابتدای خط باشد)
pip install -r requirements.txt
```

### مرحله 4: اجرای کامندها
```bash
# بررسی دیتابیس
python3 manage.py inspect_database

# وارد کردن محتوا
python3 manage.py import_content_from_json --author-id 1
```

---

## 🔍 بررسی فعال بودن محیط مجازی

بعد از `source venv/bin/activate` باید این را ببینید:

```bash
(venv) root@srv9461186756:/opt/irpps/src/backend#
```

اگر `(venv)` را نمی‌بینید، محیط مجازی فعال نشده است.

---

## 🐛 عیب‌یابی

### خطا: "python3: command not found"
```bash
# نصب Python3
apt-get update
apt-get install python3 python3-pip python3-venv
```

### خطا: "pip: command not found"
```bash
# نصب pip
apt-get install python3-pip
```

### خطا: "Permission denied"
```bash
# استفاده از sudo (اگر نیاز باشد)
sudo python3 manage.py inspect_database
```

### خطا: "No module named 'django'"
```bash
# نصب Django
pip install Django==4.2.7
# یا نصب همه requirements
pip install -r requirements.txt
```

---

## 📝 مثال کامل برای سرور شما

```bash
# 1. رفتن به پوشه backend
cd /opt/irpps/src/backend

# 2. فعال کردن محیط مجازی (اگر وجود دارد)
source venv/bin/activate

# 3. اگر venv وجود ندارد، ایجاد کنید:
# python3 -m venv venv
# source venv/bin/activate

# 4. نصب requirements (اگر نصب نشده)
pip install -r requirements.txt

# 5. اجرای کامند
python3 manage.py inspect_database

# 6. وارد کردن محتوا
python3 manage.py import_content_from_json --author-id 1
```

---

## 💡 نکات مهم

1. **همیشه از `python3` استفاده کنید** (نه `python`)
2. **قبل از اجرای کامندها، محیط مجازی را فعال کنید**
3. **اطمینان حاصل کنید که `requirements.txt` نصب شده است**
4. **اگر از cPanel استفاده می‌کنید، ممکن است مسیر venv متفاوت باشد**

---

## 🔗 مسیرهای احتمالی venv در cPanel

```bash
# بررسی مسیرهای مختلف
ls -la /opt/irpps/src/backend/venv
ls -la /opt/irpps/venv
ls -la ~/venv
ls -la /home/username/venv
ls -la /home/username/virtualenv
```

---

**تاریخ ایجاد**: 1403/10/18

