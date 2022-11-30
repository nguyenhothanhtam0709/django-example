from rest_framework import serializers

class WebsocketPostAPISerializer(serializers.Serializer):
    channel_name = serializers.CharField(required=True)
    type = serializers.CharField(required=True)
    message = serializers.CharField(required=True)
    username = serializers.CharField(required=True)