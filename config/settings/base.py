"""
Django settings for Waves Resource Center project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

import decouple
import dj_database_url

# Django Settings
# ===============

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  decouple.config('DJANGO_SECRET_KEY',
    default='nd_3b#di47ij(&qp!&!#mdbl3fuzcj+meu@=!h4u=531(=bti1'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  decouple.config('DJANGO_DEBUG', cast=bool, default=False)

ALLOWED_HOSTS =  decouple.config('ALLOWED_HOSTS', cast=decouple.Csv(),
    default='127.0.0.1, localhost'
)

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'crispy_forms',
    'embed_video',
    'phonenumber_field',
    'storages',
]

LOCAL_APPS = [
    'accounts',
    'books',
    'core',
    'videos',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# https://docs.djangoproject.com/en/3.1/topics/http/middleware/
# https://docs.djangoproject.com/en/3.1/ref/middleware/#middleware-ordering
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Auth
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth

AUTH_USER_MODEL = 'accounts.User'

LOGIN_REDIRECT_URL = 'books'

LOGOUT_REDIRECT_URL = 'index'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {'default': dj_database_url.config(conn_max_age=600)}


# Email
# https://docs.djangoproject.com/en/3.1/ref/settings/#email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST =  decouple.config('DJANGO_EMAIL_HOST', default='smtp.gmail.com')

EMAIL_PORT =  decouple.config('DJANGO_EMAIL_PORT', default=587)

EMAIL_USE_TLS = True

EMAIL_HOST_USER =  decouple.config('DJANGO_EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD =  decouple.config('DJANGO_EMAIL_HOST_PASSWORD')


# Media (user uploaded files)
# https://docs.djangoproject.com/en/3.1/ref/settings/#file-uploads

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = "/media/"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/ref/settings/#static-files

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Third Party Apps Settings
# =========================

# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'



# Project Specific Settings
# =========================

ADMIN_URL = 'admin/'

HEADLESS_BROWSER_TESTS =  decouple.config('CI', cast=bool, default=False)

# Location of files used for testing
TEST_FILES_DIR = BASE_DIR / 'test_files'
