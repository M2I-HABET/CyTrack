'''
Created on Mar 27, 2017

@author: DGXU
'''
import json
#a data container for the different table variables
class flightData(object):
    '''
    classdocs
    '''
    flight_ID = ""
    flight_info = {} #needs to be  
    
    control_checklists = {}
    control_team_members = {}
    flight_data = {}
    given_commands = {}
    go_nogo = {}
    launch_checklists = {}
    launch_team_members = {}
    manager_checklists = {}
    manager_team_members = {}
    members = {}
    prediction_checklists = {}
    predictions = {}
    recovery_checklists = {}
    recovery_team_members = {}
    

    def __init__(self, flight_ID):
        '''
        Constructor
        '''
        self.flight_ID = flight_ID
        self.flight_info = {"id":flight_ID, "radios_in_use":None, "primary_tracking":None, 
                            "secondary_tracking":None, "comm_freq":None,"date":None, "notes":None}
        self.control_checklists = {"flight_id":flight_ID, "mission_planning":None, 
                                   "ERR":None,"LRR":None,"preflight":None,"Notes": None}
        self.control_team_members = {"flight_id":flight_ID, "member_id":None, "notes":None}
        self.flight_data= {"flight_id":flight_ID,"launch_time":None, "burst_time":None, 
                          "recovery_time":None,"packets":None, "notes":None}
        self.given_commands = {"flight_id":flight_ID, "time":None, "result":None, "notes":None}
        self.go_nogo = {"flight_id":flight_ID,"ERR_launch_decision":None,"ERR_recovery_decision":None, 
                        "ERR_manager_decision":None, "ERR_control_decision":None, "LRR_launch_decision":None,
                        "LRR_recovery_decision":None, "LRR_manager_decision":None, "LRR_control_decision":None,
                        "preflight_launch_decision":None,"preflight_recovery_decision":None, 
                        "preflight_manager_decision":None, "preflight_control_decision":None, "notes":None}
        self.launch_checklists = {"flight_id":flight_ID, "mission_planning":None, "ERR":None, "LRR":None, "preflight":None,
                                   "ERR_inventory":None, "LRR_inventory":None, "preflight_inventory":None, "notes":None}
        self.launch_team_members = {"flight_id":flight_ID, "member_id": None, "notes":None}
        self.manager_checklists = {"flight_id":flight_ID, "mission_planning":None, "ERR":None, "LRR":None, "preflight":None, "notes":None}
        self.manager_team_members = {"flight_id":flight_ID, "member_id":None, "notes":None}
        self.members = {"member_id":None, "name":None, "callsign":None, "email":None, "number":None}
        self.prediction_checklists = {"flight_id":flight_ID, "check_id":None, "meeting_date":None, "payload_mass":None, "ballon_mass":None,
                                      "launch_time":None, "burst_altitude":None, "neck_lift":None, "ascent_rate":None, "overfill_underfill":None,
                                      "burst_lat":None, "burst_lon":None, "burst_time":None, "landing_lat":None, "landing_lon":None, "landing_time":None,
                                      "total_flight_time":None, "driving_time":None, "distance":None}
        self.predictions = {"flight_id":flight_ID, "ERR_prediction":None, "LRR_prediction":None, "preflight_prediction":None, "notes":None}
        self.recovery_checklists = {"flight_id":flight_ID, "mission_planning":None, "ERR":None, "LRR":None, "preflight":None, "ERR_inventory":None, 
                                    "LRR_inventory":None, "preflight_inventory":None, "notes":None}
        self.recovery_team_members = {"flight_id":flight_ID, "member_id":None, "notes":None}
        
        
    #loads all the known data
    def loadData(self, data):
        if data is None:
            self.createNewData()
            return
        
        #TODO 
        return
    
    def createNewData(self):
        #TODO fills variables with default values
        
        return