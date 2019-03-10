from django.shortcuts import render
from CyPredict.predictor.Predictor.LatexPrediction import LatexHAB
from django.contrib.auth.decorators import login_required
import xml.etree.ElementTree as ET
from django.http import HttpResponseRedirect
#import requests
#import pandas as pd
# Create your views here.

@login_required
def predictionOutPut(request):
    numkeys = 0
    for key in request.POST:
        numkeys = numkeys + 1
    print(numkeys)
    if numkeys != 14:
        return HttpResponseRedirect('../')
    year = int(request.POST.get("year"))
    month = request.POST.get("month")
    day = int(request.POST.get("day"))
    hour = int(request.POST.get("hour"))
    minute = int(request.POST.get("min"))
    lat = float(request.POST.get("lat"))
    lon = float(request.POST.get("lon"))
    altitude = int(request.POST.get("altitude"))
    mass = float(request.POST.get("mass"))
    lift = float(request.POST.get("lift"))
    pArea = float(request.POST.get("pArea"))
    pcd = float(request.POST.get("pcd"))
    bmass = float(request.POST.get("bmass"))
    tStep = 15
    pre = LatexHAB(tStep)
    dateString = str(month)+" "+str(day)+", "+str(year)+" "+str(hour)+":"+str(minute)+":00 UTC"
    print(dateString)
    pre.setValues(dateString,lat,lon,altitude,mass,lift,pArea,pcd,bmass)
    results = pre.runPrediction()
    del pre
    print(results[0])
    print(results[1])
    print(results[2])
    return render(request, 'CyPredict/predict.html', {'results': results[3],'results2': results[4], "burst_lat": results[2][1], "burst_lon": results[2][0], "burst_alt": results[2][2]})
    #return render(request, 'CyPredict/predict.html', {'results': results[3],'results2': results[4], "burst_lat": int(results[2][1]*10000)/10000.0, "burst_lon": int(results[2][0]*10000)/10000.0, "burst_alt": int(results[2][2]*10000)/10000.0})

@login_required
def getParams(request):
    
    return render(request, 'CyPredict/getperams.html')


# Helper Functions

#def get_elevation(lat, long):
#    query = ('https://api.open-elevation.com/api/v1/lookup?locations='+str(lat)+','+str(long))
#    r = requests.get(query).json()  # json object, various ways you can extract value
#    # one approach is to use pandas json functionality:
#    elevation = pd.io.json.json_normalize(r, 'results')['elevation'].values[0]
#    print(elevation)
#    return elevation