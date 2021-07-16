from django.urls import path
from .views import (CommunityView, PostDetail,
                    AddPostView, EditPostView,
                    DeletePostView, AddCommentView,
                    EditCommentView, DeleteCommentView)

urlpatterns = [
    path('', CommunityView.as_view(), name='community_form'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('edit_post/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/add_comment/', AddCommentView.as_view(),
         name='add_comment'),
    path('post/<int:pk>/edit_comment', EditCommentView.as_view(),
         name='edit_comment'),
    path('post/<int:pk>/delete_comment/', DeleteCommentView.as_view(),
         name='delete_comment'),
]
