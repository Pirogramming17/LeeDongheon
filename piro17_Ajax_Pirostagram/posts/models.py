from statistics import mode
from django.db import models

class Post(models.Model):
    content = models.CharField(max_length=200)
    like = models.TextField(default= '<i class="fa-solid fa-heart"></i>')
    liked = models.BooleanField(default=False)
