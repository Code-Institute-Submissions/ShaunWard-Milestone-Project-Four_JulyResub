from django.urls import path
from .views import CommunityView, PostDetail

urlpatterns = [
    path('', CommunityView.as_view(), name='community_form'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
]