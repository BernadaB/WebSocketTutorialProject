import os

from channels.auth import AuthMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from websocket_tutorial.chat import routings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_tutorial.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddleware(
        URLRouter(
            routings.websocket_urlpatterns
        )
    )
})
