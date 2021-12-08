from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Review(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='reviews')
  title = models.CharField(max_length=100)
  content = models.TextField()
  rank = models.FloatField(default = 5)


class Comment(models.Model):
  review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
  user_name = models.CharField(max_length=50)
  content = models.TextField()
  