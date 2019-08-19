import requests
import time
import json

Lat = 42.0308
Lon = -93.6319
altitude = 300 # meters
postURL = "http://127.0.0.1:8000/REST/V1/flight_location"
flightID = "41ec0c23-e5dc-4be4-b67b-df9a49bf31d8"
scriptID = "c4414887-f22a-4ef9-9a3b-949497166b93"
if(True):
    r = requests.post('http://127.0.0.1:8000/REST/V1/new_flight')
    json_data = json.loads(r.text)
    flightID = json_data["flightID"]
    scriptID = json_data["scriptID"]
print(flightID)
print(scriptID)
while(False):
    time.sleep(1)
    params = {'scriptID': scriptID, 'flightID': flightID, 'time': int(time.time()), 'lat': Lat, 'lon': Lon, 'alt':altitude}
    r = requests.post(url = postURL, data = params, timeout=5)
    print(r.text)
    Lat = Lat + .001
    Lon = Lon + .001
    altitude = altitude + 20