from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('list/', list, name='list'),
    path('koreanfood/', korean, name='koreanfood'),
    path('japanesefood/', japanese, name='japanesefood'),
    path('yangsigfood/', yangsig, name='yangsigfood'),
    path('fastfood/', fastfood, name='fastfood'),
    path('asianfood/', asian, name='asianfood'),
    path('chinesefood/', chinese, name='chinesefood'),
]
