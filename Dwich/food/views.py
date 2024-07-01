from .models import Burger, Dwich, Salade, Dessert, Frite
from django.shortcuts import render

# Create your views here.


def food(request):
    return render(request, './food/templates/food.html')

def burgers(request):
    request.session.set_expiry(0)
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers}
    return render(request, './food/templates/burgers.html', ctx)

def dwichs(request):
    request.session.set_expiry(0)
    dwichs = Dwich.objects.all()
    ctx = {'dwichs': dwichs}
    return render(request, './food/templates/dwichs.html', ctx)

def salades(request):
    request.session.set_expiry(0)
    salades = Salade.objects.all()
    ctx = {'salades': salades}
    return render(request, './food/templates/salades.html', ctx)

def desserts(request):
    request.session.set_expiry(0)
    desserts = Dessert.objects.all()
    ctx = {'desserts': desserts}
    return render(request, './food/templates/desserts.html', ctx)

def frites(request):
    request.session.set_expiry(0)
    frites = Frite.objects.all()
    ctx = {'frites': frites}
    return render(request, './food/templates/frites.html', ctx)
