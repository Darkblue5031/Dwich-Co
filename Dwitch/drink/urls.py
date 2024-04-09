from django.urls import path
from . import views


app_name ='drink'

urlpatterns = [
    path('softs', views.soft, name='softs'),
    path('cafes', views.cafes, name='cafes'),
    path('bieres', views.bieres, name='bieres'),
    path('pressions', views.pressions, name='pressions'),
    path('', views.drink, name='drink'),
]
