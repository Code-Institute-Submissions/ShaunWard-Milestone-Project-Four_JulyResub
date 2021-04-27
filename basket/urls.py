from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='basket'), # route url that will render basket.html from views.py view_basket
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('remove/<item_id>/', views.remove_from_basket, name='remove_from_basket'),
]
