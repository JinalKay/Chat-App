from django.urls import re_path
from .consumers import *

websocket_urlpatterns = [
    re_path(r"ws/chatroom/(?P<chatroom_name>\w+)/$", ChatroomConsumer.as_asgi()),
    re_path(r"ws/online-status/$", OnlineStatusConsumer.as_asgi()),
]
