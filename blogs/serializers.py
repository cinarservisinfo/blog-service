from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class BlogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Blog
        fields = ('id', 'user', 'caption', 'description','image','slug', 'content', 'created', 'updated', 'is_active')
        read_only_fields = ('created', 'updated', 'slug')
