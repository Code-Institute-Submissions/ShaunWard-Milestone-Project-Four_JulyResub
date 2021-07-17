from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_community_posts, name='community'),
    path('post/', views.add_post, name='add_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('<int:post_id>/', views.comments_section, name='comments_section'),
    path('comment/', views.add_comment, name='add_comment'),
    path('edit/<int:post_id>/', views.edit_comment, name='edit_comment'),
    path('delete/<int:post_id>/', views.delete_comment, name='delete_comment'),
]