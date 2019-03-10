from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class predictions(models.Model):
    uuidVal = models.CharField(max_length=36)
    yearVal = models.IntegerField()
    monthVal = models.CharField(max_length=15)
    dayVal = models.IntegerField()
    hourVal = models.IntegerField()
    minuteVal = models.IntegerField()
    latVal = models.FloatField()
    lonVal = models.FloatField()
    altitudeVal = models.IntegerField()
    massVal = models.FloatField()
    liftVal = models.FloatField()
    pAreaVal = models.FloatField()
    pcdVal = models.FloatField()
    bmassVal = models.FloatField()
    path = ArrayField(
        models.CharField(max_length=100, blank=True)
    )
    # burst perams
    btime = models.IntegerField()
    blat = models.FloatField()
    blon = models.FloatField()
    balt = models.FloatField()
