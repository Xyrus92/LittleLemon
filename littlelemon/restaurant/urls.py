from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.sayHello, name='sayHello'),
    path('', views.index, name='index'),
]