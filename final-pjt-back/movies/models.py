from django.db import models
from reviews.models import Review
# Create your models here.
class Genres(models.Model):
    genre_name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    poster_url = models.CharField(max_length=100)
    rank = models.FloatField()
    release_date = models.DateField()
    genre = models.ManyToManyField(Genres)
    