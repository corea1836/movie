from django.contrib import admin
from movies.models import Movie, Genres

admin.site.register(Movie)
admin.site.register(Genres)
