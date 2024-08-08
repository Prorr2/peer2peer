from typing import Any
from django.core.management.base import BaseCommand, CommandParser
class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        pass
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        pass