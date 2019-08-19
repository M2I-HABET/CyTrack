from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^flight_location', views.AddFlightData),
    url(r'^flight_data_raw', views.AddFlightJsonData),
    path(r'flight/<str:uuid>', views.GetFlightPath),
    path(r'flight/array/<str:uuid>', views.GetFlightPathArray),
    path(r'flight/dataarray/<str:uuid>', views.GetFlightDataArray),
    
    
    path(r'flightpos/<str:uuid>', views.GetFlightPos),
    url(r'^new_flight', views.newFlight),
    url(r'^$', views.help),
    
]