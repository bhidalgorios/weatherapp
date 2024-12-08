from django.db import models
# models.py defines what kind of data you are going to be storing and retrieving
# from your database

# Create your models here.

class Reading(models.Model):
    number = models.IntegerField()
    observation_time = models.CharField(max_length=50)
    is_daytime = models.CharField(max_length=50)
    temperature = models.IntegerField()
    temperature_unit = models.CharField(max_length=50)
    wind_speed = models.CharField(max_length=50)
    wind_direction = models.CharField(max_length=50)
    icon_url = models.URLField()
    short_forecast = models.CharField(max_length=50)
    detailed_forecast = models.CharField(max_length=150)
