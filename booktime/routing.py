from channels.routing import ProtocolTypeRouter, URLRouter
import main.routing
from channels.auth import AuthMiddlewareStack
 

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            main.routing.websocket_urlpatterns
        )
    ),
})