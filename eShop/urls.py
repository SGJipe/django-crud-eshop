from unittest import result
from django.urls import path
from . import views

app_name='myCrud'
urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),
    path('product-detail/<int:product_id>', views.product_detail, name='product_detail'),
    path('chat/', views.chat_socket, name='chat'),
    path('chat/<room_code>', views.chat_board, name='chat_board'),
    # path('product-detail/<int:product_id>', views.buy_product, name='buy_product'),
]