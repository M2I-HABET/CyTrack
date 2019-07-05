import requests
import time
import json

Lat = 42.0308
Lon = -93.6319
altitude = 300 # meters
postURL = "http://127.0.0.1:8000/REST/V1/flight_location"
flightID = ""
scriptID = ""
r = requests.post('http://127.0.0.1:8000/REST/V1/new_flight')
json_data = json.loads(r.text)
flightID = json_data["flightID"]
scriptID = json_data["scriptID"]
while(True):
    time.sleep(1)
    params = {'scriptID': scriptID, 'flightID': flightID, 'time': int(time.time()), 'lat': Lat, 'lon': Lon, 'alt':altitude}
    r = requests.post(url = postURL, data = params)
    print(r.text)