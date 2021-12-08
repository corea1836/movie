from django.core import paginator
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers, status
from movies.models import Movie
from accounts.models import User
from .models import Review, Comment
from .serializers import CommentSerializer, ReviewSerializer, CreateReviewSerializer

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def review_list_create(request):
    if request.method == 'GET':
      reviews = Review.objects.all()
      serializer = ReviewSerializer(reviews, many=True)
      return Response(serializer.data)
  
    elif request.method == 'POST':
      review = request.data
      movie = get_object_or_404(Movie, pk = review['movie']['id'])
      user = get_object_or_404(User, username = review['user']['username'])
      if user or movie:
        review['user'] = user
        review['movie'] = movie
        
        serializer = CreateReviewSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
          serializer.save(movie = movie, user = user)
          return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def review_paganter(request):
  reviews = Review.objects.all().order_by("-id")
  paginator = Paginator(reviews, 10)
  pagenum = request.GET["page"]
  page_obj = paginator.get_page(pagenum)
  serializer = ReviewSerializer(page_obj, many=True)
  res={
    'page': len(reviews),
    'data': serializer.data
  }
  return Response(res)

@api_view(['GET', 'DELETE', 'PUT'])

def review_detail_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
      serializer = ReviewSerializer(review) 
      return Response(serializer.data)

    elif request.method == 'PUT':
      serializer = ReviewSerializer(review, data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
      review.delete() 
      data = {
        'delete': f'데이터 {review_pk}번이 삭제되었습니다.'
      }
      return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comment_create(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  serializer = CommentSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save(review=review)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def comment_detail_delete(request, comment_pk):
  comment = get_object_or_404(Comment, pk = comment_pk)
  if request.method == 'GET':
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

  elif request.method == 'DELETE':
    comment.delete()
    data = {
      'delete': f'{comment_pk}가 삭제되었습니다.'
      }
    return Response(data=data, status=status.HTTP_204_NO_CONTENT)