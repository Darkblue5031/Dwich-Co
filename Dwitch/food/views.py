from django.shortcuts import render
from django.http import HttpResponse
from .models import Burger, Dwitch, Salade, Dessert, Frite

# Create your views here.

def food(request):
    return render(request, 'html/food.html')

def burgers(request):
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers}
    return render(request, 'html/burgers.html', ctx)

def dwitchs(request):
    dwitchs = Dwitch.objects.all()
    ctx = {'dwitchs': dwitchs}
    return render(request, 'html/dwitchs.html', ctx)

def salades(request):
    salades = Salade.objects.all()
    ctx = {'salades': salades}
    return render(request, 'html/salades.html', ctx)

def desserts(request):
    desserts = Dessert.objects.all()
    ctx = {'desserts': desserts}
    return render(request, 'html/desserts.html', ctx)

def frites(request):
    frites = Frite.objects.all()
    ctx = {'frites': frites}
    return render(request, 'html/frites.html', ctx)