from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=255)
    body = models.TextField(verbose_name="Body")
    author = models.ForeignKey(User, verbose_name="Author", related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return self.title
