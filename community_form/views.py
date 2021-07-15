from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class CommunityView(ListView):
    model = Post
    template_name = 'community_form.html'
    ordering = ['-date_of_post']


class PostDetail(DetailView):
    model = Post
    template_name = 'community_post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class EditPostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['content']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('community_form')
