from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from CyTracking.models import singleFlight
import json
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
    flight = singleFlight(IDs = flightID, flightPositionData = [["","","","","",""]], dataAdded = 'False')
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
        print("dataAdded: "+flight.dataAdded)
        try:
            if flight.dataAdded == 'False':
                flight.flightPositionData.append([scriptID, time, lat, lon, alt, rssi])
                flight.dataAdded = 'True'
                flight.save()
            else:
                flight.flightPositionData = [[scriptID, time, lat, lon, alt, rssi]]
                
        except:
            flight.flightPositionData = [[scriptID, time, lat, lon, alt, rssi]]
            flight.dataAdded = 'True'
            data = {'response': 'flight data wasnt set yet'}
            flight.save()
            return JsonResponse(data)
        flight.save()
        data = {'response': 'acepted'}
    except:
        data = {'response': 'REJECTED'}
    return JsonResponse(data)

@csrf_exempt 
def AddFlightJsonData(request):
    scriptID = str(request.POST.get('scriptID'))
    flightID = str(request.POST.get('flightID'))
    gpsDat = str(request.POST.get('gps'))
    jsonDat = {'scriptID': scriptID, 'flightID': flightID, 'gpsDat':gpsDat}
    
    print("test")
    print(jsonDat)
    #jsonDat = json.loads(jsonDat)
    data = {}
    try:
        flight = singleFlight.objects.get(IDs = flightID)
        print(flight)
        print(flight.IDs)
        if flight.flightData is None:
            flight.flightData = str([jsonDat])
            
        else:
            flight.flightData.append(str(jsonDat))
        flight.save()
        data = {'response': 'acepted'}
    except Exception as e:
        print(e)
        data = {'response': 'REJECTED'}
    return JsonResponse(data)


#@csrf_exempt 
#def AddFlightData(request):
#    scriptID = str(request.POST.get('scriptID'))
#    flightID = str(request.POST.get('flightID'))
#    time = str(request.POST.get('time'))
#    lat = str(request.POST.get('lat'))
#    lon = str(request.POST.get('lon'))
#    alt = str(request.POST.get('alt'))
#    rssi = str(request.POST.get('rssi'))
#    print(rssi)
#    data = {}
#    try:
#        flight = singleFlight.objects.get(IDs = flightID)
#        print(flight)
#        print(flight.IDs)
#        if flight.flightPositionData[0][0] == "":
#            flight.flightPositionData.append([scriptID, time, lat, lon, alt, rssi])
#        else:
#            flight.flightPositionData = [[scriptID, time, lat, lon, alt, rssi]]
#        flight.save()
#        data = {'response': 'acepted'}
#    except:
#        data = {'response': 'REJECTED'}
#    return JsonResponse(data)


@csrf_exempt 
def GetFlightPath(request,uuid):
    flightID = uuid
    flight = singleFlight.objects.get(IDs = flightID)
    data = flight.flightPositionData
    data.pop(0)
    retDat = []
    timesec = int(data[0][1])
    for dat in data:
        retDat.append(int(dat[1])-timesec)
        retDat.append(float(dat[3]))
        retDat.append(float(dat[2]))
        retDat.append(float(dat[4]))
    return JsonResponse({'dat':retDat})


@csrf_exempt 
def GetFlightPathArray(request,uuid):
    flightID = uuid
    print(uuid)
    flight = singleFlight.objects.get(IDs = flightID)
    data = flight.flightPositionData
    data.pop(0)
    retDat = []
    print(data[0])
    timesec = int(data[0][1])
    for dat in data:
        try:
            #print(dat)
            retDat.append(dat)
            #retDat.append([int(dat[1])-timesec, float(dat[3]), float(dat[2]), float(dat[4]), float(dat[5])])
        except Exception as e:
            print(e)
    print("Returning Flight")
    return JsonResponse({'dat':retDat})

@csrf_exempt 
def GetFlightDataArray(request,uuid):
    flightID = uuid
    print(uuid)
    flight = singleFlight.objects.get(IDs = flightID)
    data = flight.flightData
    data.pop(0)
    retDat = []
    print(data[0])
    print("Returning Flight")
    return JsonResponse({'dat':data})


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
