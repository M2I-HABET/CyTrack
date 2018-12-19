'''
Created on Sep 25, 2016

@author: matth
'''


#from connector.serialData import Serial
from APRSDecoder.decodeAPRS import APRSDecoder
import AppLogger.LoggerINIT 

from Predictor.LatexPrediction import LatexHAB

#from time import sleep
    
if __name__ == '__main__':
    '''
    baud=9600
    portname="COM13"    
    a=Serial(portname,baud)
    a.startSerialDat()
    sleep(2)
    a.writeToPort("test")
    sleep(10)
    print(a.getFromPort())
    a.stopSerialDat()
    
    AppLogger.LoggerINIT.initialize_Logger()
    
    a=APRSDecoder()
    a.setString("W0ISU-11>APOTU0,TCPIP*,qAS,W0ISU:/135340h/9<uw6u^rO:SG/A=049854 11.6V 45F HDOP01.0 SATS08 ISU HABET L-139-B")
    
    a.setString("W0ISU-11>APOTU0,TCPIP*,qAS,W0ISU:/153927h/9=e06p{8O*;G/A=090958 11.0V 74F HDOP01.3 SATS09 ISU HABET L-139-B")
    a.parseString()
    thing=a.getParsed()
    print(thing)
    
    
    '''
    tStep=15
    
    
    pre = LatexHAB(tStep)
    
    #setValues(self,time,lat,lon,altitude,mass,lift,pArea,pcd,bmass,bcd):
    
    pre.setValues('December 19, 2018 16:30:00 US/Central', 42.0308, -93.6319, -0, 3.0, 4.667, 2.0, 1.5, 1200, .25)
    
    pre.runPrediction()
     
    #https://www.darrinward.com/lat-long/?id=2679280
    print("done")
    
    
     



    