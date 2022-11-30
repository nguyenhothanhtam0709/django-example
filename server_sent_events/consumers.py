import json
from channels.generic.http import AsyncHttpConsumer


class SimpleServerSentEventsConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        print(f'channel {self.channel_name} joined')

        await self.send_headers(headers=[
            (b"Cache-Control", b"no-cache"),
            (b"Content-Type", b"text/event-stream"),
            # (b"Transfer-Encoding", b"keep-alive"),
            (b"Connection", b"chunked"),
        ])
        await self.send_body(f"start event stream for channel: {self.channel_name}", more_body=True)

    async def chat_message(self, event):
        await self.send_headers(headers=[
            (b"Cache-Control", b"no-cache"),
            (b"Content-Type", b"text/event-stream"),
            # (b"Transfer-Encoding", b"keep-alive"),
            (b"Connection", b"chunked"),
        ])
        print(f'send to client {self.channel_name}')
        await self.send_body(json.dumps(event).encode("utf-8"), more_body=True)
        
