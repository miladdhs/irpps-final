#!/bin/bash
# اسکریپت اجرای دستور add_new_events داخل Docker container
# ساده‌ترین روش برای اجرا روی سرور

set -e

# رنگ‌ها برای خروجی
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# مسیرهای پیش‌فرض
WORK_DIR="${WORK_DIR:-/opt/irpps/src}"
COMPOSE_FILE="${COMPOSE_FILE:-$WORK_DIR/docker-compose.yaml}"

# بررسی وجود docker-compose.yaml
if [ ! -f "$COMPOSE_FILE" ]; then
    echo -e "${RED}❌ فایل docker-compose.yaml پیدا نشد: $COMPOSE_FILE${NC}"
    exit 1
fi

cd "$WORK_DIR"

echo -e "${YELLOW}📦 در حال اجرای backend و mysql containers...${NC}"

# اجرای backend و mysql
docker compose up -d backend mysql

# منتظر می‌ماند تا MySQL آماده شود
echo -e "${YELLOW}⏳ منتظر آماده شدن MySQL...${NC}"
sleep 10

# بررسی وضعیت container
if ! docker ps | grep -q irpps-backend; then
    echo -e "${RED}❌ Container backend اجرا نشد!${NC}"
    exit 1
fi

if ! docker ps | grep -q irpps-mysql; then
    echo -e "${RED}❌ Container mysql اجرا نشد!${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Containers اجرا شدند${NC}"
echo -e "${YELLOW}🚀 در حال اجرای دستور: python manage.py add_new_events${NC}"
echo ""

# اجرای دستور داخل container
docker compose exec -T backend python manage.py add_new_events

EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✅ دستور با موفقیت اجرا شد${NC}"
else
    echo -e "${RED}❌ دستور با خطا مواجه شد (کد خروج: $EXIT_CODE)${NC}"
fi

exit $EXIT_CODE

