from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def food(request):
    return render(request, 'html/food.html')

def burgers(request):
    return render(request, 'html/burgers.html')