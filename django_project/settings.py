# coding:utf-8
"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1c!wsf5v7xh5)!a1di$nq@2etwgagfox4gygzxoumxo0eewr(o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', '34.205.17.166', 'pacific-castle-92803.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database

# https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rds.html#python-rds-connect
if True: #'RDS_HOSTNAME' in os.environ:
    # print("get RDS_HOSTNAME = %s, %s" % (os.environ['RDS_HOSTNAME'], "using: "))
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'ebdb', #os.environ['RDS_DB_NAME'],
            'USER': 'admin', #os.environ['RDS_USERNAME'],
            'PASSWORD': 'BXY5201314', #os.environ['RDS_PASSWORD'],
            'HOST': 'aa626k2y7e4zh5.clx727wyrnc4.us-east-1.rds.amazonaws.com', #os.environ['RDS_HOSTNAME'],
            'PORT': '3306', #os.environ['RDS_PORT'],
        }
    }
"""
else:
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
    print("use LOCALHOST mysql: " )
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', #'django.db.backends.sqlite3',
            'NAME': 'localdb', #os.path.join(BASE_DIR, 'db.sqlite3'),
            'USER': 'root',
            'PASSWORD': 'BXY5201314',
            'HOST': 'localhost', #'127.0.0.1',
            'PORT': '3306',
        }
    }
"""
    # print(DATABASES)
"""
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'USER': 'kmvpwjnqwepprh',
            'PASSWORD': 'b5a9c8902a8fbf0bbfd21c60890854f929b3f8b734399838a9a83ea4290a0909',
            'HOST': 'ec2-54-243-61-194.compute-1.amazonaws.com',
            'PORT': '5432',
        }
    }
"""

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'

# ref: https://www.youtube.com/watch?v=lN9-aUpj588
#import dj_database_url
#db_from_env = dj_database_url.config()
#DATABASES['default'].update(db_from_env)

# Activate Django-Heroku.
# ref: https://devcenter.heroku.com/articles/django-app-configuration
# import django_heroku
# django_heroku.settings(locals())

# ref: https://medium.com/@_christopher/how-to-send-emails-with-python-django-through-google-smtp-server-for-free-22ea6ea0fb8e
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# 设成环境变量才可：
EMAIL_HOST_USER = os.environ.get('GMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('GMAIL_PW')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
