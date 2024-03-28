from django.urls import path
from . import views


app_name ='munu'

urlpatterns = [
    path('', views.menus, name='menu'),
]