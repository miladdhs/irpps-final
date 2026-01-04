#!/bin/bash
# اسکریپت اجرای دستور add_new_events روی PC محلی
# این اسکریپت می‌تواند از SSH Tunnel یا اتصال مستقیم استفاده کند

set -e

# رنگ‌ها برای خروجی
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# مسیرهای پیش‌فرض
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$SCRIPT_DIR"
ENV_FILE="$BACKEND_DIR/.env.local"

echo -e "${BLUE}🔍 بررسی تنظیمات...${NC}"

# بررسی وجود فایل .env.local
if [ ! -f "$ENV_FILE" ]; then
    echo -e "${YELLOW}⚠️  فایل .env.local پیدا نشد${NC}"
    echo -e "${YELLOW}💡 ایجاد فایل نمونه از .env.local.example...${NC}"
    
    if [ -f "$BACKEND_DIR/.env.local.example" ]; then
        cp "$BACKEND_DIR/.env.local.example" "$ENV_FILE"
        echo -e "${GREEN}✅ فایل .env.local ایجاد شد${NC}"
        echo -e "${YELLOW}⚠️  لطفاً تنظیمات را در $ENV_FILE ویرایش کنید${NC}"
        exit 1
    else
        echo -e "${RED}❌ فایل .env.local.example هم پیدا نشد!${NC}"
        exit 1
    fi
fi

# بارگذاری متغیرهای محیطی از .env.local
echo -e "${BLUE}📋 بارگذاری تنظیمات از .env.local...${NC}"

# خواندن فایل .env.local و export کردن متغیرها
set -a
source "$ENV_FILE"
set +a

# بررسی متغیرهای ضروری
REQUIRED_VARS=("DB_NAME" "DB_USER" "DB_PASSWORD" "DB_HOST" "DB_PORT")
MISSING_VARS=()

for var in "${REQUIRED_VARS[@]}"; do
    if [ -z "${!var}" ]; then
        MISSING_VARS+=("$var")
    fi
done

if [ ${#MISSING_VARS[@]} -ne 0 ]; then
    echo -e "${RED}❌ متغیرهای زیر در .env.local تنظیم نشده‌اند:${NC}"
    for var in "${MISSING_VARS[@]}"; do
        echo -e "   - $var"
    done
    exit 1
fi

# نمایش تنظیمات (بدون نمایش پسورد)
echo ""
echo -e "${BLUE}📋 تنظیمات:${NC}"
echo -e "   DB_HOST: $DB_HOST"
echo -e "   DB_NAME: $DB_NAME"
echo -e "   DB_USER: $DB_USER"
echo -e "   DB_PORT: $DB_PORT"
echo ""

# بررسی اتصال به دیتابیس
echo -e "${BLUE}🔍 در حال بررسی اتصال به دیتابیس...${NC}"

# بررسی اینکه آیا Python و PyMySQL نصب هستند
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 نصب نشده است!${NC}"
    exit 1
fi

# تست اتصال
python3 -c "
import pymysql
import sys
try:
    conn = pymysql.connect(
        host='$DB_HOST',
        port=int('$DB_PORT'),
        user='$DB_USER',
        password='$DB_PASSWORD',
        database='$DB_NAME',
        connect_timeout=10
    )
    conn.close()
    print('✅ اتصال به دیتابیس موفق بود')
    sys.exit(0)
except pymysql.err.OperationalError as e:
    if 'Can\'t connect' in str(e):
        print(f'❌ نتوانست به دیتابیس متصل شود: {e}')
        print('💡 اگر از SSH Tunnel استفاده می‌کنید، مطمئن شوید تونل فعال است:')
        print('   ssh -L $DB_PORT:localhost:3306 root@api.irpps.org')
    else:
        print(f'❌ خطا در اتصال: {e}')
    sys.exit(1)
except Exception as e:
    print(f'❌ خطای غیرمنتظره: {e}')
    sys.exit(1)
" 2>&1

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ نتوانستیم به دیتابیس متصل شویم!${NC}"
    echo ""
    echo -e "${YELLOW}💡 راهنمای استفاده از SSH Tunnel:${NC}"
    echo "   1. در یک ترمینال جداگانه تونل SSH را ایجاد کنید:"
    echo "      ssh -L $DB_PORT:localhost:3306 root@api.irpps.org"
    echo "   2. سپس این اسکریپت را در ترمینال دیگر اجرا کنید"
    echo ""
    echo -e "${YELLOW}💡 یا از اسکریپت run_add_events_docker.sh روی سرور استفاده کنید${NC}"
    exit 1
fi

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

# تنظیم متغیرهای محیطی اضافی
export IS_DOCKER="False"
export SECRET_KEY="${SECRET_KEY:-django-insecure-ispp-project-secret-key-2024-change-in-production-xyz123}"
export ALLOWED_HOSTS="${ALLOWED_HOSTS:-localhost,127.0.0.1}"

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

