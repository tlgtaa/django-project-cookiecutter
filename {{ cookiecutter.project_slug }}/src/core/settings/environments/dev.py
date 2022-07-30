import logging
import socket

from core.settings.components.common import MIDDLEWARE
from core.settings.components.installed_apps import INSTALLED_APPS


DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
    'nplusone.ext.django',
    'django_migration_linter',
]

ALLOWED_HOSTS = ['*']


MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'querycount.middleware.QueryCountMiddleware',
]


_HOSTNAME, _, _IPS = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind('.')] + '.1' for ip in _IPS] + ['127.0.0.1', '10.0.2.2']

MIDDLEWARE = ['nplusone.ext.django.NPlusOneMiddleware'] + MIDDLEWARE

# Logging N+1 requests:
NPLUSONE_RAISE = True  # comment out if you want to allow N+1 requests
NPLUSONE_LOGGER = logging.getLogger('django')
NPLUSONE_LOG_LEVEL = logging.WARN
NPLUSONE_WHITELIST = [
    {'model': 'admin.*'},
]
