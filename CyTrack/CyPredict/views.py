from django.shortcuts import render
from CyPredict.predictor.Predictor.LatexPrediction import LatexHAB
from django.contrib.auth.decorators import login_required
import xml.etree.ElementTree as ET
from django.http import HttpResponseRedirect
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
    # 2019, "Jan", 31, 18, 0, 42.0308, -93.6319, -0,3.0, 4.667, 2.0, 1.5, 2000
    # year,month,day,hour,minute,lat,lon,altitude,mass,lift,pArea,pcd,bmass
    pre.setValues(year,month,day,hour,minute,lat,lon,altitude,mass,lift,pArea,pcd,bmass)
    results = pre.runPrediction()
    del pre
    print(results[0])
    print(results[1])
    print(results[2])
    return render(request, 'CyPredict/predict.html', {'results': results[3]})

@login_required
def getParams(request):
    
    return render(request, 'CyPredict/getperams.html')
