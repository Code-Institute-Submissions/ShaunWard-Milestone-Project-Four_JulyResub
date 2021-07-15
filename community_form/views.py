from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class CommunityView(ListView):
    model = Post
    template_name = 'community_form.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'community_post_detail.html'
