from django.shortcuts import render
from CyTracking.models import singleFlight
import time

# Create your views here.


def maps(request):
    return render(request, 'CyTrack/track.html')

def flight(request, uuid):
    flightID = uuid
    print(uuid)
    flight = singleFlight.objects.get(IDs = flightID)
    data = flight.flightPositionData
    data.pop(0)
    retDat = []
    print(data[0])
    timesec = int(data[0][1])
    retDat2=[]
    for dat in data:
        retDat.append(str(int(dat[1])-timesec)+","+dat[3]+','+dat[2]+","+dat[4]+",")
    print(retDat[0])
    timeDat = time.gmtime(timesec)
    year = str(timeDat.tm_year)
    month = timeValFormat(timeDat.tm_mon)
    day = timeValFormat(timeDat.tm_mday)
    hour = timeValFormat(timeDat.tm_hour)
    minute = timeValFormat(timeDat.tm_min)
    second = timeValFormat(timeDat.tm_sec)
    timeformat = year+"-"+month+"-"+day+"T"+hour+":"+minute+":"+second+"Z" #2012-08-04T10:00:00Z
    endDate = str(int(year)+1)+"-"+month+"-"+day+"T"+hour+":"+minute+":"+second+"Z"
    
    return render(request, 'CyTrack/track.html',{'path': retDat, 'date': timeformat, 'endDate':endDate, 'uuid': flightID})






#helper functions

def timeValFormat(val):
    if val<10:
        val = "0"+str(val)
    else:
        val = str(val)
    return val