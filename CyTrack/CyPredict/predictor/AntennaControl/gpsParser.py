'''
Created on Nov 12, 2016

@author: DGXU
adapted from http://cosinekitty.com/compass.html
'''
import Configuration.config as config
import math
class GPSParser(object):
    '''
    classdocs
    '''
    
    azimith=0
    zenith=0
   
    def __init__(self):
        '''
        Constructor
        '''
        
        
        
    def getTargetLatestLat(self):
        return
    
    def getTargetLatestLon(self):
        return 
    
    def getTargetLatestAlt(self):
        return 
    
    def getStationLatestLat(self):
        return config.stationLat
    
    def getStationLatestLon(self):
        return config.stationLat
    
    def getStationLatestAlt(self):
        return config.stationAlt
    
    
    def getAzmith(self):
        self.azimith=self.findAzmith()
        return self.azimith
    
    
    def getZenith(self):
        self.zenith = self.findZenith()
        return self.zenith
    
    def findAzimith(self):
        oblate = True
        a = {'lat': self.getStationLatestLat(), 'lon':self.getStationLatestLon(), 'elv':self.getStationLatestAlt()}
        b = {'lat': self.getTargetLatestLat(), 'lon':self.getTargetLatestLon(), 'elv':self.getTargetLatestAlt()}
        
        ap = self.locationToPoint(a, oblate)
        bp = self.locationToPoint(b, oblate)
        
        br = self.rotateGlobe(b, a, bp['radius'], ap['radius'], oblate)
        
        if(br['z']*br['z'] + br['y']*br['y'] > 0.0000001):
            theta = math.atan2(br['z'], br['y']) * 180.0 /math.pi
            azimuth = 90.0 -theta;
            if(azimuth < 0.0):
                azimuth += 360.0
            if(azimuth > 360.0):
                azimuth -= 360.0
                
        return azimuth
    
    def findZenith(self):
        oblate = True
        a = {'lat': self.getStationLatestLat(), 'lon':self.getStationLatestLon(), 'elv':self.getStationLatestAlt()}
        b = {'lat': self.getTargetLatestLat(), 'lon':self.getTargetLatestLon(), 'elv':self.getTargetLatestAlt()}
        
        ap = self.locationToPoint(a, oblate)
        bp = self.locationToPoint(b, oblate)
        
        bma = self.normalizeVectorDiff(bp, ap)
        
        altitude = 90.0 - (180.0 / math.pi)*math.acos(bma['x']*ap['nx'] + bma['y']*ap['ny'] + bma['z']*ap['nz']);
        
        return altitude
    
    def earthRadiusInMeters(self, latRad):
        
        a = 6378137.0 
        b = 6356752.3
        cos = math.cos(latRad)
        sin = math.sin(latRad)
        t1 = a * a * cos;
        t2 = b * b * sin;
        t3 = a * cos;
        t4 = b * sin;
        return math.sqrt((t1*t1+t2+t2)/(t3*t3+t4*t4))
        
    def geocentricLatitude(self, lat):
        e2 = 0.00669437999014
        return math.atan(1.0- e2) * math.tan(lat)

    def locationToPoint(self, c, oblate):
        lat = c['lat'] * math.pi / 180.0
        lon = c['lon'] * math.pi / 180.0
        
        radius = self.earthRadiusInMeters(lat) if oblate else 6371009.0
        clat = self.geocentricLatitude(lat) if oblate else lat
        
        cosLon = math.cos(lon);
        sinLon = math.sin(lon);
        cosLat = math.cos(clat);
        sinLat = math.sin(clat);
        x = radius * cosLon * cosLat;
        y = radius * sinLon * cosLat;
        z = radius * sinLat;
        
        cosGlat = math.cos(lat)
        sinGlat = math.sin(lat)
        
        nx = cosGlat * cosLon;
        ny = cosGlat * sinLon;
        nz = sinGlat;
        
        x += c['elv'] * nx;
        y += c['elv'] * ny;
        z += c['elv'] * nz;
        
        return {'x':x, 'y':y, 'z':z, 'radius':radius, 'nx':nx, 'ny':ny, 'nz':nz}
        
    def distance(self, ap, bp):
        dx = ap['x'] - bp['x'];
        dy = ap['y'] - bp['y'];
        dz = ap['z'] - bp['z'];
        return math.sqrt (dx*dx + dy*dy + dz*dz);
        
    def rotateGlobe(self, b, a, bradius, aradius, oblate):
        br = {'lat':b['lat'], 'lon':(b['lon'] - a['lon']), 'elv':b['elv']}
        brp = self.locationToPoint(br, oblate)
        
        alat = -a['lat'] * math.pi / 180.0
        if(oblate):
            alat = self.geocentricLatitude(alat)
        acos = math.cos(alat)
        asin = math.sin(alat)
        
        bx = (brp['x'] * acos) - (brp['z'] * asin)
        by = brp['y']
        bz = (brp['x']* asin) + (brp['z'] * acos)

        return {'x':bx, 'y':by, 'z':bz, 'radius':bradius};
    def normalizeVectorDiff(self, b, a):
        dx = b['x'] - a['x']
        dy = b['y'] - a['y']
        dz = b['z'] - a['z']
        dist2 = dx*dx + dy*dy + dz*dz
        if (dist2 == 0):
            return
        
        dist = math.sqrt(dist2)
        return { 'x':(dx/dist), 'y':(dy/dist), 'z':(dz/dist), 'radius':1.0 }
  