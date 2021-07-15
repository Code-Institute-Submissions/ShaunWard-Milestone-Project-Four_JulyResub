from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subject', 'content', 'author')

        widgets = {
            'author': forms.TextInput(attrs={'id': 'author-input',
                                        'class': 'form-control', 'value': '',
                                        'type': 'hidden'}),
        }
