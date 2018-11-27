#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_quartet-trail
------------

Tests for `quartet-trail` models module.
"""

from django.test import TestCase

from quartet_trail import models
from quartet_capture.models import Rule

class TestQuartet_trail(TestCase):

    def setUp(self):
        pass

    def test_tracked_model(self):
        r = Rule()
        r.name = "Test Rule"
        r.description = "A rule description"
        r.save()
        r.name = "Updated Name"
        r.save()
        rule_history = models.HistoricalRule.objects.all()
        self.assertEqual(rule_history[0].name, "Updated Name")
        self.assertEqual(rule_history[1].name, "Test Rule")
        

    def tearDown(self):
        pass
