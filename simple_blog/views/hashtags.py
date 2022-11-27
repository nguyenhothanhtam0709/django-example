from rest_framework.views import APIView
from simple_blog.serializers.hashtags import CreateHashTagSerializer, ManyHashTagsWithRelationSerializer, HashTagWithRelationSerializer, HashTagSerializer
from rest_framework.response import Response
from rest_framework import status
from simple_blog.models import HashTag
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound


class HashTagsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CreateHashTagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        hashtags = HashTag.objects.all()
        serializer = ManyHashTagsWithRelationSerializer(hashtags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class HashTagView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            hashtag = HashTag.objects.get(pk=id)
            serializer = HashTagWithRelationSerializer(hashtag)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except HashTag.DoesNotExist:
            raise NotFound('Hashtag does not exist.')

    def put(self, request, id):
        try:
            hashtag: HashTag = HashTag.objects.get(pk=id)
            serializer = HashTagSerializer(hashtag, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except HashTag.DoesNotExist:
            raise NotFound('Hashtag does not exist.')
        pass

    def delete(self, request, id):
        try:
            hashtag: HashTag = HashTag.objects.get(pk=id)
            hashtag.delete()
            return Response(status=status.HTTP_200_OK)
        except HashTag.DoesNotExist:
            raise NotFound('Hashtag does not exist.')
