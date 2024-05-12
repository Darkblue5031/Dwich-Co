from django.urls import path
from . import views


app_name ='food'

urlpatterns = [
    path('burgers', views.burgers, name='burgers'),
    path('', views.food, name='food'),
    path('dwichs', views.dwichs, name='dwichs'),
    path('salades', views.salades, name='salades'),
    path('desserts', views.desserts, name='desserts'),
    path('frites', views.frites, name='frites'),
]