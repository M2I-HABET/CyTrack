from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^flight_location', views.AddFlightData),
    path(r'flight/<str:uuid>', views.GetFlightPath),
    url(r'^new_flight', views.newFlight),
    url(r'^$', views.help),
    
]