from rest_framework.views import APIView
from websocket.utils.channel import send_to_channel
from server_sent_events.utils.channel import send_to_channel
from rest_framework.response import Response
from rest_framework import status
from simple_blog.serializers.post_api import WebsocketPostAPISerializer, SsePostAPISerializer

"""
test websocket
"""
class WebsocketPost(APIView):
    def post(self, request):
        serializer = WebsocketPostAPISerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        channel_name = serializer.validated_data.pop('channel_name')
        type = serializer.validated_data.pop('type')
        send_to_channel(channel_name=channel_name, type=type, data=serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

"""
test server-sent events
"""
class SsePost(APIView):
    def post(self, request):
        serializer = SsePostAPISerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        channel_name = serializer.validated_data.pop('channel_name')
        type = "send_message"
        send_to_channel(channel_name=channel_name, type=type, data=serializer.validated_data)
        return Response(status=status.HTTP_200_OK)