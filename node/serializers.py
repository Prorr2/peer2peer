from rest_framework import serializers
from .models import Node

class HelloSerializer(serializers.Serializer):
    status = serializers.CharField()
    protocol = serializers.CharField()
    version = serializers.IntegerField()

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = "__all__"
    def create(self, validated_data):
        if Node.objects.filter(ip = validated_data.get("ip"), port = validated_data.get("port")).exists():
            return None
        return super().create(validated_data) 