from django.urls import path
from . import views


app_name ='food'

urlpatterns = [
    path('burgers', views.burgers, name='burgers'),
    path('', views.food, name='food'),
]