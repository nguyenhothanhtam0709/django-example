from rest_framework.views import APIView
from simple_blog.serializers.posts import CreatePostSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework import status
from simple_blog.models import Post


class PostsView(APIView):
    def post(self, request):
        serializer = CreatePostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostView(APIView):
    def get(self, request, id):
        try:
            post = Post.objects.get(pk=id)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except Post.DoesNotExist:
            return Response({'message': 'The post does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            post = Post.objects.get(pk=id)
            serializer = PostSerializer(post, data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except Post.DoesNotExist:
            return Response({'message': 'The post does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            post: Post = Post.objects.get(pk=id)
            post.delete()
            return Response(status=status.HTTP_200_OK) 
        except Post.DoesNotExist:
            return Response({'message': 'The post does not exist'}, status=status.HTTP_404_NOT_FOUND)