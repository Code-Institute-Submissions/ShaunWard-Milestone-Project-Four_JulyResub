from django.urls import path
from . import views

urlpatterns = [
    path('commuity/', views.all_community_posts, name='all_community_posts'),
]