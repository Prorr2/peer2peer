from django.shortcuts import render, HttpResponse
from .forms import NodeForm, HelloProtocolForm
from .models import Node
import requests
import json
from .serializers import NodeSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
# Create your views here.
def connectNode(ip, port, Node : Node):
    data = {"validator" : Node.uuid}
    requests.post(f"ip:port/hello", data)

def ConnectNodeView(request):
    form = NodeForm()
    if request.POST:
        form = NodeForm(request.POST)
        if form.is_valid():
            ip = form.cleaned_data.get("ip")
            port = form.cleaned_data.get("port")

            print(ip, port)
    return render(request, "connectNode.html", {"form" : form})

class HelloProtocolAPI(APIView):
    def get(self, request):
        return Response({"status" : "ok", "protocol" : "bigastrou", "version" : 0}) 

@api_view(['GET'])
def Peers(request):
    nodes = Node.objects.exclude(trust = False).filter(node_type = "remote")
    serializer = NodeSerializer(nodes, many=True)
    return Response({"peers" : serializer.data})
