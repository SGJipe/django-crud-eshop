from django.urls import path
from eShop.chat import eShopConsumer

websocket_urlpatterns = [
    path('ws/eshop/chat/', eShopConsumer.as_asgi()),
    # url(r'^ws/eshop/chat/(?P<room_code>\w+)/$', eShopConsumer.as_asgi()),
]