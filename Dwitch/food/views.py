from json import loads
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Burger, Dwitch, Salade, Dessert, Frite, Commande, Item
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import NewUserForm
from django.views.decorators.csrf import csrf_exempt
from random import choice
# Create your views here.

def randomOrderNumber(length :int)-> int :
    choices = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number0 = ''.join((choice(choices) for l in range(length)))
    return number0

def food(request):
    return render(request, 'html/food.html')

def burgers(request):
    request.session.set_expiry(0)
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers}
    return render(request, 'html/burgers.html', ctx)

def dwitchs(request):
    request.session.set_expiry(0)
    dwitchs = Dwitch.objects.all()
    ctx = {'dwitchs': dwitchs}
    return render(request, 'html/dwitchs.html', ctx)

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

@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')
        orders = loads(request.session['order'])
        request.session['total'] = request.POST.get('total')
        print(request.session['total'])
        randomNum = randomOrderNumber(6)
        while Commande.object.filter(number=randomNum).count()> 0:
            randomNum = randomOrderNumber(6)
        if request.user.is_authenticated:
            order = Commande(client=request.user, 
                             numero=randomNum, 
                             prix=float(request.session['total']), 
                             note=request.session['note'])
            order.save()
            for article in orders:
                item = Item(
                    commande = order,
                    nom = article[0],
                    prix = article[1]

                )
                item.save()
    else:
        print("Received non-AJAX request")
    return render(request, 'html/order.html')

def success(request):
    order = request.session['order']
    ctx = {'order':order}
    return render(request, 'html/success.html', ctx) 

def signup(request):
    ctx = {}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/food/burgers')
        else :
            ctx['form'] = form
    else :
        form = NewUserForm()
        ctx['form'] = form
    return render(request, 'html/signup.html', ctx)
        
def login(request):
    if request.POST:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=username, password=pwd)
        print(pwd, username)
        if user is not None:
            auth_login(request, user)
            return redirect('/food/burgers')
        else:
            messages.info(request, 'username and/or password are incorrect')
    ctx = {'active_link': 'login'}
    return render(request, 'html/login.html', ctx)

def logout(request):
    auth_logout(request)
    return redirect('/food/login')