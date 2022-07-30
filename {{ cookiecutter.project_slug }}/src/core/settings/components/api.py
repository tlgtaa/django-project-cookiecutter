from datetime import timedelta

from core.settings.components import env


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTTokenUserAuthentication',
    ],
}

SIMPLE_JWT = {
    'SIGNING_KEY': env.str('SIGNING_KEY'),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=120),
    'REFRESH_TOKEN_LIFETIME': timedelta(weeks=120),
}
