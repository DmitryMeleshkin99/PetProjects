from django import http
from django.urls import path
from . import views

app_name = 'sneakers'

urlpatterns = [
    path('man/', views.man, name='man'),
    path('', views.home, name='home'),
    path('<int:sneaker_id>/', views.detail, name='detail'),
    path('about', views.about, name='about')
]