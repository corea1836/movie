from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Movie, Genres
from reviews.models import Review

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields =("id", "genre_name")

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', "overview", "rank", "poster_url", "release_date", "genre", 'reviews')