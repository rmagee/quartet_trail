# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.urls import re_path, include

from quartet_trail.urls import urlpatterns as quartet_trail_urls

app_name = "quartet_trail"

urlpatterns = [
    re_path(r"^", include(quartet_trail_urls)),
]
