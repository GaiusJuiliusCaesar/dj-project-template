#!/usr/bin/env bash
# -*- coding: utf-8 -*-

##############################################################################
#
# Name        : check_service.sh
# Description : Check Nginx and Gunicorn services are up and running.
# Engineer    : Gaius Juilius Caesar
#
##############################################################################

#
# Check the service status and restart the service.
#
alias sshpass="sshpass -f ~/.sshpass"
/usr/bin/systemctl is-active nginx.service > /dev/null 2>&1
NGINX_SERVICE_STATUS="$?"

if [[ "${NGINX_SERVICE_STATUS}" -ne 0 ]]; then
  sshpass /usr/bin/sudo /usr/bin/systemctl restart nginx.service
fi

/usr/bin/systemctl is-active gunicorn.service > /dev/null 2>&1
GUNICORN_SERVICE_STATUS="$?"

if [[ "${GUNICORN_SERVICE_STATUS}" -ne 0 ]]; then
  sshpass  /usr/bin/sudo /usr/bin/systemctl restart gunicorn.service
fi
