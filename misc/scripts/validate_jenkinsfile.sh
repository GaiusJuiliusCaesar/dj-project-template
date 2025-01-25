#!/usr/bin/env bash
# -*- coding: utf-8 -*-

##############################################################################
#
# Name        : validate_jenkinsfile.sh
# Description : Validate the Jenkinsfile
# Engineer    : Gaius Juilius Caesar
#
##############################################################################

#
# Make sure have set and you exported the following environment variables.
#
# export JENKINS_URL="https://localhost:8080/jenkins/"
# export JENKINS_USER="jenkinsadmin"
#
# https://localhost:8080/jenkins/user/jenkinsadmin/security/ - API Token
#
# export JENKINS_API_TOKEN="fdhdf34225643646fdhdfg567657erst"
# export JENKINS_INSECURE=false
#

/usr/bin/curl --user ${JENKINS_USER}:${JENKINS_API_TOKEN} \
  -X POST \
  -F "jenkinsfile=<Jenkinsfile" \
  ${JENKINS_URL}/pipeline-model-converter/validate
