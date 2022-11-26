from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views.posts import PostsView,PostView

urlpatterns = [
    path('posts/<int:id>', PostView.as_view()),
    path('posts', PostsView.as_view()),
]