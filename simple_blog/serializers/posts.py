from django.db.models import fields
from rest_framework import serializers
from simple_blog.models import Post


class CreatePostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content')

        
class PostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')
