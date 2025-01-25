#!/usr/bin/env python

"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

import ast
import os
import warnings
from pathlib import Path

import dj_database_url
import dj_email_url
import django_cache_url
from django.core.management.utils import get_random_secret_key

# Set custom environment Variables
#
ENV = os.environ


#
# Custom functions
#
def get_list(text):
    """Split the bash environment varilables into list."""
    return [item.strip() for item in text.split(",")]


def get_bool_from_env(name, default_value):
    """Get boolean values from environment variables."""
    if name in ENV:
        value = ENV[name]
        try:
            return ast.literal_eval(value)
        except ValueError as err:
            raise ValueError(
                "{} is an invalid value for {}".format(value, name)
            ) from err
    return default_value


#
# Django debug toolbar
# https://docs.djangoproject.com/en/stable/ref/settings/#internal-ips
#
INTERNAL_IPS = get_list(os.getenv("INTERNAL_IPS", "127.0.0.1,::1"))

#
# Build paths inside the project like this: BASE_DIR / 'subdir'.
#
BASE_DIR = Path(__file__).resolve().parent.parent

#
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
#
# SECURITY WARNING: keep the secret key used in production secret!
#
SECRET_KEY = os.getenv("SECRET_KEY")

#
# SECURITY WARNING: don't run with debug turned on in production!
#
DEBUG = get_bool_from_env("DEBUG", False)

if not SECRET_KEY and DEBUG:
    warnings.warn("SECRET_KEY not configured, using a random temporary key.")
    SECRET_KEY = get_random_secret_key()

#
# This is a list of valid fully-qualified domain names (FQDNs) for the Django
# server. Django will not permit write access to the server via any other
# hostnames. The first FQDN in the list will be treated as the preferred name.
# https://docs.djangoproject.com/en/stable/ref/settings/#allowed-hosts
#
ALLOWED_HOSTS = get_list(os.getenv("ALLOWED_HOSTS", "localhost"))

#
# Specify one or more name and email address tuples representing
# {{ project_name }} administrators. These people will be notified of
# application errors (assuming correct email settings are provided).
# https://docs.djangoproject.com/en/stable/ref/settings/#admins
#
ADMINS = [tuple(get_list(os.environ["ADMINS"]))]
MANAGERS = ADMINS

#
# Application definition
#
DJANGO_APPS = [
    #
    # Django
    #
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #
    # https://docs.djangoproject.com/en/stable/ref/contrib/humanize/
    #
    "django.contrib.humanize",
    #
    # https://docs.djangoproject.com/en/stable/ref/contrib/postgres/search/
    #
    "django.contrib.postgres",
    #
    # Admin
    #
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    #
    # 3rd Party
    #
    "corsheaders",
    "csp",
    "django_crontab",
    #
    # https://django-dbbackup.readthedocs.io/en/stable/index.html
    #
    "dbbackup",
    #
    # https://django-hosts.readthedocs.io/en/latest/index.html
    #
    # "django_hosts",
    #
    # https://django-health-check.readthedocs.io/en/stable
    #
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.storage",
    "health_check.contrib.migrations",
    "health_check.contrib.psutil",
    "health_check.contrib.redis",
]
LOCAL_APPS = [
    #
    # Local Apps
    #
]
FRONTEND_APPS = [
    #
    # Frontend Apps
    #
]
DEBUG_APPS = [
    #
    # Development | Debug
    #
    "django_extensions",
]

INSTALLED_APPS = (
    DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + FRONTEND_APPS + DEBUG_APPS
)

#
# DB BACKUP
#
DB_BACKUP_PATH = BASE_DIR / "backup/"
DBBACKUP_STORAGE = "django.core.files.storage.FileSystemStorage"
DBBACKUP_STORAGE_OPTIONS = {"location": os.getenv("BACKUP_PATH", DB_BACKUP_PATH)}
DBBACKUP_EMAIL_SUBJECT_PREFIX = "[DB_BACKUP] "

#
# Settings for django-hosts
#
# ROOT_HOSTCONF = "{{ project_name }}.hosts"
# DEFAULT_HOST = ""
ROOT_URLCONF = "{{ project_name }}.urls"

