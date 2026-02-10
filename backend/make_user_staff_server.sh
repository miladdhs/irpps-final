#!/bin/bash

# Script to make a user staff member on the server
# Usage: ./make_user_staff_server.sh [username]
# Default username is 'admin' if not provided

USERNAME="${1:-admin}"

echo "=========================================="
echo "Making user '$USERNAME' a staff member..."
echo "=========================================="

# Run Django shell command to update user
python3 manage.py shell << EOF
from django.contrib.auth import get_user_model

User = get_user_model()

try:
    user = User.objects.get(username='$USERNAME')
    print(f"Found user: {user.username}")
    print(f"Current status:")
    print(f"  - is_staff: {user.is_staff}")
    print(f"  - is_superuser: {user.is_superuser}")
    print(f"  - is_active: {user.is_active}")
    
    # Update user to be staff
    user.is_staff = True
    user.is_active = True
    user.save()
    
    print(f"\n✓ User '{user.username}' is now a staff member!")
    print(f"New status:")
    print(f"  - is_staff: {user.is_staff}")
    print(f"  - is_superuser: {user.is_superuser}")
    print(f"  - is_active: {user.is_active}")
    
except User.DoesNotExist:
    print(f"✗ User '$USERNAME' not found!")
    print("\nAvailable users:")
    for u in User.objects.all()[:10]:
        print(f"  - {u.username} (staff: {u.is_staff}, superuser: {u.is_superuser})")
        
except Exception as e:
    print(f"✗ Error: {e}")

EOF

echo "=========================================="
echo "Done!"
echo "=========================================="
