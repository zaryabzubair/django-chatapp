from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer

from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Connected', event)
        print("Channel Layer: ", self.channel_layer)
        print("Channel Name: ", self.channel_name)

        async_to_sync(self.channel_layer.group_add)(
            'tech',
            self.channel_name
        )

        self.send({
            "type": "websocket.accept"
        })

    def websocket_receive(self, event):
        print('Message received: ', event["text"])
        

    def websocket_disconnect(self, event):
        print('Disconnected', event)
        print("Channel Layer: ", self.channel_layer)
        print("Channel Name: ", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            'tech',
            self.channel_name
        )
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept"
        })
    
    async def websocket_receive(self, event):
        print('Message received: ', event["text"])
        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })
    
    async def websocket_disconnect(self, event):
        pass
        raise StopConsumer()