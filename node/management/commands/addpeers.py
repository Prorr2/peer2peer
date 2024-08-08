from typing import Any
from django.core.management.base import BaseCommand, CommandParser
import requests
from node.serializers import NodeSerializer
import json
class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("data", nargs="+", type=str)
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        ip = options["data"][0]
        port = options["data"][1]
        jsonPeers = json.loads(requests.get(f"http://{ip}:{port}/peers").content)["peers"]
        serializer = NodeSerializer(data = jsonPeers, many = True)
        if serializer.is_valid():
            for peer in jsonPeers:
                ip = peer["ip"]
                port = peer["port"]
                self.stdout.write(
                    self.style.SUCCESS(f"Nodo {ip}:{port} añadido")
                )
            data = serializer.save()
            print(data)
