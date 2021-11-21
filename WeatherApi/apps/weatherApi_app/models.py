# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CityWeatherModel(models.Model):
    city  = models.CharField(max_length=45, default="Enter in the city name")
    list = models.CharField(max_length=50)

# class CityWeatherModel(models.Model):
#     name = models.CharField(max_length=45, default="Enter in the city name")
#     main = models.CharField(max_length=50)
#     day = models.FloatField()
#     max = models.FloatField()
#     min = models.FloatField()
#     humidity = models.FloatField()
#     description = models.CharField(max_length=100)
