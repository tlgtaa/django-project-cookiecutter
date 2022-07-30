_DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

_THIRD_PARTY_APPS = [
    'rest_framework',
    'phonenumber_field',
]

_PROJECT_APPS = [
    'core',
]

INSTALLED_APPS = _DJANGO_APPS + _THIRD_PARTY_APPS + _PROJECT_APPS
