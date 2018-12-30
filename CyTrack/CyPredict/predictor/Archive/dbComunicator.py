'''
Created on Mar 27, 2017

@author: DGXU
'''
from Archive import flightData
import json
# Purpose:
#    object that deals with the creation and management of 
#    the database. Also, maybe change class name...
class comunicator(object):
    '''
    classdocs
    '''
    flight_ID = ""
    data = None

    def __init__(self, flight_ID):
        '''
        Constructor
        '''
        self.flight_ID = flight_ID
        
        #if the flight ID exists it loads data from that id.
        if self._check_Id():
            curData = self.getAllData()
        else:
            curData = None
        
        self.data = flightData.flightData(flight_ID, curData)
        
        
        
    #checks if id exists in db
    def _check_Id(self):
        #TODO
        return True
        
    def getAllData(self):
        #TODO retrieves all data from DB
        return