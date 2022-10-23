import sneakers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Sneaker

def man(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'index.html', {'sneakers':sneakers})

def detail(request, sneaker_id):
    sneaker = get_object_or_404(Sneaker, pk=sneaker_id)
    return render(request, 'detail.html', {'sneaker':sneaker})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

