from django.shortcuts import render


# Create your views here.

def menus(request):
    return render(request, 'html/menus.html')
