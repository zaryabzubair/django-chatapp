from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio, json

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept"
        })

    def websocket_receive(self, event):
        print('Message received: ', event["text"])
        for i in range(10):
            self.send({
                "type": "websocket.send",
                "text": json.dumps({'count':i})
            })
            sleep(1)

    def websocket_disconnect(self, event):
        pass
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept"
        })
    
    async def websocket_receive(self, event):
        print('Message received: ', event["text"])
        for i in range(10):
            await self.send({
                "type": "websocket.send",
                "text": json.dumps({'count':i})
            })
            await asyncio.sleep(1)
    
    async def websocket_disconnect(self, event):
        pass
        raise StopConsumer()