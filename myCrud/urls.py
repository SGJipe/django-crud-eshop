from unittest import result
from django.urls import path
from . import views

app_name='myCrud'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:question_id>/', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('update/<int:question_id>/', views.update, name='update'),
    path('delete/<int:question_id>/', views.delete, name='delete'),
    path('<int:question_id>/results/', views.results, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]