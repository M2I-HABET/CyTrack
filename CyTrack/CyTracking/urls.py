from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'<str:uuid>', views.flight),
    url(r'^$', views.maps)
    
]