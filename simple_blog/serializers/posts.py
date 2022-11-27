from django.db.models import fields
from rest_framework import serializers
from simple_blog.models import Post
from .user import UserSerializer


class CreatePostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content')

    def create(self, validated_data):
        user = self.context.get('user', None)
        return Post.objects.create(user=user, **validated_data)


class RetrievePostSerializer (serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')
