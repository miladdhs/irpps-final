#!/bin/bash
# اسکریپت اجرای کامندهای Django از داخل Docker container

# بررسی اینکه docker-compose در حال اجرا است
if ! docker ps | grep -q irpps-backend-1; then
    echo "❌ Docker container در حال اجرا نیست!"
    echo "ابتدا docker-compose up -d را اجرا کنید"
    exit 1
fi

# اجرای کامند
if [ -z "$1" ]; then
    echo "استفاده: ./run_commands_in_docker.sh <command>"
    echo "مثال: ./run_commands_in_docker.sh 'inspect_database'"
    echo "مثال: ./run_commands_in_docker.sh 'import_content_from_json --author-id 1'"
    exit 1
fi

docker-compose exec backend python3 manage.py $@

