'''
Created on Sep 25, 2016

@author: matth
'''

from CyPredict.predictor.Predictor.LatexPrediction import LatexHAB

def predict():
    tStep=15
    pre = LatexHAB(tStep)
    
    # setValues(self,time,lat,lon,altitude,mass,lift,pArea,pcd,bmass,bcd):
    
    pre.setValues(2019,"Jan",30,18,0, 42.0308, -93.6319, -0, 3.0, 4.667, 2.0, 1.5, 1200, .25)
    
    values = pre.runPrediction()
     
    # https://www.darrinward.com/lat-long/?id=2679280
    print("done")
    return values