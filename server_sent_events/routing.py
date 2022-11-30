from django.urls import re_path, path

from server_sent_events.consumers import SimpleServerSentEventsConsumer

sse_urlpatterns = [
    path('sse/data',
        SimpleServerSentEventsConsumer.as_asgi()),
]
