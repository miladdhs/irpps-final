"""
Management command to clear all profile images from database
Usage: python manage.py clear_all_profile_images
"""
import os
import sys
import shutil
from pathlib import Path
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

# Fix encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

User = get_user_model()


class Command(BaseCommand):
    help = 'Clear all profile images from database and optionally delete files'

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete-files',
            action='store_true',
            help='Also delete the actual image files from media directory',
        )

    def handle(self, *args, **options):
        delete_files = options['delete_files']
        
        self.stdout.write('Starting profile image cleanup...')
        
        # Get all users with profile images
        users_with_images = User.objects.exclude(profile_image='').exclude(profile_image__isnull=True)
        total_users = users_with_images.count()
        
        if total_users == 0:
            self.stdout.write(self.style.SUCCESS('No users have profile images to clear.'))
            return
        
        self.stdout.write(f'Found {total_users} users with profile images.')
        
        # Confirm action
        if not options.get('verbosity', 1) == 0:
            confirm = input(f'Are you sure you want to clear profile images for {total_users} users? (yes/no): ')
            if confirm.lower() != 'yes':
                self.stdout.write('Operation cancelled.')
                return
        
        cleared_count = 0
        error_count = 0
        
        # Clear profile images from database
        for user in users_with_images:
            try:
                old_image_path = None
                if user.profile_image:
                    old_image_path = user.profile_image.path if hasattr(user.profile_image, 'path') else None
                
                # Clear the profile_image field
                user.profile_image = None
                user.save()
                
                cleared_count += 1
                self.stdout.write(f'Cleared profile image for user: {user.username}')
                
                # Optionally delete the actual file
                if delete_files and old_image_path and os.path.exists(old_image_path):
                    try:
                        os.remove(old_image_path)
                        self.stdout.write(f'  -> Deleted file: {old_image_path}')
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'  -> Could not delete file {old_image_path}: {str(e)}'))
                
            except Exception as e:
                error_count += 1
                self.stdout.write(self.style.ERROR(f'Error clearing image for user {user.username}: {str(e)}'))
        
        # Optionally clean up the entire profile_images directory
        if delete_files:
            try:
                media_root = Path(settings.MEDIA_ROOT)
                profile_images_dir = media_root / 'profile_images'
                
                if profile_images_dir.exists():
                    # Remove all files in the directory
                    for file_path in profile_images_dir.iterdir():
                        if file_path.is_file():
                            try:
                                file_path.unlink()
                                self.stdout.write(f'Deleted file: {file_path}')
                            except Exception as e:
                                self.stdout.write(self.style.WARNING(f'Could not delete {file_path}: {str(e)}'))
                    
                    self.stdout.write(f'Cleaned up profile_images directory: {profile_images_dir}')
                
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'Error cleaning up directory: {str(e)}'))
        
        # Summary
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS('Profile Image Cleanup Summary:'))
        self.stdout.write(self.style.SUCCESS(f'  Total users processed: {total_users}'))
        self.stdout.write(self.style.SUCCESS(f'  Successfully cleared: {cleared_count}'))
        self.stdout.write(self.style.SUCCESS(f'  Errors: {error_count}'))
        if delete_files:
            self.stdout.write(self.style.SUCCESS('  Image files were also deleted from disk'))
        else:
            self.stdout.write(self.style.WARNING('  Image files remain on disk (use --delete-files to remove them)'))
        self.stdout.write(self.style.SUCCESS('=' * 60))