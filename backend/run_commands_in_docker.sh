#!/bin/bash
# اسکریپت اجرای کامندهای Django از داخل Docker container
# این اسکریپت container را اجرا می‌کند، کامند را اجرا می‌کند و بعد متوقف می‌کند

set -e

WORK_DIR="/opt/irpps/src"

if [ -z "$1" ]; then
    echo "استفاده: ./run_commands_in_docker.sh <command>"
    echo "مثال: ./run_commands_in_docker.sh 'inspect_database'"
    echo "مثال: ./run_commands_in_docker.sh 'import_content_from_json --author-id 1 --file /path/to/file.json'"
    exit 1
fi

cd "$WORK_DIR"

echo "📦 اجرای backend container..."
docker compose up -d backend mysql

echo "⏳ منتظر آماده شدن MySQL..."
sleep 5

echo "🚀 اجرای کامند..."
docker compose exec -T backend python3 manage.py "$@"

EXIT_CODE=$?

echo ""
echo "🛑 متوقف کردن container..."
docker compose stop backend mysql

exit $EXIT_CODE

