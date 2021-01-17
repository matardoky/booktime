import os
from django.urls import re_path, path
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booktime.settings")
django_asgi_app = get_asgi_application()

from .auth import TokenGetAuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import main.routing


application = ProtocolTypeRouter({
    "http": URLRouter(
        main.routing.http_urlpatterns + [re_path("", django_asgi_app)]
    ),
    "websocket": TokenGetAuthMiddlewareStack(
        URLRouter(
            main.routing.websocket_urlpatterns
        )
    ),
    
})





# import django
# from channels.routing import get_default_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booktime.settings")
# django.setup()

# application = get_default_application()

