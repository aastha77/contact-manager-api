import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ContactConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("contacts", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("contacts", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Handle incoming WebSocket messages

    async def contact_update(self, event):
        await self.send(text_data=json.dumps(event["content"]))
