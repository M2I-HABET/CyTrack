'''
Created on Jan 12, 2017

@author: matth
'''

class ObjectData(object):
    '''
    This will be the location of the data for an object. You will be able to on 
    the fly to add and remove sources of data i.e. from aprs.fi or from radio.
    
    '''
    flightID=''

    def __init__(self,flightid):
        '''
        Constructor
        '''
        self.flightID=flightid
        
        
    '''
    This section will be the getters and setters for the tracker. 
    '''
    def setSerialSources(self):
        return

    def getNewestAPRS(self):
        return
    
    def addNewAPRS(self):
        return
    
    
    def getNewestPos(self):
        return
    
    def addNewPos(self):
        return
    
    
    def getLatestCommand(self):
        return
    
    def addNewCommand(self,cmd):
        return 
    
    def getLatestResponse(self):
        return
    
    def addNewResponse(self,cmd,rsd):
        return 
    
    
    '''---------------------------------------------------------------------'''
    
    '''
    This will be a modifier section. In here will be the ability to change data
    sources and add new ones.
    '''
    
    def addNewSource(self):
        '''
        This will be added to make it so that you can add new sources of data
        to the system. 
        '''
        return
    
    def changeAPRS(self,index):
        return
    
    
    def changePos(self,index):
        return
    
    
    '''---------------------------------------------------------------------'''
    
    '''
    This section will be functions that are called from the getters and setters
    
    '''
    
    
    
    
    
        