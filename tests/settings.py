# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "6q8wk36(q4*8666-==w*sz8)k7l@@2!o8n_jw0wtk3+q+falk@"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    'quartet_masterdata',
    'quartet_capture',
    'quartet_output',
    'serialbox',
    'list_based_flavorpack',
    'random_flavorpack',
    'quartet_templates',
    'simple_history',
    'quartet_trail',
    'quartet_epcis',
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()
