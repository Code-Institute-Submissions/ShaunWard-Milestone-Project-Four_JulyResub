from django.shortcuts import render
from .models import Post


def all_community_posts(request):
    posts = Post.objects.all()
    template = 'community/community.html'

    context = {
        'posts': posts
    }
    
    return render(request, template, context)
