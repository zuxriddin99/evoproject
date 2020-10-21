from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Posts(models.Model):
    owner = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=200, null=True)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
