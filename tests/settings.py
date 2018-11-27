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
    'quartet_manifest.apps.QuartetManifestConfig',
    'quartet_epcis.apps.QuartetEPCISConfig',
    'quartet_capture.apps.QuartetCaptureConfig',
    'quartet_masterdata.apps.QuartetMasterdataConfig',
    'quartet_output.apps.QuartetOutputConfig',
    'quartet_trail.apps.QuartetTrailConfig',
    'serialbox.apps.PoolsConfig',
    'random_flavorpack.apps.RandomFlavorpackConfig',
    'list_based_flavorpack.apps.ListBasedFlavorpackConfig',
    'quartet_templates.apps.QuartetTemplatesConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'rest_auth',
    'rest_auth.registration',
    'rest_framework_swagger',
    'corsheaders',
    'django_filters',
    'simple_history',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()
