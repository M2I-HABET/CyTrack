from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib import admin
# Create your models here.


class singleFlight(models.Model):
    IDs = models.CharField(max_length=36, blank=False, default = 0)
    flightPositionData = ArrayField(
        ArrayField(
            models.CharField(max_length=100, blank=True),
            size=6,  # This is going to be Source Time Lat Lon Alt
        ),blank=True
    )
