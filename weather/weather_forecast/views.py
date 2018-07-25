# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from rest_framework import viewsets
from .serializers import ForecastSerializer

from weather_forecast.models import Forecast


def index(request):
    return render(
        request,
        'index.html',
    )


class ForecastListView(LoginRequiredMixin, generic.ListView):
    model = Forecast
    paginate_by = 3


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all().order_by('-date')
    serializer_class = ForecastSerializer


class ForecastDetailView(generic.DetailView):
    model = Forecast
    template_name = 'weather_forecast/forecast_detail.html'
