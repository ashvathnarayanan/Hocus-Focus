import asyncio
from app.models import *
from app import prototype
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

def save_question(event):
    try:
        total=len(list(Question.objects.filter(course=event["name"])))+1
    except:
        total=1
    question=Question(course=event["name"],number=total)
    question.content,options,question.answer=prototype.speech_to_question(event["lang"])
    question.save()
    return (question,options)

class StudentConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("DistracNot", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("DistracNot", self.channel_name)

    async def send_options(self, event):
        while True:
            try:
                trigger=Trigger.objects.get(name=event["name"])
                qn,options=save_question(event)
                await self.send_json({"type":"start","qno":qn.number,"options":options,"qn":qn.content})
                await asyncio.sleep(10)
            except:
                await self.send_json({"type":"stop"})
                break
