from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'), # route url that will render all_products from views.py
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]