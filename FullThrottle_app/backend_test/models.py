from django.db import models
import pytz
from datetime import datetime

# Create your models here.
class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()  
    end_time = models.DateTimeField()

class User(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    id = models.CharField(max_length=60, primary_key=True)
    real_name = models.CharField(max_length=60)
    tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    activity_periods = models.ManyToManyField(ActivityPeriod)
