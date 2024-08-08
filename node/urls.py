from django.urls import path
from .views import ConnectNodeView, HelloProtocolAPI, Peers
from rest_framework import routers

urlpatterns = [
    path("", ConnectNodeView, name="ConnectNode"),
    path("hello", HelloProtocolAPI.as_view(), name="HelloProtocolAPI"),
    path("peers",Peers, name="Peers")
]

