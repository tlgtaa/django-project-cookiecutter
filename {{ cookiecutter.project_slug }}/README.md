# {{ cookiecutter.project_name }}

## {{ cookiecutter.description }}


## Setup on local machine

```bash
$ cd {{ cookiecutter.project_slug }}
# rename .env-example
$ mv .env-example .env
{% if cookiecutter.use_docker == 'y' -%}
$ docker network create {{ cookiecutter.project_slug }}-network
$ docker-compose up -d --build
{% else -%}
$ python -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements/dev.txt
$ cd src && python manage.py migrate
{% endif %}
```

> **WARNING:** Do not forget to change sensetive secret keys as _DJANGO_SECRET_KEY and etc_.

## Pre-commit

for self check before any changes use pre-commit

`Installation:`
  - Install pre-commit on you local machine
  ```bash
  $ pip install pre-commit
  ```

  - then run in project root (.pre-commit.yaml location)
  ```bash
  $ pre-commit install
  ```
