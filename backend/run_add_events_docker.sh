#!/bin/bash
# اسکریپت اجرای دستور add_new_events داخل Docker container
# ساده‌ترین روش برای اجرا روی سرور

set -e

# رنگ‌ها برای خروجی
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
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

# بررسی وجود دستور در container
echo -e "${BLUE}🔍 بررسی وجود دستور add_new_events...${NC}"
if ! docker compose exec -T backend test -f /app/events/management/commands/add_new_events.py 2>/dev/null; then
    echo -e "${YELLOW}⚠️  دستور add_new_events در container پیدا نشد${NC}"
    echo -e "${YELLOW}🔨 در حال rebuild کردن backend container (این ممکن است چند دقیقه طول بکشد)...${NC}"
    docker compose build backend
    docker compose up -d backend
    echo -e "${YELLOW}⏳ منتظر آماده شدن backend...${NC}"
    sleep 15
    
    # بررسی مجدد
    if ! docker compose exec -T backend test -f /app/events/management/commands/add_new_events.py 2>/dev/null; then
        echo -e "${RED}❌ بعد از rebuild هم دستور پیدا نشد!${NC}"
        echo -e "${YELLOW}💡 لطفاً دستی بررسی کنید:${NC}"
        echo "   docker compose exec backend ls -la /app/events/management/commands/"
        exit 1
    fi
    echo -e "${GREEN}✅ دستور بعد از rebuild پیدا شد${NC}"
else
    echo -e "${GREEN}✅ دستور پیدا شد${NC}"
fi

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

