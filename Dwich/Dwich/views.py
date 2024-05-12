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
from random import choice


# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'html/home.html')


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
    return render(request, 'html/signup.html', ctx)


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
    return render(request, 'html/login.html', ctx)


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
    return render(request, 'html/order.html', {'pickup_slots': pickup_slots})


def success(request, data=None):
    orderNum = request.session.get('orderNum')
    total = request.session.get('total')
    print(total)
    if orderNum == -1:
        return HttpResponse("User not authenticated or no more slots available")
    if orderNum is not None and Commande.objects.filter(numero=orderNum).exists():
        items = Item.objects.filter(commande__numero=orderNum)
        ctx = {'orderNum': orderNum, 'total': total, 'items': items}
        return render(request, 'html/success.html', ctx)
    else:
        return HttpResponse("Order not found or invalid")
