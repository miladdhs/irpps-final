#!/bin/bash
# اسکریپت اجرای موقت کامند Django - فقط backend container را اجرا می‌کند و بعد متوقف می‌کند

set -e  # در صورت خطا متوقف شود

# رنگ‌ها برای خروجی
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# بررسی آرگومان‌ها
if [ -z "$1" ]; then
    echo -e "${RED}❌ خطا: کامند را مشخص کنید${NC}"
    echo ""
    echo "استفاده:"
    echo "  ./run_command_temporary.sh 'inspect_database'"
    echo "  ./run_command_temporary.sh 'import_content_from_json --author-id 1 --file /path/to/file.json'"
    echo ""
    echo "مثال‌ها:"
    echo "  ./run_command_temporary.sh 'inspect_database --model news'"
    echo "  ./run_command_temporary.sh 'import_content_from_json --author-id 1 --file /opt/irpps/src/frontend/public/Content/structured_content_complete.json'"
    exit 1
fi

COMMAND="$1"
COMPOSE_FILE="/opt/irpps/src/docker-compose.yaml"
WORK_DIR="/opt/irpps/src"

# بررسی وجود docker-compose.yaml
if [ ! -f "$COMPOSE_FILE" ]; then
    echo -e "${RED}❌ فایل docker-compose.yaml پیدا نشد: $COMPOSE_FILE${NC}"
    exit 1
fi

cd "$WORK_DIR"

echo -e "${YELLOW}📦 در حال اجرای backend container...${NC}"

# فقط backend و mysql را اجرا می‌کند (frontend را اجرا نمی‌کند)
docker compose up -d backend mysql

# منتظر می‌ماند تا MySQL آماده شود
echo -e "${YELLOW}⏳ منتظر آماده شدن MySQL...${NC}"
sleep 5

# بررسی وضعیت container
if ! docker ps | grep -q irpps-backend-1; then
    echo -e "${RED}❌ Container backend اجرا نشد!${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Container اجرا شد${NC}"
echo -e "${YELLOW}🚀 در حال اجرای کامند: python3 manage.py $COMMAND${NC}"
echo ""

# اجرای کامند
docker compose exec -T backend python3 manage.py $COMMAND

EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✅ کامند با موفقیت اجرا شد${NC}"
else
    echo -e "${RED}❌ کامند با خطا مواجه شد (کد خروج: $EXIT_CODE)${NC}"
fi

echo ""
echo -e "${YELLOW}🛑 در حال متوقف کردن container...${NC}"

# متوقف کردن container
docker compose stop backend mysql

echo -e "${GREEN}✅ Container متوقف شد${NC}"

exit $EXIT_CODE

