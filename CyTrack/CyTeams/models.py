from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=30, blank=False)
    des = models.CharField(max_length=150, blank=True)
    members = ArrayField(
        ArrayField(
            models.CharField(max_length=30, blank=True),
            size=2,  # This is going to be Source Time Lat Lon Alt
        )
    )
    checklistNames = ArrayField(
        models.CharField(max_length=80, blank=True)
    )
    checklists = ArrayField(
        ArrayField(
            models.CharField(max_length=30, blank=True),
            size=5,  # This is going to be Source Time Lat Lon Alt
        )
    )
    missions = ArrayField(models.CharField(max_length=30, blank=True))
    trainings = ArrayField(
        ArrayField(
            models.CharField(max_length=30, blank=True),
            size=2,  # This is going to be Source Time Lat Lon Alt
        )
    )


class Mission(models.Model):
    # This class will contain all of the mission specific information.
    # This will just hold some of the basic info about what the mission
    # will be doing but nothing beyond that will be stored
    ID = models.CharField(max_length=10, blank=False),
    des = models.CharField(max_length=150, blank=True)
    flights = ArrayField(models.CharField(max_length=30, blank=True))
    checklistNames = ArrayField(
        models.CharField(max_length=80, blank=True)
    )
    checklists = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=5,  # This is going to be Source Time Lat Lon Alt
        )
    )


class Flights(models.Model):
    ID = models.CharField(max_length=10, blank=False),
    des = models.CharField(max_length=150, blank=True)
    flightDate = models.DateTimeField(auto_now=False)
    flightPerams = JSONField()  # Flight specific perameters like mass
    members = ArrayField(  # This will be member name and role
        ArrayField(
            models.CharField(max_length=30, blank=True),
            size=2,  # This is going to be Source Time Lat Lon Alt
        )
    )
    checklistNames = ArrayField(
        models.CharField(max_length=80, blank=True)
    )
    checklists = ArrayField(  # This is checklist name and checklist item
        ArrayField(
            models.CharField(max_length=30, blank=True),
            size=2,  # This is going to be Source Time Lat Lon Alt
        )
    )
    flightPositionData = ArrayField(
        ArrayField(
            models.CharField(max_length=50, blank=True),
            size=5,  # This is going to be Source Time Lat Lon Alt
        )
    )
