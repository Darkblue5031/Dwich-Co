from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'html/index.html')

def soft(request):
    return render(request, 'html/soft.html')