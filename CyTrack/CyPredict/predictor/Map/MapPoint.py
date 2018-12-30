class MapPath(object):
    lat = 0.0
    long = 0.0
    alt = 0.0
    time = 0.0
    name = ""
    
    def __init__(self, lat, long, alt, time, name):
        self.lat = lat
        self.long = long
        self.alt = alt
        self.time = time
        self.name = name
    
    def getLat(self):
        return self.lat
    
    def setLat(self, lat):
        self.lat = lat
        
    def getLong(self):
        return self.long
    
    def setLong(self, long):
        self.long = long
        
    def getAlt(self):
        return self.alt
    
    def setAlt(self, alt):
        self.alt = alt
        
    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        
    def toString(self):
        return self.name + ": " + self.lat + ", " + self.lon + ", " + self.alt + ", " + self.time
        