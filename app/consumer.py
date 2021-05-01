import asyncio
from app import prototype
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class StudentConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("DistracNot", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("DistracNot", self.channel_name)

    async def send_options(self, event):
        # options=prototype.main()
        await self.send_json({"options":["ash","vath",'naray','anan']})

    async def stop_options(self, event):
        await self.send_json({"options":"opop"})
