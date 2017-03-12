# Django settings for weather project.

from datetime import date, datetime

from django.utils.timezone import utc

from settings_local import *

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i3e4i+^h=7urdu$q$wk#6x(bkom_$o5#ltxtrgf+i%t+!76)h0'

# List of callables that know how to import templates from various sources.
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
#)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'weather.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'weather.wsgi.application'

#TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#)

TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #'DIRS': ['/home/jay/apijay/templates',],
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

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'electricity',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

def nullrain(row):
    row.rain = None
    row.rained = False

def set_rain(rain):
    def func(row):
        row.rain = rain
        row.rained = rain > 0
    return func

def set_temp_out(temp):
    def func(row):
        row.temp_out = temp
    return func

def set_temp_in(temp):
    def func(row):
        row.temp_in = temp
    return func

RAW_DATA = [
    { "start": datetime(2016, 5, 11, 1, 15, 0, 0, utc), "end": datetime(2017, 5, 11, 1, 25, 0, 0, utc), "func": set_temp_out(12.8) },
    { "start": datetime(2017, 1, 12, 0, 0, 0, 0, utc), "end": datetime(2017, 2, 2, 0, 0, 0, 0, utc), "func": nullrain },
    { "start": datetime(2013, 11, 10, 6, 4, 0, 0, utc), "end": datetime(2017, 11, 10, 6, 5, 0, 0, utc), "func": set_temp_in(18.3) }
]

HOUR_ROW = [
    { "start": datetime(2017, 1, 12, 0, 0, 0, 0, utc), "end": datetime(2017, 2, 2, 0, 0, 0, 0, utc), "func": nullrain }
]

DAY_ROW = [
    { "day": date(2017, 1, 12), "func": set_rain(7.6) },
    { "day": date(2017, 1, 13), "func": set_rain(2) },
    { "day": date(2017, 1, 14), "func": set_rain(0) },
    { "day": date(2017, 1, 15), "func": set_rain(6.1) },
    { "day": date(2017, 1, 16), "func": set_rain(3.3) },
    { "day": date(2017, 1, 17), "func": set_rain(0.3) },
    { "day": date(2017, 1, 18), "func": set_rain(0) },
    { "day": date(2017, 1, 19), "func": set_rain(0) },
    { "day": date(2017, 1, 20), "func": set_rain(0) },
    { "day": date(2017, 1, 21), "func": set_rain(0) },
    { "day": date(2017, 1, 22), "func": set_rain(0.3) },
    { "day": date(2017, 1, 23), "func": set_rain(0) },
    { "day": date(2017, 1, 24), "func": set_rain(0) },
    { "day": date(2017, 1, 25), "func": set_rain(0.3) },
    { "day": date(2017, 1, 26), "func": set_rain(0) },
    { "day": date(2017, 1, 27), "func": set_rain(0.3) },
    { "day": date(2017, 1, 28), "func": set_rain(0) },
    { "day": date(2017, 1, 29), "func": set_rain(8.6) },
    { "day": date(2017, 1, 30), "func": set_rain(0.3) },
    { "day": date(2017, 1, 31), "func": set_rain(4.6) },
    { "day": date(2017, 2, 1), "func": set_rain(1.3) }
]
