from rest_framework import serializers
from simple_blog.models import HashTag
from rest_framework.exceptions import NotFound


class CreateHashTagSerializer (serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = ('name', 'key', 'parent_hashtag')


class HashTagSerializer (serializers.ModelSerializer):
    '''
    serialize a hashtag
    '''
    class Meta:
        model = HashTag
        fields = '__all__'


class ManyHashTagsWithRelationSerializer (HashTagSerializer):
    '''
    serialize list of hashtags
    '''
    parent_hashtag = HashTagSerializer()


class HashTagWithRelationSerializer (HashTagSerializer):
    '''
    serialize a hashtag with relation
    '''
    children_hashtags = HashTagSerializer(many=True)
    parent_hashtag = HashTagSerializer()
