from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('list',list, name='list'),
]