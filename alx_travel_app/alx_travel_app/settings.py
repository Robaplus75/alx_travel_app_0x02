from pathlib import Path

import environ

# ENV VARIABLES NEEDED:
#   'DJANGO_SECRET_KEY'
#   'CELERY_BROKER_URL'
#   'DATABASE_URL':
#       POSTGRESQL: DATABASE_URL =  'postgres://USER:PASSWORD@HOST:PORT/NAME'
#       MYSQL: DATABASE_URL      =  'mysql://username:password@localhost:3306/mydatabase'
#       SQLITE: DATABASE_URL     =  'sqlite:///path/to/your/db.sqlite3'
# Initialize environment variables

env = environ.Env()
environ.Env.read_env('.env')  # Reads the .env file


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

SECRET_KEY = env('DJANGO_SECRET_KEY', default='fallback_secret_key')
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'listings',
    'celery',
    'payments'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'alx_travel_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'alx_travel_app.wsgi.application'


DATABASES = {
    'default': env.db('DATABASE_URL')  # This will automatically parse the database URL from the .env
}

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Celery Configurations

CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='amqp://robel:123@localhost:5672/development')

CHAPA_PUBLIC_KEY = env('CHAPA_PUBLIC_KEY')
CHAPA_PRIVATE_KEY = env('CHAPA_PRIVATE_KEY')
CHAPA_CALLBACK_URL = env('CHAPA_CALLBACK_URL')
CHAPA_RETURN_URL = env('CHAPA_RETURN_URL')