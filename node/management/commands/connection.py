from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
import requests
import json
from node.serializers import HelloSerializer
from node.models import Node
from node.constants import local_networks
class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("data", nargs="+", type=str)
        parser.add_argument("--trust", type=int)
        parser.add_argument("--remove", type=int)



    def handle(self, *args: Any, **options: Any) -> str | None:
        ip = options["data"][0]
        port = options["data"][1]
        trust = options["trust"] if options["trust"] == 1 else False
        url = f"http://{ip}:{port}/hello"
        response = requests.get(url)
        jsonResponse = json.loads(response.content)
        serializer = HelloSerializer(data = jsonResponse)
        if serializer.is_valid():
             
             if not options["remove"]:
                if ip not in local_networks:
                    newNode = Node.objects.get_or_create(trust = trust, ip = ip, port = port)[0]
                else:
                    newNode = Node.objects.get_or_create(trust = trust, ip = ip, port = port, node_type = "local")[0]
                self.stdout.write(
                 self.style.WARNING("Protocolo correcto")
                )
                self.stdout.write(
                    self.style.SUCCESS("Nodo conectado")
                )
             else:
                 newNode = Node.objects.get_or_create(ip = ip, port = port)[0]
                 newNode.delete()
                 self.stdout.write(
                    self.style.SUCCESS("Nodo eliminado")
                 )
        else:
            self.stdout.write(
                 self.style.ERROR("Protocolo incorrecto")
            )
            self.stdout.write(
                 self.style.ERROR("Nodo no conectado")
            )
        