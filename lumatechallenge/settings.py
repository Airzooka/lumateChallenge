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
        'USER': 'postgresql',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Paths and hosts
LC_ROOT = '/home/ubuntu/lumatechallenge/'
LC_URL = 'http://ec2-54-200-136-220.us-west-2.compute.amazonaws.com/'
MEDIA_ROOT = LC_ROOT + 'media/'
MEDIA_URL = LC_URL + 'media/'
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
    '/home/_static/'
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
    '/home/_static/html/'
    )

# Django Misc
ROOT_URLCONF = 'lumatechallenge.urls'
WSGI_APPLICATION = 'lumatechallenge.wsgi.application'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.admin',
    # 'django.contrib.admindocs',
    )
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    )
    
# Misc
SITE_ID = 1
SECRET_KEY = '%9%cm@2qms!4)&h6jwbah8$fcel2706jf6jbw01+*&23u^+pus'