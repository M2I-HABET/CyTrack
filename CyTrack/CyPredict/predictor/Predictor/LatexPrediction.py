import os, shutil
import datetime
from DateTime import DateTime 
import math 
#from copy import deepcopy
from CyPredict.predictor.atmosphere.RUCGFS import RUCGFS 
from CyPredict.predictor.atmosphere.GSDParser import GSDParser

import geopy as geopy
from geopy.distance import VincentyDistance
debug=False
cesium=True


class LatexHAB(object):
    balloonName = None
    
    startTime = 0.0
    startLat = 0.0
    startLon = 0.0
    startAlt = 0.0
    groundLevel = 0.0
    isAscending = True
    tStep = 15
    
    payloadMass = 0.0
    balloonLift = 0.0
    parachuteArea = 0.0 
    parachuteDrag = 0.0
    balloonMass = 0.0 
    balloonDrag = 0.0 
    burstRad = 0.0
    
    burst = [0, 0, 0];  #MapPoint
    landing = 0.0; #MapPoint
    
    RHOG = 0.1762  # kg/m^3 (Helium)
    RHO = 1.276    # kg/m^3 (Air)
    R = 8.31432
    MWGAS = 0.004002602
    NWAIR = 0.0289644
    
    balloons = ["Kaymont 200", "Kaymont 300", "Kaymont 350",
                "Kaymont 600", "Kaymont 800", "Kaymont 1000",
                "Kaymont 1200", "Kaymont 1500", "Kaymont 2000",
                "Kaymont 3000"]
    
    balloonData = [
        [0.2,    1.524,    0.25],    # Kaymont 200
        [0.3,    1.981,    0.25],    # Kaymont 300
        [0.6,    3.048,    0.3],     # Kaymont 600
        [0.8,    3.505,    0.3],     # Kaymont 800
        [1.0,    3.962,    0.3],     # Kaymont 1000
        [1.2,    4.267,    0.25],    # Kaymont 1200
        [1.5,    4.724,    0.25],    # Kaymont 1500
        [2.0,    5.334,    0.25],    # Kaymont 2000
        [3.0,    6.553,    0.25]     # Kaymont 3000
    ]
     
    #This should work!  
    def __init__(self, step):
        self.tStep = step
    
    #This should work! 
    def toString(self):
        return self.balloonName + ": " + self.balloonLift + "kg neck lift"
    
    def setValues(self,time,lat,lon,altitude,mass,lift,pArea,pcd,bmass):
        
        '''
        time is in the form of 'Mar 9, 1997 13:45:00 UTC'
        '''
        dt = DateTime(time)
        self.parachuteDrag=pcd
        self.parachuteArea=pArea
        
        self.startTime= int(dt.millis());
        self.startTime=self.startTime/1000
        
        self.startLat=lat
        self.startLon=lon
        self.startAlt=altitude
        self.burst = [self.startLat,self.startLon,self.startAlt]
        self.payloadMass=mass
        self.balloonLift=lift
        self.parachuteArea=pArea
        self.balloonDrag=pcd
        self.balloonMass=bmass
        return
    
    def runPrediction(self,notBurst=True): #Returns a MapPath
        path = 0.0 #Should equal a mappath
        cesiumDat = []
        cesiumDat2 = []
        historical = False
        self.isAscending = notBurst # setting up so that we can do post burst
        RUC=RUCGFS()
        
        
        wind = RUC.getAtmosphere(self.startTime, int(self.startLat*10)/10.0, int(self.startLon*10)/10.0);
        
        for i in range(0,len(self.balloonData)-1):
            bDat=self.balloonData[i];
            if bDat[0]==self.balloonMass/1000:
                self.balloonMass = bDat[0];
                self.burstRad = bDat[1];
                self.balloonDrag = bDat[2];
                
                
            
        
        if historical:
            time = datetime.datetime.now()
            wind = os.path.join("c:\\Habet\\historical_data\\", time + ".txt")
        GSD=GSDParser()
        atmo = GSD.parseAtmosphere(wind,False);
        cwd = os.getcwd()
        folder = cwd+"\\wind\\"
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        
        if atmo == None:
            return None
        if atmo == 'invalid':
            print("NO DATA USA FUCKED OFF")
            return None
     
        curAscending = self.isAscending
        cLat = self.startLat
        cLon = self.startLon
        cAlt = self.startAlt
        eTime = 0.0
        dX = 0.0
        dY = 0.0
        
        volume = (self.balloonLift + self.balloonMass) / (self.RHO - self.RHOG);
        radius = math.pow((3.0 * volume) / (4 * math.pi), 1.0/3.0);
        area = math.pi * math.pow(radius, 2.0);
        ascentRate = math.pow(((self.balloonLift - self.payloadMass) * 9.81) / (0.5 * self.RHO * self.balloonDrag * area), 1.0/2.0);
        times=0
        accenttimes=0
        decenttimes=0
        while(curAscending==True):
            accenttimes+=1
            if debug: print('altitude',str(cAlt))
            if debug: print('assending')
            #Solve for motion
            state = atmo.getAtAltitude(cAlt)
            if debug: print('statewind:'+str(state.getWindSpeed()))
            windX = state.getWindSpeed() * math.sin(math.radians(state.getWindDirection() + 180.0));
            windY = state.getWindSpeed() * math.cos(math.radians(state.getWindDirection() + 180.0));
            if debug: print('windx:'+str(windX))
            if debug: print('windY:'+str(windY))
            dX += windX * self.tStep;
            dY += windY * self.tStep;
            cAlt += ascentRate * self.tStep;
            eTime += self.tStep;
            
            #Check for burst
            cRhoG = (state.getPressure() * self.MWGAS) / (self.R * (state.getTemperature() + 273.15));
            cRhoA = (state.getPressure() * self.NWAIR) / (self.R * (state.getTemperature() + 273.15));
            cV = (self.balloonLift + self.balloonMass) / (cRhoA - cRhoG);
            cR = math.pow((3.0 * cV) / (4.0 * math.pi), 1.0 / 3.0);
            
            if cR >= self.burstRad: 
                curAscending = False
                self.burst=[cLat, cLon, cAlt]
                break
            
            
            self.range = math.pow(math.pow(dX, 2.0) + math.pow(dY, 2.0), 0.5);
            if debug: print('range:'+str(self.range))
            self.bearing = math.atan2(dX, dY);
            # convert to standar bearing system
            
            self.bearing =self.bearing+math.pi
            
            
             
            if debug: print('curAscending:'+str(curAscending))
            if debug: print('current radius:'+str(cR))
            if debug: print('burst radius',self.burstRad)
            if debug: print('Dx:'+str(dX))
            if debug: print('Dy'+str(dY))
            if debug: print('bering'+str(self.bearing))
            #Convert to lat/lon
            
            #Point2D.Double cPos = directGeodesic(new Point2D.Double(startLon, startLat), bearing, range);
            
            
            
            origin=geopy.Point(self.startLat,self.startLon)
            destination = VincentyDistance(kilometers=self.range/1000).destination(origin, ((self.bearing+math.pi)*180/math.pi))
            
            cLat = destination.latitude;
            cLon = destination.longitude;
            if debug: print('lat:'+str(cLat))
            if debug: print('lon:'+str(cLon))
            
            if cesium:
                cesiumDat.append(str((accenttimes)*self.tStep)+','+str(int(cLon*10000)/10000)+','+str(int(cLat*10000)/10000)+','+str(int(cAlt))+',')
                cesiumDat2.append(str((accenttimes)*self.tStep)+','+str(int(cLon*10000)/10000)+','+str(int(cLat*10000)/10000)+',')
            if not cesium : print(str(cLat)+','+str(cLon))
            
        
        while cAlt > self.groundLevel:
            decenttimes+=1
            if debug: print('altitude',str(cAlt))
            if debug: print('falling')
            state = atmo.getAtAltitude(cAlt);
            windX = state.getWindSpeed() * math.sin(math.radians(state.getWindDirection() + 180.0));
            windY = state.getWindSpeed() * math.cos(math.radians(state.getWindDirection() + 180.0));
            if debug: print('windx'+str(windX))
            if debug: print('windy'+str(windY))
            dX += windX * self.tStep;
            dY += windY * self.tStep;
            cRhoA = (state.getPressure() * self.NWAIR) / (self.R * (state.getTemperature() + 273.15));
            if debug: print('cRhoA:'+str(self.parachuteDrag))
            descentRate = math.sqrt((self.payloadMass * 9.81) / (0.5 * cRhoA * self.parachuteArea * self.parachuteDrag));
            cAlt -= descentRate * self.tStep;
            eTime += self.tStep;
            
            #Convert to lat/lon
            self.range = math.pow(math.pow(dX, 2.0) + math.pow(dY, 2.0), 0.5);
            self.bearing = math.atan2(dX, dY);
            #Point2D.Double cPos = directGeodesic(new Point2D.Double(startLon, startLat), bearing, range);
            self.bearing =(self.bearing+math.pi)
          
            
            origin=geopy.Point(self.startLat,self.startLon)
            destination = VincentyDistance(kilometers=(self.range/1000.0)).destination(origin, ((self.bearing+math.pi)*180/math.pi))
            
            cLat = destination.latitude;
            cLon = destination.longitude;
            if debug: print('bering:'+str(self.bearing))
            if debug: print('range:'+str(self.range))
            if debug: print('clat:'+str(cLat))
            if debug: print('clon:'+str(cLon))
            if cesium :
                cesiumDat.append(str((accenttimes+decenttimes)*self.tStep)+','+str(int(cLon*10000)/10000)+','+str(int(cLat*10000)/10000)+','+str(int(cAlt))+',')
                cesiumDat2.append(str((accenttimes+decenttimes)*self.tStep)+','+str(int(cLon*10000)/10000)+','+str(int(cLat*10000)/10000)+',')
            if not cesium : print(str(cLat)+','+str(cLon))
            #Store
            #path.add(cLat, cLon, cAlt, self.self.startTime + math.round(eTime));
            
        #landing = new MapPoint(cLat, cLon, cAlt, self.startTime + Math.round(eTime), "Burst");
        times=accenttimes+decenttimes
        #print("burst: "+str(self.burst))
        #print("range: "+str(self.range))
        #print('Times: '+str(times))
        #print('AccentTimes: '+str(accenttimes))
        #print('DecentTimes: '+str(decenttimes))
        del atmo
        return [times, self.range, self.burst, cesiumDat, cesiumDat2];


    def getBurst(self): # Returns a MapPoint
        return self.burst
        
    def getLanding(self): #Returns a MapPoint
        return self.landing
    
    #This should work! 
    def setAscending(self, ascending):
        self.isAscending = ascending    
    
    #This should work! 
    def setGroundLevel(self, level):
        self.groundLevel = level
    
    def setStart(self, start): #Takes a MapPoint
        self.startLat = start.getLatitude();
        self.startLon = start.getLongitude();
        self.self.startTime = start.getTime();
        self.startAlt = start.getAltitude();
        
    def equals(self, aObject):
        if aObject == self:
            return True
        
        if object == None:
            return False
        
        #if !(o isinstance(obj, latexPredictor)):
        #return False
        obj = object
        
        if self.self.startTime == obj.self.startTime and \
            self.startLat == obj.startLat and \
            self.startLon == obj.startLon and \
            self.startAlt == obj.startAlt and \
            self.groundLevel == obj.groundLevel and \
            self.isAscending == obj.isAscending and \
            self.payloadMass == obj.payloadMass and \
            self.balloonLift == obj.balloonLift and \
            self.parachuteArea == obj.parachuteArea and \
            self.parachuteDrag == obj.parachuteDrag and \
            self.balloonMass == obj.balloonMass and \
            self.balloonDrag == obj.balloonDrag and \
            self.burstRad == obj.burstRad:
            
            return True
        
        return False
    
    def hashCode(self):
        ahash = 1;
        ahash = ahash * 31 + self.self.startTime.hashCode();
        ahash = ahash * 31 + self.startLat.hashCode();
        ahash = ahash * 31 + self.startLon.hashCode();
        ahash = ahash * 31 + self.startAlt.hashCode();
        ahash = ahash * 31 + self.balloonMass.hashCode();
        ahash = ahash * 31 + self.balloonLift.hashCode();
        
        return ahash;
    
    
    def getTypeName(self):
        return self.ballonName
    
    def getLift(self):
        return self.balloonLift
    
    def clone(self):
        #clone = deepcopy(LatexPredictor)
        #clone.balloonData = deepcopy(clone.balloonData)
#         clone = new LatexPredictor();
#         clone.balloonDrag = new Double(balloonDrag).doubleValue();
#         clone.balloonLift = new Double(balloonLift).doubleValue();
#         clone.balloonMass = new Double(balloonMass).doubleValue();
#         clone.balloonName = new String(balloonName);
#         clone.burstRad = new Double(burstRad).doubleValue();
#         clone.groundLevel = new Double(groundLevel).doubleValue();
#         clone.isAscending = new Boolean(isAscending).booleanValue();
#         clone.parachuteArea = new Double(parachuteArea).doubleValue();
#         clone.parachuteDrag = new Double(parachuteDrag).doubleValue();
#         clone.payloadMass = new Double(payloadMass).doubleValue();
#         clone.startAlt = new Double(startAlt).doubleValue();
#         clone.startLat = new Double(startLat).doubleValue();
#         clone.startLon = new Double(startLon).doubleValue();
#         clone.self.startTime = new Long(self.startTime).longValue();

        return
    

        
        
        
    
    
    def setStartTime(self, time):
        self.self.startTime = time