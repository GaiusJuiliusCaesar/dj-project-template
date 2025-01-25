#!/usr/bin/env bash
# -*- coding: utf-8 -*-

#
# Build
#

#
# Add your domain name (domain.tld) to your /etc/hosts file to test locally.
# Remove the 127.0.0.1 when you push to production.
#
docker buildx build --no-cache \
  --add-host domain.tld:127.0.0.1 \
  --add-host www.domain.tld:127.0.0.1 \
  --tag django:latest \
  --file Dockerfile .

#
# Push
#
docker push gaiusjuiliuscaesar7/django:latest
