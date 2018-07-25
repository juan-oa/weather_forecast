from .models import Forecast
from rest_framework import serializers


class ForecastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forecast
        fields = ('id', 'date', 'min_temp', 'max_temp', 'wind', 'rain')
