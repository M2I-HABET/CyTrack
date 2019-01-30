from django.shortcuts import render
from CyPredict.predictor.Predictor.LatexPrediction import LatexHAB
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def predictionOutPut(request):
    year=request.POST.get("year", '')
    print("Checking")
    print("year"+str(year)) 
    #month
    #day
    #hour
    #minute
    #lat
    #lon
    #altitude
    #mass
    #lift
    #pArea
    #pcd
    #bmass
    tStep = 15
    pre = LatexHAB(tStep)
    # year,month,day,hour,minute,lat,lon,altitude,mass,lift,pArea,pcd,bmass
    pre.setValues(2019, "Jan", 31, 18, 0, 42.0308, -93.6319, -0,
                  3.0, 4.667, 2.0, 1.5, 2000)
    results = pre.runPrediction()
    del pre
    print(results[0])
    print(results[1])
    print(results[2])
    return render(request, 'CyPredict/predict.html', {'results': results[3]})

@login_required
def getParams(request):
    
    return render(request, 'CyPredict/getperams.html')
