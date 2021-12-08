from django.urls import path
from . import views


urlpatterns = [
    path('', views.movies_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('genres/', views.get_genre),
    # path('genrereco/<int:genre_pk>/', views.genre_reco),
    path('loaddata/', views.moive_data_load),
    path('loadgenre/', views.genre_data_load),
]