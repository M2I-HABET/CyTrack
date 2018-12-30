'''
Created on Jan 21, 2017

@author: adapted by DGXU
'''
from atmosphere.AtmosphereProfile import AtmosphereProfile
import calendar
import datetime
import traceback
debug=False

# A class to parse NOAA GSD formatted soundings.
class GSDParser:
    
    # Parse the given file and return a profile.
    # @param isHistorical put true
    def parseAtmosphere(self, file, isHistorical):
        line = ""
        conversion = 0.514444444
        hour, day, year = 0, 0, 0
        month = ""
        lat, lon = 0.0, 0.0
        profile = AtmosphereProfile(0,0)
        try:
            if debug: print(file)
            if debug: print("That is the file name")
            #with open(file, 'r') as opened:
            opened=open(file,'r')

            line = opened.readline()
            running=True
            while (line != "" and line.strip()!="" ):

                if "lapse in appropriation" in line:
                    raise Exception("USA got no money")
                if debug: print(line)
                if line == "":
                    break
                str = line.split()
                s = iter(str)
                try:
                    token = next(s)
                except:
                    break
                type = 0
                try:
                    type=int(token)
                except ValueError:
                    one, two = 0, 0

                    try:
                        if debug: print("trying2")
                        one = int(next(s))
                        two = int(next(s))
                        hour = int(one)
                        day = int(two)
                        month = int(next(s))
                        year = int(next(s))
                        
                    except:
                        line = opened.readline()
                        continue
                    
                    if debug: print('hour:'+str(hour))
                    try:
                        cal = datetime.datetime(year, month, day, hour, 0, 0, None, 0)
                        if debug: print(cal)
                        profile.startTime = int(calendar.timegm(cal.utctimetuple())) 
                           
                    except:
                        line = opened.readline()
                        if debug: print("didnt like datetime")
                        continue
                
                if debug: print(type)
                if type == 1:
                    if debug: print("in1")
                    try:
                        next(s)
                        next(s)
                        lat = float(next(s))
                        lon = float(next(s))
                    except:
                        break
                        
                    profile.lat = lat
                    profile.lon = lon
                    #break
        
                elif type == 3:
                    if debug: print("in3")
                    next(s)
                    next(s)
                    unit = next(s)
                    if unit == 'kt':
                        conversion = 0.514444444
                    elif unit == 'm/s':
                        conversion = 1.0
                    else:
                        if debug: print("Unsupported wind speed unit!")
                        break
                    #break
                    
                elif type == 9 or type==4:
                    if debug: print("in9")
                    try:
                        p = int(next(s))
                        h = int(next(s))
                        t = int(next(s))
                        dp = int(next(s))
                        dira = int(next(s))
                        spd = int(next(s))
                        
                        if debug: print(spd)
                            
                        if p == 99999 or h == 99999 or t == 99999 or dp == 99999 or dir == 99999 or spd == 99999:
                            break
                        if isHistorical:
                            profile.addData(h/3.28084, p*100 , t , dp , dira, spd * conversion)
                        else:
                            
                            profile.addData(h, p * 10.0, t / 10.0, dp / 10.0, dira, spd * conversion)
                            
                    except:
                        if isHistorical:
                            if debug: print("There is a formating problem with your Winds Aloft")
                        break
                    #break
                #else:
                    #break	
                line = opened.readline()
        except:
            traceback.print_exc()
            return "invalid"
        if debug: print('DONE')
        return profile
    
    #created for legacy support
    def parseAtmosphereHistorical(self, file):
        return self.parseAtmosphere(file, True)
        
