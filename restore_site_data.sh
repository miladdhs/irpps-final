#!/bin/sh
set -eu

AUTHOR_ID="${1:-1}"

echo "Starting required containers..."
docker compose up -d mysql backend

echo "Waiting for backend to finish startup..."
sleep 15

echo "Running migrations..."
docker compose exec -T backend python manage.py migrate --noinput

echo "Importing latest prepared site data bundle..."
docker compose exec -T backend python manage.py import_site_data_bundle --author-username "system_import_${AUTHOR_ID}"

echo "Verifying restored record counts..."
docker compose exec -T backend python manage.py inspect_database --format count

echo "Restore workflow finished."
