from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/page/tools/<str:room_name>/', consumers.ChatConsumer),
]