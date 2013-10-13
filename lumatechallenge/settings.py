"""Settings for the Lumate Challenge Django project.

This script attempts to find a file called ".debug", which is placed on
the testing server and not pulled or pushed with git.  The final server
will not have this file.  As a result, we use it's presence to toggle
debug mode and determine which settings to use.

Settings beginning with LC are unique to the Lumate Challenge.

"""
from os import path

# Root path for this project
LC_ROOT = path.dirname(__file__) + '/'

# Debug
if path.exists(LC_ROOT + '.debug'):
    DEBUG = True
else:
    DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Contact
ADMINS = (
    ('Alexander Litty', 'me@alexlity.com'),
    )
MANAGERS = ADMINS

# Database
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'lumatechallenge',
            'USER': 'runner',
            'PASSWORD': 'asdf1234',
            'HOST': 'localhost',
            'PORT': '',
            }
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'lumatechallenge',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '',
            }
        }

# Lumate Challenge paths and URLs
if DEBUG:
    LC_URL = 'http://localhost/lumateChallenge/'
else:
    LC_URL = 'http://ec2-54-200-136-220.us-west-2.compute.amazonaws.com/'
    
# Other paths and URLs
MEDIA_ROOT = LC_ROOT + 'media/'
MEDIA_URL = LC_URL + 'media/'
ROOT_URLCONF = 'lumatechallenge.urls'
ALLOWED_HOSTS = [LC_URL]

# Time, date, and other locale
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_TZ = True
USE_L10N = True
USE_I18N = True

# Static files
STATIC_ROOT = LC_ROOT + 'static/'
STATIC_URL = LC_URL + 'static/'
STATICFILES_DIRS = (
    LC_ROOT + 'static/'
    )
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

# Templates
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )
TEMPLATE_DIRS = (
    LC_ROOT + 'templates/'
    )
    
# Apps and Middleware
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    )
INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'guestbook'
    )

# Django Misc
WSGI_APPLICATION = 'lumatechallenge.wsgi.application'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer' 
SECRET_KEY = '%9%cm@2qms!4)&h6jwbah8$fcel2706jf6jbw01+*&23u^+pus'