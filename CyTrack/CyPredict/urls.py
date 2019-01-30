from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'Prediction', views.predictionOutPut),
    url(r'^$', views.getParams)
]
