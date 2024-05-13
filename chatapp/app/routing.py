from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sc/<str:groupname>/', consumers.MySyncConsumer.as_asgi()),
    path('ws/as/<str:groupname>/', consumers.MyAsyncConsumer.as_asgi()),
]