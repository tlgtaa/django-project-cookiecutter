#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# We use calendar versioning
version = "2022.07.30"

setup(
    name="django-project-cookiecutter",
    version=version,
    description=(
        "A very opinionated Cookiecutter template for creating production-ready "
        "Django projects quickly."
    ),
    author="Abdraimov Talgat",
    author_email="abdraimov.talga@gmail.com",
    url="",
    packages=[],
    license="BSD",
    zip_safe=False,
    keywords=(
        "cookiecutter, Python, projects, project templates, django, "
        "skeleton, scaffolding, project directory, setup.py, boilerplate"
    ),
)
