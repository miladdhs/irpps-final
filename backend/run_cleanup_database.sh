#!/bin/bash

# اسکریپت اجرای تمیزکاری دیتابیس

echo "اجرای اسکریپت تمیزکاری دیتابیس..."

# فعال‌سازی محیط مجازی
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# اجرای اسکریپت Python
python cleanup_database.py

echo "اتمام اجرا"
