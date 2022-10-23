from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    link = request.GET.get('url')
    return render(request, 'home.html', {'link':link})


