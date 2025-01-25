#!/usr/bin/env bash
# -*- coding: utf-8 -*-

##############################################################################
#
# Name        : runner.sh
# Description : Script to start the gunicorn service inside docker container.
# Engineer    : Gaius Juilius Caesar
# Reference   : https://shorturl.at/CFmsk
#
##############################################################################

#
# Arguments
#
RUN_PORT="${PORT:-9000}"
PROJ_NAME="{{ project_name }}"

nohup /home/linuxbrew/.linuxbrew/opt/redis/bin/redis-server /home/linuxbrew/.linuxbrew/etc/redis.conf &
DOTENV_PRIVATE_KEY=$(cat /opt/venv/bin/envfile) pipenv run /usr/local/bin/dotenvx run --env-file=.env --overload -- ${VIRTUAL_ENV}/bin/python manage.py migrate --no-input
DOTENV_PRIVATE_KEY=$(cat /opt/venv/bin/envfile) pipenv run /usr/local/bin/dotenvx run --env-file=.env --overload -- ${VIRTUAL_ENV}/bin/python manage.py createsuperuser --no-input
DOTENV_PRIVATE_KEY=$(cat /opt/venv/bin/envfile) pipenv run /usr/local/bin/dotenvx run --env-file=.env --overload -- ${VIRTUAL_ENV}/bin/python manage.py crontab add
DOTENV_PRIVATE_KEY=$(cat /opt/venv/bin/envfile) pipenv run /usr/local/bin/dotenvx run --env-file=.env --overload -- ${VIRTUAL_ENV}/bin/python manage.py crontab show
DOTENV_PRIVATE_KEY=$(cat /opt/venv/bin/envfile) pipenv run /usr/local/bin/dotenvx run --env-file=.env --overload -- ${VIRTUAL_ENV}/bin/python ${VIRTUAL_ENV}/bin/gunicorn ${PROJ_NAME}.wsgi:application --bind "0.0.0.0:$RUN_PORT" --daemon
/usr/bin/sudo /usr/sbin/nginx -g 'daemon off;'
