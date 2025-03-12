"""
ASGI config for evaluacionc1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluacionc1.settings')
django.setup()
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from .routingsocket import websocket_urlpatterns



django_asgi_app = get_asgi_application()

application =  ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': URLRouter(websocket_urlpatterns), #websocket url patterns vendra del archivo routingsocket.py
})
