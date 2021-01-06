from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler

from django.urls import re_path
import main.routing
 

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            main.routing.websocket_urlpatterns
        )
    ),
    'http': URLRouter(
        main.routing.http_urlpatterns + [re_path(r"", AsgiHandler)]
    ),
})