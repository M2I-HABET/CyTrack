from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib import admin
from datetime import datetime
# Create your models here.


class singleFlight(models.Model):
    IDs = models.CharField(max_length=36, blank=False, default = 0)
    dataAdded = models.CharField(max_length=10,blank=False,default = "True")
    #Desc = models.CharField(max_length=50, blank=True, default = "Old Flight Data")
    flightDate = models.DateTimeField(default=datetime.now(),null=True, blank=True)
    flightPositionData = ArrayField(
        ArrayField(
            models.CharField(max_length=100, blank=True),
            size=6,  # This is going to be Source Time Lat Lon Alt
        ),blank=True
    )
    flightData = ArrayField(
        models.CharField(max_length=1000, blank=True),
        blank=True, default = list
    )

    