#
# Health Check
#
HEALTH_CHECK = {
    "DISK_USAGE_MAX": 90,  # percent
    "MEMORY_MIN": 100,  # in MB
}
REDIS_URL = os.getenv("CACHE_URL", "redis://127.0.0.1:6379/1")

#
# Middleware
#
MIDDLEWARE = [
    #
    # Django-Hosts Middleware
    #
    # "django_hosts.middleware.HostsrequestMiddleware",
    "django.middleware.security.SecurityMiddleware",
    #
    # https://github.com/adamchainz/django-permissions-policy/tree/main
    #
    "django_permissions_policy.PermissionsPolicyMiddleware",
    #
    # WhiteNoise Middleware
    #
    "whitenoise.middleware.WhiteNoiseMiddleware",
    #
    # Custom Middleware to display header x-page-generation-duration-ms
    # with time taken to load (process) the Request.
    #
    "{{ project_name }}.middleware.StatsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    #
    # Cross Headers
    #
    "corsheaders.middleware.CorsMiddleware",
    #
    # Caches
    #
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    #
    # 3rd Party Django-CSP
    #
    "csp.middleware.CSPMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    #
    # Django-Hosts Middleware
    #
    # "django_hosts.middleware.HostsresponseMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(BASE_DIR / "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.csrf",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "{{ project_name }}.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "{{ project_name }}.wsgi.application"

#
# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
#
DATABASES = dict()
DATABASES["default"] = dj_database_url.config(conn_max_age=600, conn_health_checks=True)
#
# Default primary key field type
# https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field
#
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#
# Which cache alias to use
# https://docs.djangoproject.com/en/stable/ref/settings/#cache-middleware-alias
#
CACHE_MIDDLEWARE_ALIAS = "default"
#
# Number of seconds to cache a page for (TTL)
# https://docs.djangoproject.com/en/stable/ref/settings/#cache-middleware-seconds
#
CACHE_MIDDLEWARE_SECONDS = 600
#
# Should be used if the cache is shared across multiple sites that use the same Django instance
# https://docs.djangoproject.com/en/stable/ref/settings/#cache-middleware-key-prefix
#
CACHE_MIDDLEWARE_KEY_PREFIX = ""

#
# Caches
# https://docs.djangoproject.com/en/stable/ref/settings/#caches
# https://docs.djangoproject.com/en/stable/topics/cache/#cache-arguments
#
CACHES = {"default": django_cache_url.config()}
CACHES["default"]["TIMEOUT"] = int(os.getenv("CACHE_TIMEOUT", 60))
#
# Default User Auth Model
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-user-model
# https://docs.djangoproject.com/en/stable/topics/auth/customizing/#auth-custom-user
#
AUTH_USER_MODEL = "auth.User"

#
# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators
#
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

#
# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/
#
LANGUAGE_CODE = os.getenv("LANGUAGE_CODE", "en-us")
TIME_ZONE = os.getenv("TIME_ZONE", "UTC")
USE_I18N = get_bool_from_env("USE_I18N", True)
USE_L10N = get_bool_from_env("USE_L10N", True)
USE_TZ = get_bool_from_env("USE_TZ", True)

#
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/
# https://docs.djangoproject.com/en/stable/ref/settings/#static-root
# https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/#staticfiles-finders
#

#
# If you do want to run `python manage.py collectstatic --noinput` command,
# and if you want to use multiple static directory use STATICFILES_DIRS and
# disable STATIC_ROOT.
#
# The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting.
#
STATICFILES_DIRS = [
    str(BASE_DIR / "staticfiles"),
]

#
# Command `python manage.py collectstatic --noinput` will copy all static files
# into STATIC_ROOT.
#
STATIC_ROOT = str(BASE_DIR / "static")
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_URL = "/static/"
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

#
# https://docs.djangoproject.com/en/5.1/ref/settings/#media-root
#
MEDIA_ROOT = str(BASE_DIR / "media")
MEDIA_URL = "/media/"

#
# Cookie settings
# https://docs.djangoproject.com/en/stable/ref/settings/#sessions
#
SESSION_COOKIE_NAME = "X-SESSION-COOKIE"
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


#
# CSRF Cookie Settings
# https://docs.djangoproject.com/en/stable/ref/settings/#csrf-cookie-httponly
#
CSRF_COOKIE_NAME = "X-CSRF-COOKIE"
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = get_list(os.getenv("CSRF_TRUSTED_ORIGINS", "https://localhost"))

#
# HTTPS Everywhere
#
SECURE_SSL_REDIRECT = True
SECURE_SSL_HOST = ALLOWED_HOSTS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

#
# Strict-Transport-Security
#
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

#
# X-Frame-Options
# https://docs.djangoproject.com/en/stable/ref/settings/#x-frame-options
# https://docs.djangoproject.com/en/stable/ref/clickjacking/
#
X_FRAME_OPTIONS = "SAMEORIGIN"

#
# X-XSS-Protection
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-browser-xss-filter
#
SECURE_BROWSER_XSS_FILTER = True

#
# X-Content-Type-Options
#
SECURE_CONTENT_TYPE_NOSNIFF = True

#
# Referrer Policy
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-referrer-policy
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
#
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

#
# Content Security Policy (CSP)
# https://django-csp.readthedocs.io/en/latest/index.html
# https://www.laac.dev/blog/content-security-policy-using-django/
#
CSP_DEFAULT_SRC = [
    "'self'",
    "http:",
    "https:",
    "data:",
    "blob:",
]
CSP_STYLE_SRC = [
    "'self'",
]
CSP_SCRIPT_SRC = [
    "'self'",
]
CSP_SCRIPT_SRC_ELEM = [
    "'self'",
]
CSP_FONT_SRC = [
    "'self'",
]
CSP_IMG_SRC = [
    "'self'",
    "https://i.pinimg.com",
]
CSP_FRAME_SRC = [
    "'self'",
]
CSP_INCLUDE_NONCE_IN = [
    "script-src",
    "script-src-elem",
]

#
# Permission-Policy
# https://github.com/adamchainz/django-permissions-policy/tree/main
# https://adamj.eu/tech/2019/08/02/feature-policy-updates-now-required-for-a-plus/
#
PERMISSIONS_POLICY = {
    "accelerometer": [],
    "autoplay": [],
    "camera": [],
    "display-capture": [],
    "encrypted-media": [],
    "fullscreen": [],
    "geolocation": [],
    "gyroscope": [],
    "magnetometer": [],
    "microphone": [],
    "midi": [],
    "payment": [],
    "usb": [],
}

#
# Django cross headers
# https://github.com/adamchainz/django-cors-headers
#
CORS_ORIGIN_WHITELIST = get_list(
    os.getenv("CORS_ORIGIN_WHITELIST", "https://localhost")
)
CORS_ALLOW_METHODS = get_list(os.getenv("CORS_ALLOW_METHODS", "GET,POST,PUT,DELETE"))

#
# Email Settings
# https://docs.djangoproject.com/en/stable/ref/settings/#email-backend
#
email_config = dj_email_url.config()
EMAIL_FILE_PATH = email_config["EMAIL_FILE_PATH"]
EMAIL_HOST_USER = email_config["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = email_config["EMAIL_HOST_PASSWORD"]
EMAIL_HOST = email_config["EMAIL_HOST"]
EMAIL_PORT = email_config["EMAIL_PORT"]
EMAIL_BACKEND = email_config["EMAIL_BACKEND"]
EMAIL_USE_TLS = email_config["EMAIL_USE_TLS"]
EMAIL_USE_SSL = email_config["EMAIL_USE_SSL"]
EMAIL_SUBJECT_PREFIX = "[PROJECT] "

#
# Default sent email address
# https://docs.djangoproject.com/en/stable/ref/settings/#default-from-email
#
SERVER_EMAIL = email_config.get("SERVER_EMAIL", "root@localhost")
DEFAULT_FROM_EMAIL = email_config.get("DEFAULT_FROM_EMAIL", "webmaster@localhost")

#
# Cronjobs
#
PYTHON_PATH = str(os.getenv("VIRTUAL_ENV")) + "/bin/python"
CRONTAB_PYTHON_EXECUTABLE = "dotenvx run -- " + PYTHON_PATH
CRONTAB_COMMAND_SUFFIX = ">/dev/null 2>&1"
CRONJOBS = [
    ("0 4 * * *", "django.core.management.call_command", ["clearsessions"]),
    (
        "0 5 * * *",
        "{{ project_name }}.backup.backup_job",
        ">> " + os.path.join(BASE_DIR, "backup/backup.log"),
    ),
]
