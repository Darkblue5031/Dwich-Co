from django.urls import path
from . import views

app_name ='drink'

urlpatterns = [
    path('soft', views.soft, name='soft'),
]