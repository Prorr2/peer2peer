from django.urls import path
from .views import Running, HelloProtocolAPI, Peers
from rest_framework import routers

urlpatterns = [
    path("", Running, name="Running"),
    path("hello", HelloProtocolAPI.as_view(), name="HelloProtocolAPI"),
    path("peers",Peers, name="Peers")
]

