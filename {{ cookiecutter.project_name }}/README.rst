{{ cookiecutter.project_name }}
==========================================

Introduction

{{ cookiecutter.project_short_description }}

Development installation of this project itself
-----------------------------------------------

We use Docker in this project. Build it as follows::

  $ docker compose build --build-arg uid=`id -u` --build-arg gid=`id -g` web

And up the service::

  $ docker compose up web

Optionally, install pre-commit hooks (isort, black, flake8, mypy)::

  $ pre-commit install

Testing
-------

We use pytest::

  $ docker compose run --rm web pytest --cov

  $ docker compose run --rm web pytest integration_test


Bumping package versions
------------------------

If you want to upgrade all package versions, use pip-compile::

  $ docker compose run --rm web pip-compile requirements/base.in

  $ docker compose run --rm web pip-compile requirements/dev.in

If you want to selectively upgrade a package version (e.g. fastapi)::

  $ docker compose run --rm web pip-compile -P fastapi requirements/base.in


Updating the project's cruft
----------------------------

This project was generated from https://github.com/nens/cookiecutter-python-app-template.
Any update done in the template can be imported into this repo using cruft (https://cruft.github.io/)::

  $ pip install cruft

  $ cruft update
