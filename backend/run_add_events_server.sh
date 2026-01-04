#!/bin/bash
# اسکریپت اجرای دستور add_new_events روی سرور (خارج از Docker)
# این اسکریپت IP کانتینر MySQL را پیدا می‌کند و متغیرهای محیطی را تنظیم می‌کند

set -e

# رنگ‌ها برای خروجی
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# مسیرهای پیش‌فرض
WORK_DIR="${WORK_DIR:-/opt/irpps/src}"
BACKEND_DIR="${BACKEND_DIR:-$WORK_DIR/backend}"

# تنظیمات دیتابیس از docker-compose.yaml
DB_NAME="${DB_NAME:-irporg_DB}"
DB_USER="${DB_USER:-irporg_admin}"
DB_PASSWORD="${DB_PASSWORD:-tHPXArRfwrX3WH!*j}"
DB_PORT="${DB_PORT:-3306}"

echo -e "${BLUE}🔍 در حال پیدا کردن کانتینر MySQL...${NC}"

# بررسی وجود کانتینر MySQL
MYSQL_CONTAINER=$(docker ps --filter "name=irpps-mysql" --format "{{.Names}}" | head -n 1)

if [ -z "$MYSQL_CONTAINER" ]; then
    echo -e "${RED}❌ کانتینر MySQL پیدا نشد!${NC}"
    echo -e "${YELLOW}💡 لطفاً ابتدا کانتینرها را اجرا کنید:${NC}"
    echo "   cd $WORK_DIR && docker compose up -d mysql"
    exit 1
fi

echo -e "${GREEN}✅ کانتینر MySQL پیدا شد: $MYSQL_CONTAINER${NC}"

# دریافت IP کانتینر از Docker network
echo -e "${BLUE}🔍 در حال دریافت IP کانتینر MySQL...${NC}"

# روش 1: استفاده از docker inspect
MYSQL_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "$MYSQL_CONTAINER" 2>/dev/null)

# روش 2: اگر روش اول کار نکرد، از docker network استفاده می‌کنیم
if [ -z "$MYSQL_IP" ]; then
    NETWORK_NAME=$(docker inspect -f '{{range $k, $v := .NetworkSettings.Networks}}{{$k}}{{end}}' "$MYSQL_CONTAINER" 2>/dev/null | head -n 1)
    if [ -n "$NETWORK_NAME" ]; then
        MYSQL_IP=$(docker network inspect "$NETWORK_NAME" --format '{{range .Containers}}{{.IPv4Address}}{{end}}' 2>/dev/null | grep -oP '\d+\.\d+\.\d+\.\d+' | head -n 1)
    fi
fi

# روش 3: استفاده از localhost اگر پورت اکسپوز شده باشد
if [ -z "$MYSQL_IP" ]; then
    echo -e "${YELLOW}⚠️  نتوانستیم IP کانتینر را پیدا کنیم. استفاده از localhost...${NC}"
    MYSQL_IP="localhost"
fi

echo -e "${GREEN}✅ IP کانتینر MySQL: $MYSQL_IP${NC}"

# بررسی اتصال به دیتابیس
echo -e "${BLUE}🔍 در حال بررسی اتصال به دیتابیس...${NC}"

# تست اتصال با Python
python3 -c "
import pymysql
import sys
try:
    conn = pymysql.connect(
        host='$MYSQL_IP',
        port=$DB_PORT,
        user='$DB_USER',
        password='$DB_PASSWORD',
        database='$DB_NAME',
        connect_timeout=5
    )
    conn.close()
    print('✅ اتصال به دیتابیس موفق بود')
    sys.exit(0)
except Exception as e:
    print(f'❌ خطا در اتصال به دیتابیس: {e}')
    sys.exit(1)
" 2>&1

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ نتوانستیم به دیتابیس متصل شویم!${NC}"
    echo -e "${YELLOW}💡 پیشنهاد: از اسکریپت run_add_events_docker.sh استفاده کنید${NC}"
    exit 1
fi

# تنظیم متغیرهای محیطی
export DB_HOST="$MYSQL_IP"
export DB_NAME="$DB_NAME"
export DB_USER="$DB_USER"
export DB_PASSWORD="$DB_PASSWORD"
export DB_PORT="$DB_PORT"
export IS_DOCKER="False"
export DEBUG="False"

# تنظیم SECRET_KEY و ALLOWED_HOSTS اگر تنظیم نشده باشند
export SECRET_KEY="${SECRET_KEY:-django-insecure-ispp-project-secret-key-2024-change-in-production-xyz123}"
export ALLOWED_HOSTS="${ALLOWED_HOSTS:-localhost,127.0.0.1}"

echo ""
echo -e "${BLUE}📋 تنظیمات:${NC}"
echo -e "   DB_HOST: $DB_HOST"
echo -e "   DB_NAME: $DB_NAME"
echo -e "   DB_USER: $DB_USER"
echo -e "   DB_PORT: $DB_PORT"
echo ""

# رفتن به دایرکتوری backend
cd "$BACKEND_DIR"

# بررسی وجود manage.py
if [ ! -f "manage.py" ]; then
    echo -e "${RED}❌ فایل manage.py پیدا نشد در: $BACKEND_DIR${NC}"
    exit 1
fi

# فعال‌سازی virtual environment اگر وجود دارد
if [ -d "venv" ]; then
    echo -e "${BLUE}🐍 فعال‌سازی virtual environment...${NC}"
    source venv/bin/activate
elif [ -d "../venv" ]; then
    echo -e "${BLUE}🐍 فعال‌سازی virtual environment...${NC}"
    source ../venv/bin/activate
fi

echo -e "${YELLOW}🚀 در حال اجرای دستور: python manage.py add_new_events${NC}"
echo ""

# اجرای دستور
python manage.py add_new_events

EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✅ دستور با موفقیت اجرا شد${NC}"
else
    echo -e "${RED}❌ دستور با خطا مواجه شد (کد خروج: $EXIT_CODE)${NC}"
fi

exit $EXIT_CODE

