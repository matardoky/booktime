from django.urls import path
from . import consumers
from channels.auth import AuthMiddlewareStack


websocket_urlpatterns = [
    path(
        "ws/customer-service/<int:order_id>/",
        consumers.ChatConsumer.as_asgi()
    ),
    
]

http_urlpatterns = [
    path(
        "customer-service/notify/",
        AuthMiddlewareStack(
            consumers.ChatNotifyConsumer.as_asgi()
        )
    ),
]
