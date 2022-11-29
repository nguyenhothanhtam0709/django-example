from django.conf.urls import url

from websocket.consumers import SimpleWebsocketConsumer

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<chat_box_name>\w+)/$',
        SimpleWebsocketConsumer.as_asgi()),
]
