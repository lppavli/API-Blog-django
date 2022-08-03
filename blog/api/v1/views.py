from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.db.models import Count
from rest_framework import permissions
from django.contrib.postgres import aggregates
from blog.api.v1.permissions import IsAuthorOrReadOnly
from blog.api.v1.serializers import UserSerializer, PostSerializer, FollowSerializer
from blog.models import Post, Follow


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = User.objects.all().annotate(cnt=Count('posts')).order_by('-cnt')
    serializer_class = UserSerializer
    # ordering_fields = ('posts',)


class FollowViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer