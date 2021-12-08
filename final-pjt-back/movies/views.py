from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
from .serializers import GenreListSerializer, GenreSerializer, MovieSerializer
from .models import Movie, Genres
from urllib.request import urlopen

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def movies_list(request):
  if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])    
def get_genre(request):
  genres = Genres.objects.all()
  serializer = GenreListSerializer(genres, many=True)
  return Response(serializer.data)

# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def genre_reco(request, genre_pk):
#   if request.method == 'GET':
#     movies = Movie.objects.filter(genre_pk in genre)
#     serializer = MovieSerializer(movies, many=True)
#     print(serializer.data)
#     return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def moive_data_load(request):
  for a in range(1, 2):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key=1b7c84b9b10c39aaf162232cb487fb50&language=ko-KR&page={a}'
    jsondata = urlopen(url)
    data = json.loads(jsondata.read())
    datas = data.get("results")
    for data in datas:
      movie = Movie()
      movie.title = data.get("title")
      movie.overview = data.get("overview")
      movie.rank = data.get("vote_average")
      movie.poster_url = data.get("poster_path")
      movie.release_date = data.get("release_date")
      movie.save()
      for g in data.get("genre_ids"):
        print(g)
        print(type(g))
        movie.genre.add(Genres.objects.get(pk=g))

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def genre_data_load(request):
  url = f'https://api.themoviedb.org/3/genre/movie/list?api_key=1b7c84b9b10c39aaf162232cb487fb50&language=ko-KR/'
  jsondata = urlopen(url)
  data = json.loads(jsondata.read())
  datas = data.get("genres")
  for data in datas:
    genre = Genres()
    genre.id = data.get("id")
    genre.genre_name = data.get("name")
    genre.save()