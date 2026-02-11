#!/bin/bash

# اسکریپت اجرای add_board_members.py در Docker

echo "اجرای اسکریپت اضافه کردن اعضای هیئت مدیره..."
echo "=========================================="

# اجرا در کانتینر backend
docker-compose exec backend python add_board_members.py

echo ""
echo "اتمام عملیات"
