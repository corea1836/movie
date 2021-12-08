from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import User
from server import settings
#from core.utils import login_decorator

from .serializers import ProfileSerializer, UserSerializer

import json
import base64

from django.http import JsonResponse


from server.settings import SECRET_KEY
from accounts.models import User
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
  password = request.data.get('password')
  password_confirmation = request.data.get('passwordConfirmation')
  print(request.data)
  if password != password_confirmation:
    return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

  serializer = UserSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    user = serializer.save()
    user.set_password(request.data.get('password'))
    user.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def profile_detail(request):
  access_token = request.headers.get('Authorization', None)   

  a = access_token.split('.')
  a0 = a[1]
  a0 = a0 + "=" * (4 - len(a0) % 4)
  a1 = a0.encode("UTF-8")
  
  a2 = base64.b64decode(a1)
  a2 = a2.decode("UTF-8")
  a2 = json.loads(a2)
  profile = get_object_or_404(User, pk=a2['user_id'])
  if request.method =="GET":
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

  elif request.method =="PUT":
    serializer = ProfileSerializer(profile, data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def chkID(request):
  username = request.data.get("username")
  print(User.objects.filter(username=username).exists())
  if User.objects.filter(username=username).exists():
    return Response({'error': '이미 존재하는 아이디입니다.'}, status=status.HTTP_400_BAD_REQUEST)
  return Response({'results': '사용가능합니다.'})

  

 