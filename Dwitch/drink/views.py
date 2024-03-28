from django.shortcuts import render


# Create your views here.


def drink(request):
    return render(request, 'html/drink.html')

def soft(request):
    return render(request, 'html/soft.html')