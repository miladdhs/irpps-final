#!/bin/bash
set -e

echo "🚀 Starting ISPP Backend Container..."

# Wait for MySQL to be ready
echo "⏳ Waiting for MySQL to be ready..."
until python -c "
import sys
import pymysql
import os
from decouple import config

try:
    conn = pymysql.connect(
        host=config('DB_HOST', default='mysql'),
        port=int(config('DB_PORT', default='3306')),
        user=config('DB_USER', default='irporg_admin'),
        password=config('DB_PASSWORD', default=''),
        database=config('DB_NAME', default='irporg_DB'),
        connect_timeout=5
    )
    conn.close()
    print('MySQL is ready!')
    sys.exit(0)
except Exception as e:
    print(f'MySQL not ready yet: {e}')
    sys.exit(1)
" 2>/dev/null; do
    echo "⏳ MySQL is not ready yet. Waiting 2 seconds..."
    sleep 2
done

echo "✅ MySQL is ready!"

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p /app/staticfiles
mkdir -p /app/media
mkdir -p /app/media/profile_images
mkdir -p /app/logs

# Set proper permissions
chmod -R 755 /app/staticfiles
chmod -R 755 /app/media
chmod -R 755 /app/logs

# Run migrations
echo "🔄 Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "✅ Initialization complete!"

# Start Gunicorn
echo "🚀 Starting Gunicorn..."
exec gunicorn ispp_project.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info

