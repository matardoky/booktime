from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from django.urls import re_path, path
import main.routing
from .auth import TokenGetAuthMiddlewareStack
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booktime.settings")

application = ProtocolTypeRouter({
    "http": URLRouter(
        main.routing.http_urlpatterns + [re_path("", get_asgi_application())]
    ),
    "websocket": TokenGetAuthMiddlewareStack(
        URLRouter(
            main.routing.websocket_urlpatterns
        )
    ),
    
})