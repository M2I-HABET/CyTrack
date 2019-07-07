from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from CyTracking.models import singleFlight
import uuid
# Create your views here.



def help(request):
    return render(request, 'CyTrack/track.html')
@csrf_exempt
def newFlight(request):
    flightID = uuid.uuid4()
    print(flightID)
    scriptID = uuid.uuid4()
    print(scriptID)
    flight = singleFlight(IDs = flightID)
    flight.save()
    data = {'flightID': flightID, 'scriptID': scriptID}
    return JsonResponse(data)
    

@csrf_exempt 
def AddFlightData(request):
    scriptID = str(request.POST.get('scriptID'))
    flightID = str(request.POST.get('flightID'))
    time = str(request.POST.get('time'))
    lat = str(request.POST.get('lat'))
    lon = str(request.POST.get('lon'))
    alt = str(request.POST.get('alt'))
    flight = singleFlight.objects.get(IDs = flightID)
    print(flight.IDs)
    if flight.flightPositionData:
        print("was made")
        print(flight.flightPositionData)
        flight.flightPositionData.append([scriptID, time, lat, lon, alt])
    else:
        flight.flightPositionData =[scriptID, time, lat, lon, alt]
        print(flight.flightPositionData)
    flight.save()
                

    print(lat)
    data = {'response': 'acepted'}
    return JsonResponse(data)
