#!/bin/bash
# اسکریپت سریع برای بررسی دیتابیس - فقط backend را اجرا می‌کند

set -e

WORK_DIR="/opt/irpps/src"
MODEL="${1:-all}"  # پیش‌فرض: all

cd "$WORK_DIR"

echo "📦 اجرای backend container..."
docker compose up -d backend mysql

echo "⏳ منتظر آماده شدن MySQL..."
sleep 5

echo "🔍 بررسی دیتابیس..."
docker compose exec -T backend python3 manage.py inspect_database --model "$MODEL"

echo ""
echo "🛑 متوقف کردن container..."
docker compose stop backend mysql

echo "✅ انجام شد!"

