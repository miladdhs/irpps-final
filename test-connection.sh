#!/bin/bash

# رنگ‌ها برای خروجی
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=========================================="
echo "تست اتصال Frontend به Backend"
echo "=========================================="
echo ""

# تابع برای تست
test_endpoint() {
    local name=$1
    local url=$2
    local expected_code=${3:-200}
    
    echo -n "تست $name ... "
    response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    
    if [ "$response" -eq "$expected_code" ]; then
        echo -e "${GREEN}✓ موفق${NC} (HTTP $response)"
        return 0
    else
        echo -e "${RED}✗ ناموفق${NC} (HTTP $response، انتظار: $expected_code)"
        return 1
    fi
}

# شمارنده موفقیت
success=0
total=0

echo "=== تست Backend ==="
echo ""

# تست Backend Health
total=$((total + 1))
if test_endpoint "Backend Health" "http://localhost:8000/"; then
    success=$((success + 1))
fi

# تست API Endpoints
total=$((total + 1))
if test_endpoint "API Members" "http://localhost:8000/api/accounts/members/"; then
    success=$((success + 1))
fi

total=$((total + 1))
if test_endpoint "API News" "http://localhost:8000/api/news/"; then
    success=$((success + 1))
fi

total=$((total + 1))
if test_endpoint "API Events" "http://localhost:8000/api/events/"; then
    success=$((success + 1))
fi

echo ""
echo "=== تست Frontend ==="
echo ""

# تست Frontend
total=$((total + 1))
if test_endpoint "Frontend Home" "http://localhost:80/"; then
    success=$((success + 1))
fi

# تست Nginx Proxy
total=$((total + 1))
if test_endpoint "Nginx Proxy to API" "http://localhost:80/api/accounts/members/"; then
    success=$((success + 1))
fi

echo ""
echo "=== تست Database ==="
echo ""

# تست Database Connection
echo -n "تست اتصال Database ... "
if docker-compose exec -T mysql mysql -u irporg_admin -ptHPXArRfwrX3WH\!*j irporg_DB -e "SELECT 1;" > /dev/null 2>&1; then
    echo -e "${GREEN}✓ موفق${NC}"
    success=$((success + 1))
else
    echo -e "${RED}✗ ناموفق${NC}"
fi
total=$((total + 1))

echo ""
echo "=========================================="
echo "نتیجه: $success از $total تست موفق"
echo "=========================================="

if [ $success -eq $total ]; then
    echo -e "${GREEN}✓ همه تست‌ها موفق بودند!${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠ برخی تست‌ها ناموفق بودند${NC}"
    exit 1
fi
