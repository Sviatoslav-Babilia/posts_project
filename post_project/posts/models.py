from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Followers(models.Model):
    author = models.OneToOneField(User, on_delete=CASCADE)
    followers = models.ManyToManyField(User, related_name="followers")


