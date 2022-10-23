from django.urls import path
from pitanie import views

app_name = 'pitanie'
urlpatterns = [
    path('', views.home, name='home'),
    path('breakfast/', views.breakfast, name='breakfast'),
    path('dinner/', views.dinner, name='dinner'),
    path('lunch/', views.lunch, name='lunch'),
]