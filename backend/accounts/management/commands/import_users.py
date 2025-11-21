"""
Management command to import users from Excel file
Usage: python manage.py import_users
"""
import os
import sys
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction
from pathlib import Path
import openpyxl

# Fix encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

User = get_user_model()


class Command(BaseCommand):
    help = 'Import users from Excel file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='data/اسامی اعضای انجمن ریه -403.xlsx',
            help='Path to Excel file'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        
        # Get absolute path
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        excel_path = base_dir / file_path
        
        if not excel_path.exists():
            print(f'File not found: {excel_path}')
            return
        
        print(f'Reading Excel file: {excel_path}')
        
        try:
            # Open Excel file
            workbook = openpyxl.load_workbook(excel_path)
            sheet = workbook.active
            
            # Get headers (first row)
            headers = []
            for cell in sheet[1]:
                headers.append(cell.value if cell.value else '')
            
            print(f'Headers found: {headers}')
            
            # Find column indices
            col_indices = {}
            for idx, header in enumerate(headers, start=1):
                header_str = str(header).strip().strip('"').strip("'") if header else ''
                header_clean = header_str.replace('"', '').replace("'", '').strip()
                header_lower = header_clean.lower()
                
                if 'کد ملی' in header_clean or 'کدملی' in header_clean or 'national' in header_lower:
                    col_indices['national_code'] = idx
                elif 'نظام پزشکی' in header_clean or 'شماره نظام' in header_clean or 'کد نظام' in header_clean or 'کدنظام' in header_clean or 'medical' in header_lower or 'نظام' in header_clean:
                    col_indices['medical_code'] = idx
                # Check for combined Persian name column: "نام و نام خانوادگی"
                elif 'نام' in header_clean and 'خانوادگی' in header_clean:
                    col_indices['full_name_fa'] = idx
                # Check for combined English name column: "First Name & Last Name"
                elif ('first' in header_lower and 'last' in header_lower) or ('first name' in header_lower and 'last name' in header_lower):
                    col_indices['full_name_en'] = idx
                # Separate first name (English)
                elif ('نام' in header_clean and 'خانوادگی' not in header_clean and 'full_name_fa' not in col_indices) or ('first' in header_lower and 'last' not in header_lower):
                    if 'first_name' not in col_indices:
                        col_indices['first_name'] = idx
                # Separate last name (English)
                elif ('نام خانوادگی' in header_clean and 'full_name_fa' not in col_indices) or ('last' in header_lower and 'first' not in header_lower and 'full_name_en' not in col_indices) or 'family' in header_lower:
                    if 'last_name' not in col_indices:
                        col_indices['last_name'] = idx
                elif 'ایمیل' in header_clean or 'email' in header_lower:
                    col_indices['email'] = idx
                elif 'تلفن' in header_clean or 'phone' in header_lower or 'موبایل' in header_clean:
                    col_indices['phone'] = idx
            
            print(f'Column indices: {col_indices}')
            
            # Process rows
            created_count = 0
            updated_count = 0
            error_count = 0
            
            with transaction.atomic():
                for row_num, row in enumerate(sheet.iter_rows(min_row=2, values_only=False), start=2):
                    try:
                        # Skip empty rows
                        if not any(cell.value for cell in row):
                            continue
                        
                        # Extract data
                        national_code = None
                        medical_code = None
                        first_name = None
                        last_name = None
                        first_name_fa = None
                        last_name_fa = None
                        email = None
                        phone = None
                        
                        if 'national_code' in col_indices:
                            cell_value = row[col_indices['national_code'] - 1].value
                            if cell_value:
                                national_code = str(cell_value).strip().strip('"').strip("'")
                        
                        if 'medical_code' in col_indices:
                            cell_value = row[col_indices['medical_code'] - 1].value
                            if cell_value:
                                medical_code = str(cell_value).strip().strip('"').strip("'")
                        
                        # Handle combined Persian name column: "نام و نام خانوادگی"
                        if 'full_name_fa' in col_indices:
                            cell_value = row[col_indices['full_name_fa'] - 1].value
                            if cell_value:
                                full_name_fa = str(cell_value).strip().strip('"').strip("'")
                                # Split Persian name (usually space-separated)
                                name_parts_fa = full_name_fa.split()
                                if len(name_parts_fa) >= 2:
                                    first_name_fa = name_parts_fa[0]
                                    last_name_fa = ' '.join(name_parts_fa[1:])
                                elif len(name_parts_fa) == 1:
                                    first_name_fa = name_parts_fa[0]
                        
                        # Handle combined English name column: "First Name & Last Name"
                        if 'full_name_en' in col_indices:
                            cell_value = row[col_indices['full_name_en'] - 1].value
                            if cell_value:
                                full_name_en = str(cell_value).strip().strip('"').strip("'")
                                # Split English name (usually space-separated)
                                name_parts_en = full_name_en.split()
                                if len(name_parts_en) >= 2:
                                    first_name = name_parts_en[0]
                                    last_name = ' '.join(name_parts_en[1:])
                                elif len(name_parts_en) == 1:
                                    first_name = name_parts_en[0]
                        
                        # Handle separate first name (English)
                        if 'first_name' in col_indices:
                            cell_value = row[col_indices['first_name'] - 1].value
                            if cell_value:
                                first_name = str(cell_value).strip().strip('"').strip("'")
                        
                        # Handle separate last name (English)
                        if 'last_name' in col_indices:
                            cell_value = row[col_indices['last_name'] - 1].value
                            if cell_value:
                                last_name = str(cell_value).strip().strip('"').strip("'")
                        
                        if 'email' in col_indices:
                            cell_value = row[col_indices['email'] - 1].value
                            if cell_value:
                                email = str(cell_value).strip().strip('"').strip("'")
                        
                        if 'phone' in col_indices:
                            cell_value = row[col_indices['phone'] - 1].value
                            if cell_value:
                                phone = str(cell_value).strip().strip('"').strip("'")
                        
                        # Validate required fields - create user even with incomplete data
                        if not national_code:
                            # Generate a temporary username if national code is missing
                            username = f'temp_user_{row_num}'
                            print(f'Row {row_num}: Warning - No national code, using temporary username: {username}')
                        else:
                            username = national_code
                        
                        if not medical_code:
                            # Generate a temporary password if medical code is missing
                            password = f'temp_pass_{row_num}'
                            print(f'Row {row_num}: Warning - No medical code, using temporary password')
                        else:
                            password = medical_code
                        
                        # Create or update user
                        user, created = User.objects.get_or_create(
                            username=username,
                            defaults={
                                'first_name': first_name or '',
                                'last_name': last_name or '',
                                'first_name_fa': first_name_fa or '',
                                'last_name_fa': last_name_fa or '',
                                'email': email or '',
                                'phone': phone or '',
                                'is_active': True,
                            }
                        )
                        
                        if created:
                            user.set_password(password)
                            user.save()
                            created_count += 1
                            display_name = f"{first_name_fa or first_name or ''} {last_name_fa or last_name or ''}".strip()
                            print(f'Row {row_num}: Created user {username} - {display_name}')
                        else:
                            # Update existing user
                            if first_name:
                                user.first_name = first_name
                            if last_name:
                                user.last_name = last_name
                            if first_name_fa:
                                user.first_name_fa = first_name_fa
                            if last_name_fa:
                                user.last_name_fa = last_name_fa
                            if email:
                                user.email = email
                            if phone:
                                user.phone = phone
                            user.set_password(password)
                            user.is_active = True
                            user.save()
                            updated_count += 1
                            display_name = f"{first_name_fa or first_name or ''} {last_name_fa or last_name or ''}".strip()
                            print(f'Row {row_num}: Updated user {username} - {display_name}')
                    
                    except Exception as e:
                        error_count += 1
                        print(f'Row {row_num}: Error - {str(e)}')
            
            # Summary
            print('')
            print('=' * 50)
            print('Import Summary:')
            print(f'  Created: {created_count}')
            print(f'  Updated: {updated_count}')
            print(f'  Errors: {error_count}')
            print('=' * 50)
        
        except Exception as e:
            print(f'Error reading Excel file: {str(e)}')
            import traceback
            traceback.print_exc()

