from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib import admin
# Create your models here.


class singleFlight(models.Model):
    IDs = models.CharField(max_length=36, blank=False, default = 0)
    flightPositionData = ArrayField(
        ArrayField(
            models.CharField(max_length=50, blank=True),
            size=5,  # This is going to be Source Time Lat Lon Alt
        ),null=True
    )
