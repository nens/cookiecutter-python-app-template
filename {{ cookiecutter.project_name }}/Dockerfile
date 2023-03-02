FROM ubuntu:focal

# Get rid of debconf messages like "unable to initialize frontend: Dialog".
# https://github.com/docker/docker/issues/4032#issuecomment-192327844
ARG DEBIAN_FRONTEND=noninteractive

# wait-for-postgres.sh requires psql.
RUN apt-get update && apt-get install -y \
  software-properties-common \
  build-essential \
  git \
  python3-dev \
  python3-pip \
  postgresql-client \
  && rm -rf /var/lib/apt/lists/*

# These handy scripts come from https://github.com/tiangolo/uvicorn-gunicorn-docker
ADD scripts /scripts

# Create a nens user and group, with IDs matching those of the developer.
# The default values can be overridden at build-time via:
#
# docker-compose build --build-arg uid=`id -u` --build-arg gid=`id -g` web
#
# The -l option is to fix a problem with large user IDs (e.g. 1235227245).
# https://forums.docker.com/t/run-adduser-seems-to-hang-with-large-uid/27371/3
# https://github.com/moby/moby/issues/5419
ARG uid=1000
ARG gid=1000
RUN groupadd -g $gid nens && useradd -lm -u $uid -g $gid nens

RUN pip install -U pip pip-tools setuptools wheel --no-cache-dir
ADD requirements /requirements
RUN pip install --no-cache-dir -r /requirements/base.txt -r /requirements/dev.txt -e .

WORKDIR /app
USER nens:nens

# start-reload.sh runs Uvicorn alone (without Gunicorn) and in a single process.
# start.sh runs Gunicorn with Uvicorn worker(s) (recommended for production).
# For the best development experience, live auto-reload is indispensable.
# https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker#development-live-reload
# https://www.uvicorn.org/#running-with-gunicorn
CMD ["/scripts/start-reload.sh"]
