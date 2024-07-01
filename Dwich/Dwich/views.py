from json import loads
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Commande, Item, PickupSlot
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import NewUserForm
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from random import choice
from drink.models import Soft, Biere_bouteille, Biere_pression, Cafe
from food.models import Burger, Dwich, Frite, Salade, Dessert
import json


def signup(request):
    ctx = {}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            ctx['form'] = form
    else:
        form = NewUserForm()
        ctx['form'] = form
    return render(request, 'signup.html', ctx)


def login(request):
    if request.POST:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=username, password=pwd)
        print(pwd, username)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'username and/or password are incorrect')
    ctx = {'active_link': 'login'}
    return render(request, 'login.html', ctx)


def logout(request):
    auth_logout(request)
    return redirect('/login')


def randomOrderNumber(length: int) -> int:
    choices = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number0 = ''.join((choice(choices) for l in range(length)))
    return number0


@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        pickup_slot_id = request.POST.get('pickup_slot')
        pickup_slot = PickupSlot.objects.get(pk=pickup_slot_id)
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')
        orders = loads(request.session['order'])
        request.session['total'] = request.POST.get('total')
        print(request.session['total'])
        randomNum = randomOrderNumber(6)
        while Commande.objects.filter(numero=randomNum).count() > 0:
            randomNum = randomOrderNumber(6)
        print(request.user.is_authenticated, pickup_slot.remaining_capacity > 0)
        if request.user.is_authenticated and pickup_slot.remaining_capacity > 0:
            order = Commande(client=request.user,
                             numero=randomNum,
                             prix=float(request.session['total']),
                             note=request.session['note'],
                             pickup_slot=pickup_slot)
            order.save()
            pickup_slot.remaining_capacity -= 1
            pickup_slot.save()
            request.session['orderNum'] = order.numero
            print(request.session['orderNum'])
            for article in orders:
                item = Item(
                    commande=order,
                    nom=article[0],
                    prix=article[1]
                )
                item.save()
        else:
            request.session['orderNum'] = -1
    else:
        print("Received non-AJAX request")
    pickup_slots = PickupSlot.objects.all()
    return render(request, 'order.html', {'pickup_slots': pickup_slots})


def success(request, data=None):
    orderNum = request.session.get('orderNum')
    total = request.session.get('total')
    print(total)
    if orderNum == -1:
        return HttpResponse("User not authenticated or no more slots available")
    if orderNum is not None and Commande.objects.filter(numero=orderNum).exists():
        items = Item.objects.filter(commande__numero=orderNum)
        ctx = {'orderNum': orderNum, 'total': total, 'items': items}
        return render(request, 'success.html', ctx)
    else:
        return HttpResponse("Order not found or invalid")

def beer(request, beers_id: str):
    beersToFind = beers_id.split(',')
    beers = []
    for beerId in beersToFind:
        beers.append(Biere_bouteille.objects.get(pk=beerId).__dict__())
    return HttpResponse(json.dumps(beers), content_type="application/json")

def soft(request, softs_id: str):
    softsToFind = softs_id.split(',')
    print(softs_id)
    softs = []
    for softId in softsToFind:
        softs.append(Soft.objects.get(pk=softId).__dict__())
    return HttpResponse(json.dumps(softs), content_type="application/json")

def pression(request, pressions_id: str):
    pressionsToFind = pressions_id.split(',')
    pressions = []
    for pressionId in pressionsToFind:
        pressions.append(Biere_pression.objects.get(pk=pressionId).__dict__())
    return HttpResponse(json.dumps(pressions), content_type="application/json")

def coffee(request, coffees_id: str):
    coffeesToFind = coffees_id.split(',')
    coffees = []
    for coffeeId in coffeesToFind:
        coffees.append(Cafe.objects.get(pk=coffeeId).__dict__())
    return HttpResponse(json.dumps(coffees), content_type="application/json")

def burger(request, burgers_id: str):
    burgersToFind = burgers_id.split(',')
    burgers = []
    for burgerId in burgersToFind:
        burgers.append(Burger.objects.get(pk=burgerId).__dict__())
    return HttpResponse(json.dumps(burgers), content_type="application/json")

def dwitch(request, dwitchs_id: str):
    dwitchsToFind = dwitchs_id.split(',')
    dwitchs = []
    for dwitchId in dwitchsToFind:
        dwitchs.append(Dwich.objects.get(pk=dwitchId).__dict__())
    return HttpResponse(json.dumps(dwitchs), content_type="application/json")

def fries(request, fries_id: str):
    friesToFind = fries_id.split(',')
    fries = []
    for friesId in friesToFind:
        fries.append(Frite.objects.get(pk=friesId).__dict__())
    return HttpResponse(json.dumps(fries), content_type="application/json")

def salad(request, salads_id: str):
    saladsToFind = salads_id.split(',')
    salads = []
    for saladId in saladsToFind:
        salads.append(Salade.objects.get(pk=saladId).__dict__())
    return HttpResponse(json.dumps(salads), content_type="application/json")

def dessert(request, desserts_id: str):
    dessertsToFind = desserts_id.split(',')
    desserts = []
    for dessertId in dessertsToFind:
        desserts.append(Dessert.objects.get(pk=dessertId).__dict__())
    return HttpResponse(json.dumps(desserts), content_type="application/json")