from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from chat import routing

application = ProtocolTypeRouter({
    "websocket": URLRouter(routing.websocket_urlpatterns),
})
