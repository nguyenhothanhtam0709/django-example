from django.urls import re_path, path

from websocket.consumers import SimpleWebsocketConsumer

websocket_urlpatterns = [
    path('ws/chat/<chat_box_name>',
        SimpleWebsocketConsumer.as_asgi()),
]
