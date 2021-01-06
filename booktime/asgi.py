from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

from django.urls import re_path, path
import main.routing
 
application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            main.routing.websocket_urlpatterns
        )
    ),
    "http": URLRouter(
        main.routing.http_urlpatterns + [re_path("", get_asgi_application())]
    )
    
})