#!/usr/bin/env python

"""

Name        : get_random_secret_key.py
Description : Generate a secret key
Engineer    : Seshadri Raja

"""

from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()
print(SECRET_KEY)
