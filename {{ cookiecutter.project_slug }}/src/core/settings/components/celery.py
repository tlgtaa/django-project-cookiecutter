from celery.schedules import crontab

from core.settings.components import env


CELERY_BROKER_URL = env.str('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = env.str('CELERY_RESULT_BACKEND')
CELERY_TASK_DEFAULT_QUEUE = '{{ cookiecutter.project_slug }}'
CELERY_TIMEZONE = '{{ cookiecutter.timezone }}'
