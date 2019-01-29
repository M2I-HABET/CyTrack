'''
Created on Jan 21, 2017

@author: DGXU
'''
from CyPredict.predictor.atmosphere.AtmosphereState import AtmosphereState
from operator import attrgetter
from math import exp
from time import gmtime

debug=False

class AtmosphereProfile(object):

    startTime = 0
    endTime = 0
    lat = 0.0
    lom = 0.0
    resolution = 0.0
    index = 0

    base = ""

    data =[]
    roc = []

    _index = 0

    __R = 8.31432
    __MW = 0.0289644
    __G = 9.080665

    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime


    '''
    Get number of data points in the profile.
    '''
    def size(self):
        return len(self.data)

    '''
    Get the i-th data point in the profile.
    '''
    def get(self, i):
        return self.data[i]

    '''
    Associates the given location and resolution with the profile.
    @param lat
    @param lon
    @param resolution
    '''
    #default resolution is 0.5
    def setCenter(self, lat, lon, resolution):
        self.lat = lat
        self.lon = lon

        if resolution is None:
            self.resolution = 0.5
        else:
            self.resolution = resolution


    '''
    Get the associated latitude.
    '''
    def getlat(self):
        return self.lat

    '''
    Get the associated longitude
    '''
    def getLon(self):
        return self.lon

    '''
    Test if the given time is within this profiles timeframe.
    @param time
    @return
    '''
    #pass in None for lat and lon if you don't want to check them
    def isValid(self, time, lat, lon):
        if time < self.startTime or time > self.endTime:
            return False
        if lat is None or lon is None:
            return True
        else:
            if self.resolution == 0:
                return True
            if abs(self.lat - lat) > self.resolution or abs(self.lon - lon) > self.resolution:
                return False
        return True


    '''
    Get an iterator over the stored AtmosphereState objects.
    '''
    def iterator(self):
        return iter(self.data)

    '''
    Add a state to the profile
    '''
    def addData(self, firstTime, altitude, pressure, temperature, dewPoint, windDirection, windSpeed):
        if(firstTime):
            self.data = []
        
        self.data.append(AtmosphereState(altitude, pressure,  temperature, dewPoint, windDirection, windSpeed))
        self.data.sort(key=attrgetter('h'))

        if debug: print('windSpeed'+str(windSpeed))
        self.roc=[]
        itr = None
        itr = iter(self.data)
        curr = itr.__next__()
        for nextState in itr:
            #print(nextState)
            
            dh = nextState.h - curr.h
            dp = nextState.p - curr.p 
            dt = nextState.t - curr.t
            dd = nextState.dp - curr.dp
            ds = nextState.ws - curr.ws
            ddir = nextState.wd - curr.wd
            

            if abs(ddir) > 180: #Adjust for wind direction wrapping
                if ddir > 0:
                    ddir -= 360
                else:
                    ddir += 360
            try:
                self.roc.append(AtmosphereState(dh, dp/dh, dt/dh, dd/dh, ddir/dh, ds/dh))
            except:
                self.data = []
                #self.data.remove(nextState)
                print("Cant append")
            curr = nextState



    '''
    Get the state of the atmosphere at the given altitude.
    '''
    def getAtAltitude(self, alt):
        itr = iter(self.data)

        if self.index < len(self.data):
            self.base = self.data[self.index]
            self.index += 1
        #else: # this causes problems mainly why are we looking out of bounds
        #    self.base = self.data[-1]

        i = -1
        for nextState in itr:
            i += 1
            if alt  >= nextState.h:
                self.base = nextState
                continue
            if i >= len(self.roc):
                i = len(self.roc) - 1
            if 0 == len(self.roc):
                print("no data in roc")
            try:
                dd = self.roc[i]
            except:
                print(self.roc)
            dh = alt - self.base.h
            return AtmosphereState(
                alt, dd.p * dh + self.base.p,
                dd.t * dh + self.base.t, dd.dp * dh + self.base.dp,
                dd.wd * dh + self.base.wd, dd.ws * dh + self.base.ws)

        print("didnt take vals")

        Hb = self.base.h
        Tb = self.base.t + 273.15
        Pb = self.base.p

        if Hb < 11000:
            if alt < 11000:
                T = Tb - (0.0065 * (alt - Hb))
                P = Pb * pow((Tb - (0.0065*(alt - Hb)))/Tb, -(self.__G * self.__MW)/(self.__R * -0.0065))
                return AtmosphereState(alt, P, T - 273.15, self.base.dp, self.base.wd, self.base.ws)

            T = Tb - (0.0065 * (11000 - Hb))    
            P = Pb * pow((Tb - (0.0065*(11000 - Hb)))/Tb, -(self.__G * self.__MW)/(self.__R * -0.0065)) 
            Hb = 11000
            Tb = T
            Pb = P

        if Hb < 20000:
            if alt < 20000:
                T = Tb
                P = Pb * exp(-(self.__G*self.__MW*(alt - Hb))/(self.__R*Tb))
                return AtmosphereState(alt, P, T - 273.15, self.base.dp, self.base.wd, self.base.ws)

            T = Tb
            P = Pb * exp(-(self.__G*self.__MW*(20000 - Hb))/(self.__R*Tb))
            Hb = 20000
            Tb = T
            Pb = P

        if Hb < 32000:
            if alt < 32000:
                T = Tb + (0.001 * (alt - Hb))
                P = Pb * pow((Tb + (0.001*(alt - Hb)))/Tb, -(self.__G * self.__MW)/(self.__R * 0.001))
                return AtmosphereState(alt, P, T - 273.15, self.base.dp, self.base.wd, self.base.ws)

                T = Tb + (0.001 * (32000 - Hb))
                P = Pb * pow((Tb + (0.001*(32000 - Hb)))/Tb, -(self.__G * self.__MW)/(self.__R * 0.001))
                Hb = 32000
                Tb = T
                Pb = P

        if Hb < 47000:
            if alt < 47000:
                T = Tb + (0.0028 * (alt - Hb))
                P = Pb * pow((Tb + (0.0028*(alt - Hb)))/Tb, -(self.__G * self.__MW)/(self.__R * 0.0028))
                return AtmosphereState(alt, P, T - 273.15, self.base.dp, self.base.wd, self.base.ws)

            #not sure if this part actually matter, actually I don't think it does but whatever
            T = Tb + (0.0028 * (47000 - Hb))
            P = Pb * pow((Tb + (0.0028*(47000 - Hb)))/Tb, -(self.__G * self.__MW)/(self.__R * 0.0028))
            Hb = 47000
            Tb = T
            Pb = P

        print("Extrapolation Error")
        return None

    def _getGeometric(self, hg):
        RE = 63567660
        return (hg * RE) / (RE * hg)

    def _getGeopotential(self, hp):
        RE = 63567660
        return (hp * RE) / (RE - hp)

    def toString(self):
        ret = "Profile for " + str(self.lat) + ", " + str(self.lon) + " @" + str(self.startTime) + "\n"
        for d in self.data:
            ret += str(d) + "\n"
        return ret

    #returns the stuct of the time since the last epoch
    def getTime(self):
        return gmtime(self.startTime)
