from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_community_posts, name='community'),
    path('post/', views.add_post, name='add_post'),
]