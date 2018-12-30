'''
Created on Jan 21, 2017

@author: DGXU
'''

import calendar
import datetime
import os
import urllib.request
import shutil

debug=True

class RUCGFS:
    def getAtmosphere(self,time, lat, lon):
        #Adjust fields to match model
        startTime = (time // 10800)*10800
        print(lat)
        print(lon)
        rlat = lat
        rlon = lon

        #Get the time the model was last run
        cal = datetime.datetime.utcnow()
        modelRun = (cal.hour // 12) * 12
        cal.replace(hour=modelRun, minute=0, second=0,microsecond=0)
        modelTime = calendar.timegm(cal.utctimetuple())
        
        #how to get the path may or may not need to be changed
        #Check for local copy
        path = 'wind/'
        local  = None
        if os.path.exists(path):
            files = os.listdir(path)
            matchFiles = self._checkFiles(files, startTime, lat, lon)
            if len(matchFiles) > 0:
                local = matchFiles[-1]
        else:
            os.mkdir(path)
            
        #get a new model if needed
        old = True
        if local != None:
            name = os.path.basename(os.path.normpath(local))
            s = name.rfind('_')
            e = name.rfind('.')
            x = name.split('_')
            y = x[-1].split('.')
            old = modelTime > int(y)
            
        net = None
        if old:
            net = self._download(startTime, modelTime, rlat, rlon)
            
        if net is None:
            return local
        else:
            return net
    #NOT FINISHED	
    def _download(self, time, modelTime, lat, lon):
        
        address = 'https://rucsoundings.noaa.gov/get_soundings.cgi?data_source=GFS;airport=' + str(lat) + "," + str(lon) + ";hydrometeors=false&startSecs=" + str(time) + "&endSecs=" + str(time+1)
        if debug: print(address)
        cwd = os.getcwd()
        if debug: print(cwd)
        file=cwd+"\\wind\\gfs_" + str(int(lat*10)/10.0) + "_" + str(int(lon*10)/10.0) + "_" + str(int(time)) + "_" + str(modelTime) + ".gsd"
        if debug: print(file)
        if debug: print("")
        if debug: print("did it print")
        try:

            with urllib.request.urlopen(address) as response, open(file, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
        except:
            if debug: print("Cannot download or save gsd wind model file")
            
        return file
    
    def _checkFiles(self, files, startTime, lat, lon):
        filter = 'gfs_' + str(int(lat*10)) + '_' + str(int(lon*10)) + '_' + str(startTime) + '_'
        matchFiles = []
        for file in files:
            if file.startswith(filter):
                matchFiles.append(file)
        return matchFiles
    

    