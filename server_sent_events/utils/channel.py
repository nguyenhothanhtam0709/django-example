from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

"""
channel_name: name of received channel
type: event type (or event name)
data: event data
"""
def send_to_sse_channel(channel_name: str, type: str, data):
    channel_layer = get_channel_layer()
    data['type'] = type
    async_to_sync(channel_layer.send)(channel_name, data)