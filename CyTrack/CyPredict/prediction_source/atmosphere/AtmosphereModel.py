'''
Created on Jan 21, 2017

@author: translated DGXU

A representation of the atmosphere that interpolates between two atmosphere profiles.
'''

from atmosphere import AtmosphereProfile, AtmosphereState



class AtmosphereModel(object):
    startTime = 0
    endTime = 0
    lat = 0.0
    lon = 0.0
    resolution = 0.0
    
    start = AtmosphereProfile()
    end = AtmosphereProfile()
    
    #condensed it to one constructor
    def __init__(self, startTime, endTime, lat, lon, resolution):
        self.startTime = startTime
        self.endTime = endTime
        self.lat = lat
        self.lon = lon
        self.resolution = resolution
        
    #PLEASE READ: if you are not considering lat an lon just set them to 'None' when you pass them in
    def isValid(self, time, lat, lon):
        if time < self.startTime or time > self.endTime:
            return False
        if lat == None or lon == None:
            return True
        else:
            if self.resolution == 0.0:
                return True
            if abs(self.lat-lat) > self.resolution or abs(self.lon-lon) > self.resolution:
                return False
            else:
                return True
                
    def getAtAltitude(self, time, alt):
        #TODO might need to change this to a different constructor
        startState = self.start.getAtAltitude(alt)
        endState = self.end.getAtAltitude(alt)
        
        tStep = self.endTime - self.startTime
        deltaT = time - self.startTime
        dt = deltaT / tStep
        
        p = (endState.p - startState.p) * dt + startState.p
        t = (endState.t - startState.t) * dt + startState.t
        d = (endState.dp - startState.dp) * dt + startState.dp
        spd = (endState.ws - startState.ws) * dt + startState.ws
        ddir = endState.wd - startState.wd
        
        if abs(ddir) > 180:
            if ddir > 0:
                ddir = ddir - 360
            else:
                ddir = ddir + 360
                
        dir = ddir * dt + startState.wd
        
        return AtmosphereState(alt, p, t, d, dir, spd)
        