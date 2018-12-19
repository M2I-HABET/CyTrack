'''
Created on Nov 12, 2016

@author: matth
'''
from AntennaControl import gpsParser

#TODO chang so that there is only one class that initializes based off of an init file

class SerialController(object):
    '''
    classdocs
    '''
    azimuth = 0
    zenith = 0
    gps = gpsParser()

    def __init__(self):
        '''
        Constructor
        '''
    
    def getCurrentAzimuth(self):
        return self.azimuth
    def getCurrentZenith(self):
        return self.zenith
    def setAzimuth(self, azimuth):
        self.azimuth = azimuth
        return
    def setZenith(self, zenith):
        self.zenith = zenith
        return
    #returned in the format a,(azimuth),b,zenith in which it is separated in ,
    def getCurrentDataString(self):
        return "a,"+str(self.azimuth) + ",b," + str(self.zenith)
    def adjustPointing(self):
        self.zenith = self.gps.getZenith()
        self.azimuth = self.gps.getAzimuth()
        return "a,"  + str(self.azimuth) + ",b," + str(self.zenith)
        
        
    