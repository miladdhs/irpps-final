# راهنمای سریع اجرای دستور add_new_events

## 🚀 روش سریع (روی سرور)

```bash
cd /opt/irpps/src/backend
chmod +x run_add_events_docker.sh
./run_add_events_docker.sh
```

این ساده‌ترین روش است و همه چیز را خودکار انجام می‌دهد.

---

## 📋 روش‌های دیگر

### روی سرور (خارج از Docker)
```bash
cd /opt/irpps/src/backend
chmod +x run_add_events_server.sh
./run_add_events_server.sh
```

### روی PC محلی (با SSH Tunnel)
```bash
# ترمینال 1: ایجاد تونل SSH
ssh -L 3307:localhost:3306 root@api.irpps.org

# ترمینال 2: اجرای اسکریپت
cd backend
cp .env.local.example .env.local
# ویرایش .env.local و وارد کردن اطلاعات
chmod +x run_add_events_local.sh
./run_add_events_local.sh
```

---

## ⚠️ نکته مهم

اگر خطای "Can't connect to MySQL server on 'mysql'" می‌گیرید، از `run_add_events_docker.sh` استفاده کنید.

برای جزئیات بیشتر، فایل `SCRIPTS_README.md` را مطالعه کنید.

