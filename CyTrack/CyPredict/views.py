from django.shortcuts import render
from CyPredict.predictor.Predictor.LatexPrediction import LatexHAB
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def maps(request):
    tStep = 15
    pre = LatexHAB(tStep)
    pre.setValues(2019, "Jan", 31, 18, 0, 42.0308, -93.6319, -0,
                  3.0, 4.667, 2.0, 1.5, 1200, .25)
    results = pre.runPrediction()
    del pre
    return render(request, 'CyPredict/predict.html', {'results': results})
