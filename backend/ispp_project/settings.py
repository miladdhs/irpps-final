"""
Django settings for ISPP project.
"""

from pathlib import Path
import os
from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-your-secret-key-change-in-production-123456789')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'corsheaders',
    'news',
    'events',
    'dashboard',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

#CORS_ALLOW_ALL_ORIGINS = True 
CORS_ALLOW_CREDENTIALS = True  

#CORS_URLS_REGEX = r'^/api/.*$'
 
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
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
CORS_ALLOWED_ORIGINS = [
    "https://irpps.org",
    "https://api.irpps.org",
    "http://irpps.org", 
    "http://api.irpps.org",
]
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME', default='fjjedatu_newdbb'),
        'USER': config('DB_USER', default='fjjedatu_newdbb'),
        'PASSWORD': config('DB_PASSWORD', default='fjjedatu_newdbb'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
        'OPTIONS': {
#            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES', NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci'",
            'charset': 'utf8mb4',
        },
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/assets/'

# Determine static files directories based on project structure
# In local development: frontend/ exists at BASE_DIR.parent / 'frontend'
# In cPanel deployment: dist/, css/, js/, fonts/, img/ exist at BASE_DIR level
# In Docker: files are at BASE_DIR level
STATICFILES_DIRS = []

# Check if we're in Docker
IS_DOCKER = os.environ.get('IS_DOCKER', 'False').lower() == 'true'

if IS_DOCKER:
    # Docker structure (files are at BASE_DIR level)
    if (BASE_DIR / 'dist').exists():
        STATICFILES_DIRS.append(BASE_DIR / 'dist')
    if (BASE_DIR / 'css').exists():
        STATICFILES_DIRS.append(BASE_DIR / 'css')
    if (BASE_DIR / 'js').exists():
        STATICFILES_DIRS.append(BASE_DIR / 'js')
    if (BASE_DIR / 'fonts').exists():
        STATICFILES_DIRS.append(BASE_DIR / 'fonts')
    if (BASE_DIR / 'img').exists():
        STATICFILES_DIRS.append(BASE_DIR / 'img')
else:
    # Check if we're in local development (frontend/ exists)
    frontend_dir = BASE_DIR.parent / 'frontend'
    if frontend_dir.exists():
        # Local development structure
        if (frontend_dir / 'dist').exists():
            STATICFILES_DIRS.append(frontend_dir / 'dist')
        if (frontend_dir / 'css').exists():
            STATICFILES_DIRS.append(frontend_dir / 'css')
        if (frontend_dir / 'js').exists():
            STATICFILES_DIRS.append(frontend_dir / 'js')
        if (frontend_dir / 'fonts').exists():
            STATICFILES_DIRS.append(frontend_dir / 'fonts')
        if (frontend_dir / 'img').exists():
            STATICFILES_DIRS.append(frontend_dir / 'img')
    else:
        # cPanel deployment structure (files are at BASE_DIR level)
        if (BASE_DIR / 'dist').exists():
            STATICFILES_DIRS.append(BASE_DIR / 'dist')
        if (BASE_DIR / 'css').exists():
            STATICFILES_DIRS.append(BASE_DIR / 'css')
        if (BASE_DIR / 'js').exists():
            STATICFILES_DIRS.append(BASE_DIR / 'js')
        if (BASE_DIR / 'fonts').exists():
            STATICFILES_DIRS.append(BASE_DIR / 'fonts')
        if (BASE_DIR / 'img').exists():
            STATICFILES_DIRS.append(BASE_DIR / 'img')

# Only add static folder if it exists
if (BASE_DIR / 'static').exists():
    STATICFILES_DIRS.insert(0, BASE_DIR / 'static')
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

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
