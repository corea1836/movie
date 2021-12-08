from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = get_user_model()
    fields = ('username', 'password', 'genres', 'address', 'email', 'nickname', 'phone')

class ProfileSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = User
    fields = ('username', 'address', 'email', 'nickname', 'phone', 'genres')
    read_only_fields = ('username',)

class UsernameSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = User
    fields = ('username',)
    read_only_fields = ('username',)