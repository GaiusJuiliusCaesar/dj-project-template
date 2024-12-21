#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings as sett


def settings(request):
    return {"settings": sett}
