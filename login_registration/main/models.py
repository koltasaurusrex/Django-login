from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    username = models.CharField(max_length=(255))
    email = models.CharField(max_length=(255))
    password1 = models.CharField(max_length=(255))
    password2 = models.CharField(max_length=(255))
