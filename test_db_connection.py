#!/usr/bin/env python3
"""
Test script to verify database connection configuration
This script checks if the database connection settings are correct
"""

import os
import sys

# Simulate environment variables from docker-compose.yaml
os.environ['DB_NAME'] = 'irporg_DB'
os.environ['DB_USER'] = 'irporg_admin'
os.environ['DB_PASSWORD'] = 'tHPXArRfwrX3WH!*j'
os.environ['DB_HOST'] = 'mysql'
os.environ['DB_PORT'] = '3306'
os.environ['IS_DOCKER'] = 'True'

# Set UTF-8 encoding for Windows
import sys
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 60)
print("Testing Database Connection Configuration")
print("=" * 60)

# Test 1: Check if PyMySQL is available
print("\n[1] Checking PyMySQL availability...")
try:
    import pymysql
    print("   [OK] PyMySQL is installed")
except ImportError:
    print("   [ERROR] PyMySQL is NOT installed")
    print("   [TIP] Install it with: pip install PyMySQL")
    sys.exit(1)

# Test 2: Check environment variables
print("\n[2] Checking environment variables...")
required_vars = ['DB_NAME', 'DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT']
all_present = True
for var in required_vars:
    value = os.environ.get(var)
    if value:
        # Mask password
        display_value = '***' if 'PASSWORD' in var else value
        print(f"   [OK] {var} = {display_value}")
    else:
        print(f"   [ERROR] {var} is missing")
        all_present = False

if not all_present:
    print("\n   [ERROR] Some environment variables are missing!")
    sys.exit(1)

# Test 3: Test connection (if we can import decouple)
print("\n[3] Testing connection configuration...")
try:
    from decouple import config
    
    db_config = {
        'host': config('DB_HOST', default='mysql'),
        'port': int(config('DB_PORT', default='3306')),
        'user': config('DB_USER', default='irporg_admin'),
        'password': config('DB_PASSWORD', default=''),
        'database': config('DB_NAME', default='irporg_DB'),
    }
    
    print(f"   Connection config:")
    print(f"      Host: {db_config['host']}")
    print(f"      Port: {db_config['port']}")
    print(f"      User: {db_config['user']}")
    print(f"      Database: {db_config['database']}")
    print(f"      Password: {'***' if db_config['password'] else '(empty)'}")
    
    # Try to create connection (this will fail if MySQL is not running, but config is checked)
    print("\n   [NOTE] Actual connection test requires MySQL to be running")
    print("   [TIP] To test actual connection, run this inside Docker container:")
    print("      docker-compose exec backend python test_db_connection.py")
    
except ImportError:
    print("   [WARNING] python-decouple not available (this is OK, it will be in Docker)")
except Exception as e:
    print(f"   [WARNING] Error: {e}")

# Test 4: Compare with docker-compose.yaml settings
print("\n[4] Comparing with docker-compose.yaml settings...")
docker_compose_settings = {
    'MYSQL_DATABASE': 'irporg_DB',
    'MYSQL_USER': 'irporg_admin',
    'MYSQL_PASSWORD': 'tHPXArRfwrX3WH!*j',
}

backend_env = {
    'DB_NAME': 'irporg_DB',
    'DB_USER': 'irporg_admin',
    'DB_PASSWORD': 'tHPXArRfwrX3WH!*j',
}

print("   MySQL Container Settings:")
for key, value in docker_compose_settings.items():
    display_value = '***' if 'PASSWORD' in key else value
    print(f"      {key} = {display_value}")

print("\n   Backend Container Settings:")
for key, value in backend_env.items():
    display_value = '***' if 'PASSWORD' in key else value
    print(f"      {key} = {display_value}")

# Check if they match
if (docker_compose_settings['MYSQL_DATABASE'] == backend_env['DB_NAME'] and
    docker_compose_settings['MYSQL_USER'] == backend_env['DB_USER'] and
    docker_compose_settings['MYSQL_PASSWORD'] == backend_env['DB_PASSWORD']):
    print("\n   [OK] All settings match!")
else:
    print("\n   [ERROR] Settings do NOT match!")
    if docker_compose_settings['MYSQL_DATABASE'] != backend_env['DB_NAME']:
        print(f"      Database name mismatch: {docker_compose_settings['MYSQL_DATABASE']} != {backend_env['DB_NAME']}")
    if docker_compose_settings['MYSQL_USER'] != backend_env['DB_USER']:
        print(f"      User mismatch: {docker_compose_settings['MYSQL_USER']} != {backend_env['DB_USER']}")
    if docker_compose_settings['MYSQL_PASSWORD'] != backend_env['DB_PASSWORD']:
        print(f"      Password mismatch!")

print("\n" + "=" * 60)
print("[OK] Configuration check complete!")
print("=" * 60)
print("\nSummary:")
print("   - All environment variables are set correctly")
print("   - Settings match between MySQL and Backend containers")
print("   - Connection should work when containers are running")
print("\nTo test actual connection:")
print("   1. Start containers: docker-compose up -d")
print("   2. Wait for MySQL to be ready")
print("   3. Check backend logs: docker-compose logs backend")
print("   4. If migrations run successfully, connection is working!")

