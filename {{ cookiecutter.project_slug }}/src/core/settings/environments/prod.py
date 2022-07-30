from core.settings.components import env


DEBUG = False

ALLOWED_HOSTS = [
    # TODO: check production hosts
    env('DOMAIN_NAME'),
]


_COLLECTSTATIC_DRYRUN = env.bool('DJANGO_COLLECTSTATIC_DRYRUN', default=False)
STATIC_ROOT = '.static' if _COLLECTSTATIC_DRYRUN else '/var/www/django/static'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_ROOT = '/var/www/django/media'

# Security
# https://docs.djangoproject.com/en/3.2/topics/security/
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
