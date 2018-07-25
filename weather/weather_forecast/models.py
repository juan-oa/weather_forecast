# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import formats
from django.db import models
from weather_forecast.celery import app
from datetime import datetime
from .serializers import ForecastSerializer
import requests
import json


class Forecast(models.Model):
    """
    Model representing a weather forecast
    """
    date = models.DateTimeField(verbose_name='Date')
    min_temp = models.FloatField(verbose_name='Min', default=0.0)
    max_temp = models.FloatField(verbose_name='Max', default=0.0)
    wind = models.CharField(max_length=200, default='0km/h')
    rain = models.CharField(max_length=200, default='0%')

    def __str__(self):
        return formats.date_format(self.date)

    class Meta:
        ordering = ('-date',)


@app.task
def get_forecast():
    response = requests.post(url='http://weather.news24.com/ajaxpro/Weather.Code.Ajax,Weather.ashx',
                             headers={"X-AjaxPro-Method": "GetCurrentOne"}, data=json.dumps({"cityId": "77107"}))
    response.raise_for_status()
    response.json()

    result = json.loads(response.content)
    data = ForecastSerializer.serializer_field_mapping("json", Forecast.objects.all())
    Forecast.objects.create(date=datetime.strptime(result['value']['LocalUpdateTime'], 'YYYY-MM-DD HH:MM'), min_temp=result['value']['Forecast']['LowTemp'],
                            max_temp=result['value']['Forecast']['HighTemp'],
                            wind=result['value']['Forecast']['WindSpeed'],
                            rain=result['value']['Forecast']['PrecipitationProbability'])
    return result
