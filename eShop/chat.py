import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class eShopConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']
        self.room_group_name = "django-chat"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        print("Disconnected")
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        response = json.loads(text_data)
        message = response.get("message", None)

        # Send message to room group
        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'send_message',
            'message': message,
        })

    async def send_message(self, res):
        """ Receive message from room group """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "payload": res,
        }))