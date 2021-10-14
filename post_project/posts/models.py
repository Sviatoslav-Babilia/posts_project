from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class User(AbstractUser):
    following = models.ManyToManyField('self', related_name='followers', blank=True, symmetrical=False)
    
    def __str__(self):
        return str(self.get_full_name()) 


class Post(models.Model):
    author = ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.title)




