from rest_framework.views import APIView
from simple_blog.serializers.posts import RetrievePostSerializer
from rest_framework.response import Response
from rest_framework import status
from simple_blog.models import Post
from rest_framework.permissions import IsAuthenticated


class MyPostsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.filter(user=request.user.id)
        serializer = RetrievePostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
