from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^flight_location', views.AddFlightData),
    url(r'^new_flight', views.newFlight),
    url(r'^$', views.help),
    
]