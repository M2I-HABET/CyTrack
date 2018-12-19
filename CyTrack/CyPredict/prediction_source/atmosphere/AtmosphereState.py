'''
A representation of the conditions of the atmosphere.
Units are managed by the user.

@author: adapted by DGXU
'''
class AtmosphereState:

    h = 0.0
    p = 0.0
    t = 0.0
    dp = 0.0
    wd = 0.0
    ws = 0.0

    #create new state.
    def __init__(self, altitude, pressure, temperature, dewPoint, windDirection, windSpeed):
         self.h = altitude
         self.p = pressure
         self.t = temperature
         self.dp = dewPoint
         self.wd = windDirection
         self.ws = windSpeed

    #Get the altitude of this state.
    def getAltitude(self):
        return self.h

    #Get the pressure of this state.
    def getPressure(self):
        return self.p

    #Get the temperature of the state.
    def getTemperature(self):
        return self.t

    #Get the dew point of the state.
    def getDewPoint(self):
        return self.dp

    #Get the wind speed of this state.
    def getWindSpeed(self):
        return self.ws

    #Get wind direction of this state.
    def getWindDirection(self):
        return self.wd

    #Compare the altitude of the given object to this object.
    def compareTo(self, x):
        if(self.h < x.h ):
            return -1;
        if(self.h > x.h):
            return 1;
        return 0;

    #get the human readable representation of this state.
    def toString(self):
        return "@" + str(self.h) + "m: " + str(self.p) + "Pa, " + str(self.t) + "C, " + str(self.dp) + "C, " + str(self.ws) + "m/s from " + str(self.wd) + "deg"
