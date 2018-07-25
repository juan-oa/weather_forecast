import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ByteOrbit.settings')

app = Celery('weather_forecast')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'collect-daily': {
        'task': 'weather_forecast.models.get_forecast',
        'schedule': crontab(),
    },
}
