from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
class NodeTypesChoice(models.TextChoices):
    MASTER = "master"
    LOCAL = "local"
    SELF = "self"
    REMOTE = "remote"
# Create your models here.
class Node(models.Model):
    ip = models.GenericIPAddressField()
    port = models.IntegerField(default = 8000)
    node_type = models.CharField(choices=NodeTypesChoice, max_length=10, default = "remote")
    trust = models.BooleanField(default=False)
    version = models.IntegerField(default = 0)
    last_online = models.DateTimeField(default=None, null=True)
