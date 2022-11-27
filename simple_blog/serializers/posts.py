from django.db.models import fields
from pkg_resources import require
from rest_framework import serializers
from simple_blog.models import Post
from simple_blog.serializers.hashtags import HashTagSerializer
from .user import UserSerializer


class CreatePostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'hashtags')

    def create(self, validated_data):
        hashtags = validated_data.pop('hashtags', None)
        user = self.context.get('user', None)
        post: Post = Post.objects.create(user=user, **validated_data)
        if hashtags is not None and len(hashtags) > 0:
            for hashtag in hashtags:
                post.hashtags.add(hashtag)
        return post


class RetrievePostSerializer (serializers.ModelSerializer):
    user = UserSerializer()
    hashtags = HashTagSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content',
                  'created_at', 'updated_at', 'hashtags')

    def update(self, instance: Post, validated_data):
        hashtags = validated_data.pop('hashtags', None)
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.hashtags.clear()
        if hashtags is not None and len(hashtags) > 0:
            for hashtag in hashtags:
                instance.hashtags.add(hashtag)
        instance.save()
        return instance
