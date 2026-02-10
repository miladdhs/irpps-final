#!/usr/bin/env python
"""
Script to make the 'admin' user a staff member with admin privileges
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ispp_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def make_admin_staff():
    """Make the admin user a staff member"""
    try:
        # Find user with username 'admin'
        admin_user = User.objects.get(username='admin')
        
        print(f"Found user: {admin_user.username}")
        print(f"Current status:")
        print(f"  - is_staff: {admin_user.is_staff}")
        print(f"  - is_superuser: {admin_user.is_superuser}")
        print(f"  - is_active: {admin_user.is_active}")
        
        # Update user to be staff
        admin_user.is_staff = True
        admin_user.is_active = True
        admin_user.save()
        
        print(f"\n✓ User '{admin_user.username}' is now a staff member!")
        print(f"New status:")
        print(f"  - is_staff: {admin_user.is_staff}")
        print(f"  - is_superuser: {admin_user.is_superuser}")
        print(f"  - is_active: {admin_user.is_active}")
        
        return True
        
    except User.DoesNotExist:
        print("✗ User 'admin' not found!")
        print("\nAvailable users:")
        for user in User.objects.all()[:10]:
            print(f"  - {user.username} (staff: {user.is_staff}, superuser: {user.is_superuser})")
        return False
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("Making 'admin' user a staff member...")
    print("=" * 60)
    
    success = make_admin_staff()
    
    print("=" * 60)
    if success:
        print("Done! You can now access the admin panel.")
    else:
        print("Failed! Please check the error messages above.")
    print("=" * 60)
