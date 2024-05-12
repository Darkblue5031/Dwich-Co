from .models import Burger, Dwich, Salade, Dessert, Frite
from django.shortcuts import render

# Create your views here.


def food(request):
    return render(request, 'html/food.html')

def burgers(request):
    request.session.set_expiry(0)
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers}
    return render(request, 'html/burgers.html', ctx)

def dwichs(request):
    request.session.set_expiry(0)
    dwichs = Dwich.objects.all()
    ctx = {'dwichs': dwichs}
    return render(request, 'html/dwichs.html', ctx)

def salades(request):
    request.session.set_expiry(0)
    salades = Salade.objects.all()
    ctx = {'salades': salades}
    return render(request, 'html/salades.html', ctx)

def desserts(request):
    request.session.set_expiry(0)
    desserts = Dessert.objects.all()
    ctx = {'desserts': desserts}
    return render(request, 'html/desserts.html', ctx)

def frites(request):
    request.session.set_expiry(0)
    frites = Frite.objects.all()
    ctx = {'frites': frites}
    return render(request, 'html/frites.html', ctx)
