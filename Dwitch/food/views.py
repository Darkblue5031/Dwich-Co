from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'html/index.html')

def burgers(request):
    return render(request, 'html/burgers.html')