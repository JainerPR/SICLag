from django.urls import re_path
from . import consumers  # Asegúrate que este archivo existe

websocket_urlpatterns = [
    re_path(r"ws/test/$", consumers.TestConsumer.as_asgi()),
]
