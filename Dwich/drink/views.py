from django.shortcuts import render
from .models import Soft, Biere_bouteille, Biere_pression, Cafe


# Create your views here.


def drink(request):
    return render(request, 'html/drink.html')

def soft(request):
    softs = Soft.objects.all()
    ctx = {'softs': softs}
    return render(request, 'html/softs.html', ctx)

def bieres(request):
    bieres = Biere_bouteille.objects.all()
    ctx = {'bieres': bieres}
    return render(request, 'html/bieres.html', ctx)

def pressions(request):
    pressions = Biere_pression.objects.all()
    ctx = {'pressions': pressions}
    return render(request, 'html/pressions.html', ctx)

def cafes(request):
    cafes = Cafe.objects.all()
    ctx = {'cafes': cafes}
    return render(request, 'html/cafes.html', ctx)