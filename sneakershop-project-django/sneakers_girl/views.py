import sneakers_girl
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Sneaker_girl

def girls(request):
    sneakers = Sneaker_girl.objects.all()
    return render(request, 'girl.html', {'sneakers':sneakers})

def details(request, sneaker_girl_id):
    sneaker_girl = get_object_or_404(Sneaker_girl, pk=sneaker_girl_id)
    return render(request, 'details.html', {'sneaker_girl':sneaker_girl})
# Create your views here.
