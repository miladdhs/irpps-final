"""
Django settings for ISPP project.
Updated for Production/Docker with CORS & CSRF Fixes.
"""

from pathlib import Path
import os
from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-your-secret-key-change-in-production-123456789')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

# Check if we're in Docker environment
IS_DOCKER = os.environ.get('IS_DOCKER', 'False').lower() == 'true'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party apps
    'corsheaders',
    # Local apps
    'accounts',
    'news',
    'events',
    'dashboard',
    'doctors',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # Must be at the top
    'ispp_project.middleware.DatabaseRetryMiddleware', # Database retry logic
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ispp_project.middleware.Media404HandlerMiddleware', # Handle 404 for media files
]

ROOT_URLCONF = 'ispp_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ispp_project.wsgi.application'

# ==========================================
# CORS & CSRF SETTINGS (CRITICAL FIXES)
# ==========================================

# 1. CORS Configuration
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'cache-control',
    'content-type',
    'dnt',
    'expires',
    'origin',
    'pragma',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOWED_ORIGINS = [
    "https://irpps.org",
    "https://www.irpps.org",
    "https://api.irpps.org",
    # Local development
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

# 2. CSRF Configuration (Fix for Django 4+)
# This is required when the Frontend and Backend are on different subdomains
CSRF_TRUSTED_ORIGINS = [
    "https://irpps.org",
    "https://www.irpps.org",
    "https://api.irpps.org",
]

# 3. SSL/Proxy Configuration (Fix for Docker/Nginx/ArvanCloud)
# Allows Django to recognize HTTPS requests from the proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# 4. Cookie Security
# Ensure cookies are sent only over HTTPS in production
# CRITICAL: For cross-origin requests between irpps.org and api.irpps.org
if not DEBUG or IS_DOCKER:
    # Secure cookies (HTTPS only)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # SameSite=None is REQUIRED for cross-origin cookies (with Secure=True)
    SESSION_COOKIE_SAMESITE = "None"
    CSRF_COOKIE_SAMESITE = "None"
    
    # Domain sharing for subdomains (.irpps.org works for both irpps.org and api.irpps.org)
    SESSION_COOKIE_DOMAIN = ".irpps.org"
    CSRF_COOKIE_DOMAIN = ".irpps.org"
else:
    # Development: Allow cookies in localhost
    SESSION_COOKIE_SAMESITE = "Lax"
    CSRF_COOKIE_SAMESITE = "Lax"

# ==========================================

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME', default='fjjedatu_newdbb'),
        'USER': config('DB_USER', default='fjjedatu_newdbb'),
        'PASSWORD': config('DB_PASSWORD', default='fjjedatu_newdbb'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
        'CONN_MAX_AGE': 600,  # Connection pooling - keep connections alive for 10 minutes
        'OPTIONS': {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES', NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci'",
            'charset': 'utf8mb4',
            'connect_timeout': 10,  # Connection timeout in seconds
            'read_timeout': 30,     # Read timeout in seconds
            'write_timeout': 30,    # Write timeout in seconds
        },
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/assets/'

STATICFILES_DIRS = []

if IS_DOCKER:
    # Docker structure (files are at BASE_DIR level)
    for folder in ['dist', 'css', 'js', 'fonts', 'img']:
        if (BASE_DIR / folder).exists():
            STATICFILES_DIRS.append(BASE_DIR / folder)
else:
    # Check if we're in local development (frontend/ exists)
    frontend_dir = BASE_DIR.parent / 'frontend'
    if frontend_dir.exists():
        for folder in ['dist', 'css', 'js', 'fonts', 'img']:
            if (frontend_dir / folder).exists():
                STATICFILES_DIRS.append(frontend_dir / folder)
    else:
        # cPanel deployment structure
        for folder in ['dist', 'css', 'js', 'fonts', 'img']:
            if (BASE_DIR / folder).exists():
                STATICFILES_DIRS.append(BASE_DIR / folder)

# Only add static folder if it exists
if (BASE_DIR / 'static').exists():
    STATICFILES_DIRS.insert(0, BASE_DIR / 'static')

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Login URLs
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'

# Session settings
SESSION_COOKIE_AGE = 86400  # 24 hours
SESSION_SAVE_EVERY_REQUEST = True

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['file', 'console'],
            'level': 'WARNING',
            'propagate': False,
        },
        'ispp_project.middleware': {
            'handlers': ['file', 'console'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}