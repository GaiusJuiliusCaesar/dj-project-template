#!/usr/bin/env python

from django.shortcuts import render


#
# Index Page
#
def index(request):
    return render(request, "index.html")


#
# Error 400 custom page.
#
def custom_400(request, exception):
    return render(request, "400.html", status=400)


#
# Error 401 custom page.
#
def custom_401(request, exception):
    return render(request, "401.html", status=401)


#
# Error 403 custom page.
#
def custom_403(request, exception):
    return render(request, "403.html", status=403)


#
# Error 404 custom page.
#
def custom_404(request, exception):
    return render(request, "404.html", status=404)


#
# Error 500 custom page.
#
def custom_500(request, exception):
    return render(request, "500.html", status=500)
