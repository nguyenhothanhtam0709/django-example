from rest_framework.views import APIView
from simple_blog.serializers.posts import CreatePostSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework import status
from simple_blog.models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound


class PostsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, id):
        try:
            post = Post.objects.get(pk=id)
            serializer = self.serializer_class(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            raise NotFound('Post does not exist.')

    def put(self, request, id):
        try:
            post = Post.objects.get(pk=id)
            serializer = self.serializer_class(post, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            raise NotFound('Post does not exist.')

    def delete(self, request, id):
        try:
            post: Post = Post.objects.get(pk=id)
            post.delete()
            return Response(status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            raise NotFound('Post does not exist.')
