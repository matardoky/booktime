from django.urls import path
from . import consumers
from channels.auth import AuthMiddlewareStack
from booktime.auth import TokenGetAuthMiddlewareStack


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
    path(
        "mobile-api/my-orders/<int:order_id>/tracker/",
        TokenGetAuthMiddlewareStack(
            consumers.OrderTrackerConsumer.as_asgi()
        )
    ),
]
