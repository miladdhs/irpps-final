#!/bin/sh
set -eu

AUTHOR_ID="${1:-1}"

echo "Starting required containers..."
docker compose up -d mysql backend

echo "Waiting for backend to finish startup..."
sleep 15

echo "Running migrations..."
docker compose exec -T backend python manage.py migrate --noinput

echo "Restoring users/news/announcements from ispp_db.json..."
docker compose exec -T backend python manage.py import_ispp_json --path /app/ispp_db.json

echo "Restoring structured news/events from mounted JSON..."
docker compose exec -T backend python manage.py import_content_from_json --file /app/import_content/structured_content_complete.json --update --author-id "${AUTHOR_ID}"

echo "Verifying restored record counts..."
docker compose exec -T backend python manage.py inspect_database --format count

echo "Restore workflow finished."
