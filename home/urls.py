from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), # route url that will render index.html from views.py
]
