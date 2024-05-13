from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer

from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Connected', event)
        print("Channel Layer: ", self.channel_layer)
        print("Channel Name: ", self.channel_name)

        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print("Group Name: ", self.group_name)


        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.send({
            "type": "websocket.accept"
        })

    def websocket_receive(self, event):
        print('Message received: ', event['text'])
        print('Type of Message Received from Client: ', type(event["type"]))
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {
                'type': 'chat.message',
                'message': event['text']
            }
        )

    def chat_message(self, event):
    
        message = event['message']
        print('Event...: ', event)
        print('Message Data: ', message)
        print('Type: ', type(message))
        self.send({
            'type': 'websocket.send',
            'text': message
        })
        

    def websocket_disconnect(self, event):
        print('Disconnected', event)
        # print("Channel Layer: ", self.channel_layer)
        # print("Channel Name: ", self.channel_name)
        # async_to_sync(self.channel_layer.group_discard)(
        #     'tech',
        #     self.channel_name
        # )
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Connected', event)
        print("Channel Layer: ", self.channel_layer)
        print("Channel Name: ", self.channel_name)

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        print('Message received: ', event['text'])
        print('Type of Message Received from Client: ', type(event["type"]))
        await self.channel_layer.group_send(
            self.group_name, {
                'type': 'chat.message',
                'message': event['text']
            }
        )

    async def chat_message(self, event):
    
        message = event['message']
        print('Event...: ', event)
        print('Message Data: ', message)
        print('Type: ', type(message))
        await self.send({
            'type': 'websocket.send',
            'text': message
        })
        

    async def websocket_disconnect(self, event):
        print('Disconnected', event)
        print("Channel Layer: ", self.channel_layer)
        print("Channel Name: ", self.channel_name)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        raise StopConsumer()