from django.db.models import fields
from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie
from accounts.serializers import UsernameSerializer
from django.contrib.auth import get_user_model

class ReviewListSerializer(serializers.ModelSerializer):
  user = UsernameSerializer(read_only=True)
  class Meta:
    model = Review
    fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('id', 'content', 'user_name', 'review',)
    read_only_fields = ('review',)

class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('id', 'title', 'poster_url',)


class ReviewSerializer(serializers.ModelSerializer):
  user = UsernameSerializer(read_only=True)
  comments = CommentSerializer(many=True, read_only=True)
  movie = MovieSerializer(read_only=True)

  class Meta:
    model = Review
    fields = ('id', 'title', 'content', 'rank', 'comments', 'movie', 'user')


class UserIdSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ('username',)
  
class MovieIDSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('id',)

class CreateReviewSerializer(serializers.ModelSerializer):
  user = UserIdSerializer(read_only=True)
  movie = MovieIDSerializer(read_only=True)

  class Meta:
    model = Review
    fields = ('title', 'content', 'rank', 'user', 'movie')