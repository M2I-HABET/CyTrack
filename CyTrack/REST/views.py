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
    flight = singleFlight(IDs = flightID, flightPositionData = [["","","","","",""]])
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
    rssi = str(request.POST.get('rssi'))
    data = {}
    try:
        flight = singleFlight.objects.get(IDs = flightID)
        print(flight)
        print(flight.IDs)
        if flight.flightPositionData[0][0] == "":
            flight.flightPositionData.append([scriptID, time, lat, lon, alt, rssi])
        else:
            flight.flightPositionData = [[scriptID, time, lat, lon, alt, rssi]]
        flight.save()
        data = {'response': 'acepted'}
    except:
        data = {'response': 'REJECTED'}
    return JsonResponse(data)

@csrf_exempt 
def GetFlightPath(request,uuid):
    flightID = uuid
    print(uuid)
    flight = singleFlight.objects.get(IDs = flightID)
    data = flight.flightPositionData
    data.pop(0)
    retDat = []
    print(data[0])
    timesec = int(data[0][1])
    for dat in data:
        retDat.append(int(dat[1])-timesec)
        retDat.append(float(dat[3]))
        retDat.append(float(dat[2]))
        retDat.append(float(dat[4]))
    print("Returning Flight")
    return JsonResponse({'dat':retDat})

@csrf_exempt 
def GetFlightPos(request,uuid):
    flightID = uuid
    print(uuid)
    flight = singleFlight.objects.get(IDs = flightID)
    data = flight.flightPositionData
    idx = len(data)-1
    dat = data[idx]
    lat = dat[2]
    lon = dat[3]
    alt = dat[4]
    
    print("Returning Flight")
    return JsonResponse({'lat':lat, 'lon':lon, 'alt':alt})
