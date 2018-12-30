'''
Created on Jan 21, 2017

@author: translated DGXU
'''
from atmosphere import RUCGFS, GSDParser

class AtmosphereFactory(object):
    @staticmethod
    def GetGFSProfile(self, lat, lon, time):
        src = RUCGFS()
        parser = GSDParser()
        return parser.parseAtmosphere(src.getAtmosphere(time, lat, lon))