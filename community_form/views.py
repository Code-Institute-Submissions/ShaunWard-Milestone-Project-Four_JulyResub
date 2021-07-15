from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


class CommunityView(ListView):
    model = Post
    template_name = 'community_form.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'community_post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
