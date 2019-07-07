from django.shortcuts import render
from CyTracking.models import singleFlight

# Create your views here.


def maps(request):
    flightID = "affe44f5-3ec6-454d-a3ba-c9452b0d69e5"
    flight = singleFlight.objects.get(IDs = flightID)
    print(flight.flightPositionData)
    return render(request, 'CyTrack/track.html')
