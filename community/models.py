from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200, null=True)
    date_of_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name="comments",
#                              on_delete=models.CASCADE)
#     name = models.ForeignKey(User, on_delete=models.CASCADE)
#     body = models.TextField()
#     date_of_post = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return '%s - %s' % (self.post.title, self.name)
