from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views.posts import PostsView, PostView
from .views.hashtags import HashTagsView, HashTagView
from .views.auth import RegistrationView, LoginView, LogoutView, ChangePasswordView
from .views.feed import MyPostsView

urlpatterns = [
    # auth
    path('auth/register', RegistrationView.as_view(), name='register'),
    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/logout', LogoutView.as_view(), name='logout'),
    path('auth/change-password', ChangePasswordView.as_view(),
         name='change_password'),
    path('auth/token-refresh',
         jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify-token',
         jwt_views.TokenVerifyView.as_view(), name='verify_token'),

    # hash-tag
    path('hashtags', HashTagsView.as_view()),
    path('hashtags/<int:id>', HashTagView.as_view()),

    # posts
    path('posts/<int:id>', PostView.as_view()),
    path('posts', PostsView.as_view()),

    # Feed
    path('feed/my-posts', MyPostsView.as_view()),
]
