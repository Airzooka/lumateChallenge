import os

"""Settings for the Lumate Challenge Django project.

Those beginning with LC are unique to this project.

"""

# Debug
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Contact
ADMINS = (
    ('Alexander Litty', 'me@alexlity.com'),
)
MANAGERS = ADMINS

# Database
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

# Paths and hosts
LC_ROOT = os.path.dirname(__file__)
LC_URL = 'http://ec2-54-200-136-220.us-west-2.compute.amazonaws.com/'
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
    '/home/lumatechallenge/static/'
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
    '/home/lumatechallenge/templates/'
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

# Misc    
SECRET_KEY = '%9%cm@2qms!4)&h6jwbah8$fcel2706jf6jbw01+*&23u^+pus'