{{ cookiecutter.project_name }}
==========================================

Introduction

{{ cookiecutter.project_short_description }}

Development installation of this project itself
-----------------------------------------------

We use Docker in this project. Build it as follows::

  $ docker compose build --build-arg uid=`id -u` --build-arg gid=`id -g` web

And up the service::

  $ docker compose up

Optionally, install pre-commit hooks (isort, black, flake8, mypy):

  $ pre-commit install

Testing
-------

  $ docker compose run --rm web pytest 
  $ docker compose run --rm web pytest integration_test


Bumping package versions
------------------------

If you want to upgrade all package versions, use pip-compile:

  $ docker compose run --rm web pip-compile requirements/base.in
  $ docker compose run --rm web pip-compile requirements/dev.in

If you want to selectively upgrade a package version (e.g. fastapi):

  $ docker compose run --rm web pip-compile -P fastapi requirements/base.in
