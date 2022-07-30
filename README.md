# Cookiecutter

**A very opinionated Cookiecutter template for creating production-ready Django projects quickly.**


## Usage

First get Cookiecutter
```bash
$ pip install "cookiecutter>=1.7.0"

$ cookiecutter https://github.com/tlgtaa/django-project-cookiecutter.git
```

You'll be prompted for some values. Provide them, then a Django project will be created for you.

**Warning**: After this point, change 'Talgat Abdraimov', etc to your own information.

Answer the prompts with your own desired options. For example:

```bash
$ project_name [My Awesome Project]: saitama-project

$ project_slug [saitama_project]: 

$ description [Behold My Awesome Project!]: My saitama project 

$ author_name [Abdraimov Talgat]: 

$ domain_name [example.com]: saitama.kz

$ email [abdraimov-talgat@example.com]: abdraimov.talga@gmail.com

$ max_line_length [120]: 

$ version [0.1.0]: 

$ timezone [UTC]: Asia/Almaty
$ use_docker [n]: y

$ Select postgresql_version:
    1 - 14
    2 - 13
    3 - 12
    4 - 11
    5 - 10
Choose from 1, 2, 3, 4, 5 [1]: 2

$ use_celery [n]: y

  '[SUCCESS]: Project initialized, keep up the good work!'
```
Enter the project and take a look around:
```bash
$ cd saitama_project/
$ ls
```


