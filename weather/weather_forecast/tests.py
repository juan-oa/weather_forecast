# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from weather_forecast.models import Forecast, get_forecast


class TestForecast(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_collect_from_news24(self):
        get_forecast()
