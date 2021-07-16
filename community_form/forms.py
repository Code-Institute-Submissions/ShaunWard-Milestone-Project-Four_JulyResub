from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subject', 'content', 'author')

        widgets = {
            'author': forms.TextInput(attrs={'id': 'author-input',
                                             'class': 'form-control',
                                             'value': '',
                                             'type': 'hidden'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'id': 'name-input',
                                           'class': 'form-control',
                                           'value': '',
                                           'type': 'hidden'}),
        }
