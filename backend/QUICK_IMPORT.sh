#!/bin/bash
# اسکریپت سریع برای وارد کردن محتوا - فقط backend را اجرا می‌کند

set -e

WORK_DIR="/opt/irpps/src"
JSON_FILE="/opt/irpps/src/frontend/public/Content/structured_content_complete.json"
AUTHOR_ID="${1:-1}"  # پیش‌فرض: 1

cd "$WORK_DIR"

echo "📦 اجرای backend container..."
docker compose up -d backend mysql

echo "⏳ منتظر آماده شدن MySQL..."
sleep 5

echo "📥 وارد کردن محتوا..."
docker compose exec -T backend python3 manage.py import_content_from_json \
  --file "$JSON_FILE" \
  --author-id "$AUTHOR_ID"

echo ""
echo "✅ بررسی نتیجه..."
docker compose exec -T backend python3 manage.py inspect_database --model news --limit 5

echo ""
echo "🛑 متوقف کردن container..."
docker compose stop backend mysql

echo "✅ انجام شد!"

