from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from app.consumer import StudentConsumer
from django.urls import path


application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket": URLRouter([
        path("ws/", StudentConsumer.as_asgi()),
    ])
})
