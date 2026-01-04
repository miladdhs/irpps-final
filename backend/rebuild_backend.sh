#!/bin/bash
# اسکریپت سریع برای rebuild کردن backend container
# استفاده: ./rebuild_backend.sh

set -e

WORK_DIR="${WORK_DIR:-/opt/irpps/src}"
cd "$WORK_DIR"

echo "🔨 در حال rebuild کردن backend container..."
docker compose build backend
echo "🚀 در حال restart کردن backend..."
docker compose up -d backend
echo "✅ انجام شد!"
echo ""
echo "حالا می‌توانید دستور را اجرا کنید:"
echo "  ./run_add_events_docker.sh"

