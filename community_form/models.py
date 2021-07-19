from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_of_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('community_form')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments",
                             on_delete=models.CASCADE, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date_of_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def get_absolute_url(self):
        return reverse('community_form')
