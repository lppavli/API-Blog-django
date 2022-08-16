from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from django.db.models import Q
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from config import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

from blog.api.v1.permissions import IsAuthorOrReadOnly
from blog.api.v1.post_serializers import (
    FollowSerializer,
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer, FollowCreateSerializer,
)
from blog.models import Post, Follow


class PostListView(generics.ListAPIView):
    """Вывод всех постов"""

    serializer_class = PostListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["author__username"]

    def get_queryset(self):
        posts = cache.get('posts')
        if not posts:
            posts = Post.objects.all().order_by("-created_at")
            cache.set('posts', posts)
        return posts


class PostNewListView(generics.ListAPIView):
    """Вывод непрочитанных постов"""

    serializer_class = PostListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["author__username"]

    def get_queryset(self):
        posts = cache.get('posts_new')
        if not posts:
            posts = Post.objects.filter(~Q(read_users=self.request.user))
            cache.set('posts_new', posts)
        return posts


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение и удаление поста"""

    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PostDetailSerializer
    queryset = Post.objects.filter()

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class PostCreateView(generics.CreateAPIView):
    """Создание поста"""

    serializer_class = PostCreateSerializer
    queryset = Post.objects.filter()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowListView(generics.ListAPIView):
    """Просмотр подписок"""

    serializer_class = FollowSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["user__username"]

    def get_queryset(self):
        follows = cache.get('follows')
        if not follows:
            follows = Follow.objects.all()
            cache.set('follows', follows)
        return follows


class FollowCreateView(generics.CreateAPIView):
    """Создание подписки"""

    serializer_class = FollowCreateSerializer
    queryset = Follow.objects.filter()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowDestroyView(generics.DestroyAPIView):
    """Удаление подписки"""

    serializer_class = FollowSerializer
    queryset = Follow.objects.filter()
