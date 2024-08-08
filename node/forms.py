from django import forms 
from .models import Node
from django.utils.translation import gettext_lazy as _
class NodeForm(forms.Form):
    ip = forms.CharField(label="IP")
    port = forms.IntegerField(label=_("Puerto"))
    class Meta:
        model = Node
        fields = ["ip", "port"]

class HelloProtocolForm(forms.Form):
    validator = forms.UUIDField()
    class Meta:
        fields =  ["validator"]