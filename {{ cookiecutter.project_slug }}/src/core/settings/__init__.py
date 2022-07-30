from split_settings.tools import include

from core.settings.components import BASE_DIR, env


_ENV = env.str('DJANGO_ENV', default='dev')
_base_settings = (
    'components/common.py',
    'components/logging.py',
    'components/cache.py',
    'components/api.py',
    'components/installed_apps.py',
    {% if cookiecutter.use_celery == 'y'  -%}
    'components/celery.py',
    {% endif %}
    # Select the right env:
    f'environments/{_ENV}.py',
)


# Include settings:
include(*_base_settings)
