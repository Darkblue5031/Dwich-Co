from django.urls import path
from . import views


app_name ='menu'

urlpatterns = [
    path('', views.menus, name='menu'),
    path('menu_test', views.BurgerMenuAutocomplete.as_view(), name='BurgerMenuAutocomplete'),
]