from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from blog.api.v1.post_views import *

from blog.api.v1.user_views import CreateUserView, UserListView

urlpatterns = [
    path("posts/", PostListView.as_view()),
    path("posts/<int:pk>/", PostDetailView.as_view()),
    path("posts/create/", PostCreateView.as_view()),
    path("posts/new/", PostNewListView.as_view()),
    path("follows/", FollowListView.as_view()),
    path("follows/create/", FollowCreateView.as_view()),
    path("follows/<int:pk>/", FollowDestroyView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obbtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("signup/", CreateUserView.as_view()),
    path("users/", UserListView.as_view()),
]
