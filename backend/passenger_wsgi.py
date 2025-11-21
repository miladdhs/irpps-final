"""
Passenger WSGI configuration for cPanel
This file should be placed in the public_html directory or your domain's root directory
"""

import os
import sys

# Get the directory where this file is located
# In cPanel, this is usually public_html or your domain directory
project_dir = os.path.dirname(os.path.abspath(__file__))

# Add the project directory to Python path
sys.path.insert(0, project_dir)

# Set environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ispp_project.settings')

# Change to project directory (important for relative paths)
os.chdir(project_dir)

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

