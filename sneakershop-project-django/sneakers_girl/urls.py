from django import http
from django.urls import path
from . import views

app_name = 'sneakers_girl'

urlpatterns = [
    path('', views.girls, name='girls'),
    path('<int:sneaker_girl_id>/', views.details, name='details'),
]