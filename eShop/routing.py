from django.conf.urls import url
from eShop.chat import eShopConsumer

websocket_urlpatterns = [
    # url(r'^ws/play/$', eShopConsumer.as_asgi()),
    url(r'^ws/eshop/chat/(?P<room_code>\w+)/$', eShopConsumer.as_asgi()),
]