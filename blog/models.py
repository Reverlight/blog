from django.db import models
from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    theme = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, null=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    comments = models.ManyToManyField('Comment', blank=True, null=True)

    def __str__(self):
        return self.theme


class Comment(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()


class User(AbstractUser):
    pass
