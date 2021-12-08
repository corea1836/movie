from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genres
# Create your models here.

class User(AbstractUser):
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    nickname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genres)
