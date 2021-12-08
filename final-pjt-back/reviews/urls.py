from django.urls import path
from . import views

urlpatterns = [
    # Review
    path('', views.review_list_create),
    path("<int:review_pk>/", views.review_detail_update_delete),
    path("page/", views.review_paganter),
    
    # Comments
    path('<int:review_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_detail_delete),
]