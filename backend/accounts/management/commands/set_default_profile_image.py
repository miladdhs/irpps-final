"""
Management command to set default profile image for all users
Usage: python manage.py set_default_profile_image
"""
import os
import sys
import shutil
from pathlib import Path
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.files import File
from django.conf import settings

# Fix encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

User = get_user_model()


class Command(BaseCommand):
    help = 'Set default profile image for all users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--image',
            type=str,
            default='data/images (1).png',
            help='Path to default image file'
        )

    def handle(self, *args, **options):
        image_path = options['image']
        
        # Get absolute path
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        source_image = base_dir / image_path
        
        if not source_image.exists():
            self.stdout.write(self.style.ERROR(f'Image file not found: {source_image}'))
            return
        
        self.stdout.write(f'Setting default profile image from: {source_image}')
        
        # Ensure media directory exists
        media_root = Path(settings.MEDIA_ROOT)
        profile_images_dir = media_root / 'profile_images'
        profile_images_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy image to media directory with a standard name
        default_image_name = 'default_profile.png'
        dest_image = profile_images_dir / default_image_name
        
        try:
            # Copy the image file
            shutil.copy2(source_image, dest_image)
            self.stdout.write(f'Copied image to: {dest_image}')
            
            # Update all users
            users = User.objects.all()
            updated_count = 0
            
            for user in users:
                # Update all users with default image (even if they already have one)
                # Open the copied image file
                with open(dest_image, 'rb') as f:
                    user.profile_image.save(
                        default_image_name,
                        File(f),
                        save=True
                    )
                updated_count += 1
                self.stdout.write(f'Updated user: {user.username}')
            
            self.stdout.write('')
            self.stdout.write(self.style.SUCCESS('=' * 50))
            self.stdout.write(self.style.SUCCESS('Update Summary:'))
            self.stdout.write(self.style.SUCCESS(f'  Total users: {users.count()}'))
            self.stdout.write(self.style.SUCCESS(f'  Updated: {updated_count}'))
            self.stdout.write(self.style.SUCCESS('=' * 50))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            import traceback
            traceback.print_exc()

