'''
Created on Nov 7, 2016

@author: matth
'''

import aprslib

import logging
class APRSDecoder(object):
    '''
    classdocs
    '''
    aprsString=""
    aprsLat=""
    aprsLon=""
    aprsCall=""
    aprsVoltage=""
    aprsType=""
    aprsDat=""
    
    '''
    This comment block will include two aprs 
    BRB:2016-11-05 12:26:04 UTC: W0ISU-9>APBL10,N1XK-1,WA0ROI-1,WIDE2*,qAR,KA0HJZ-1:!4201.59N/09339.20WO000/000/A=000967V2A1
    opentracker:2016-11-05 14:02:21 UTC: W0ISU-11>APOTU0,TCPIP*,qAS,W0ISU:/140219h/9?%P6w_XOBMG/A=056810 11.5V 40F HDOP01.1 SATS08 ISU HABET L-139-B
    
    
    '''
    
    
    
    def __init__(self):
        '''
        Constructor
        '''
        
        
        
    def setString(self,newString):
        self.aprsString=newString
        self.parseString()
        
    def getLat(self):
        return self.aprsLat
    
    def getKey(self,key):
        '''
        This is the catch all for special feilds
        '''
        val=self.aprsDat.get(key)
        if(val!='None'):
            return val
        return False

    def getJSON(self):
        '''
        This will be used to export it to JSON for archiving.
        TODO we need to come up with a format for the JSON output. The logging 
        in the database will not be in here. This will be put into a specific
        part of the system. Look for the data distributer for this data basing. 
        '''
        return
    
    def getParsed(self):
        return self.aprsDat
    
    def parseString(self):
        
        try:
            self.aprsDat=aprslib.parse(self.aprsString)
            
        except (aprslib.ParseError, aprslib.UnknownFormat) as exp:
            logging.error(exp)
            return False
        
        
        
        
        
        