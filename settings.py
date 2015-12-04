"""
Django settings for body project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, imp
ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True
	
PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
default_keys = { 'SECRET_KEY':'^$7=a%rulqhqyo$rb5$bpuiu1v=g3g88qssp@@47&g1dcy@hjm'}
use_keys = default_keys
if ON_OPENSHIFT:
    imp.find_module('openshiftlibs')
    import openshiftlibs
    use_keys = openshiftlibs.openshift_secure(default_keys)
SECRET_KEY = use_keys['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('kamiswin', 'kamiswin@hotmail.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = []

ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.MyProfile'
# Application definition

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites",
    "accounts",
    'userena', 
    'guardian', 
    'easy_thumbnails',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
)

ROOT_URLCONF = 'body.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)


WSGI_APPLICATION = 'body.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_DIR, 'dbfile'),                 # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
AUTHENTICATION_BACKENDS = (
        'userena.backends.UserenaAuthenticationBackend',
        'guardian.backends.ObjectPermissionBackend',
        'django.contrib.auth.backends.ModelBackend',
        
    )

ANONYMOUS_USER_ID = -1

SITE_ID = 1

AUTH_PROFILE_MODULE = 'accounts.MyProfile'

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'longcrown@gmail.com'
EMAIL_HOST_PASSWORD = '2951220Gl'
EMAIL_USE_TLS = True


import os
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public/media/')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

USERENA_ACTIVATION_REQUIRED = False
USERENA_DISABLE_PROFILE_LIST = True