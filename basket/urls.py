from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='basket'), # route url that will render basket.html from views.py view_basket
]
