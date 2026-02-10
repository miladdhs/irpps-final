#!/bin/bash
# Script to add services to database in Docker

echo "🚀 Adding services to database..."
docker exec -it irpps-backend python /app/add_services.py
echo "✅ Done!"
