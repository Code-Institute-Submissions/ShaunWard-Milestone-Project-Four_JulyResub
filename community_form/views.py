from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from .models import Post, Comment
from .forms import PostForm, CommentForm
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


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})


class EditCommentView(UpdateView):
    model = Comment
    template_name = 'edit_comment.html'
    fields = ['body']


class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('community_form')
