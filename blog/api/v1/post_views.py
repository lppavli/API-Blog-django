from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from django.db.models import Q


from blog.api.v1.permissions import IsAuthorOrReadOnly
from blog.api.v1.post_serializers import (
    FollowSerializer,
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
)
from blog.models import Post, Follow


class PostListView(generics.ListAPIView):
    """Вывод всех постов"""

    serializer_class = PostListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["author__username"]
    queryset = Post.objects.all().order_by("-created_at")


class PostNewListView(generics.ListAPIView):
    """Вывод непрочитанных постов"""

    serializer_class = PostListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["author__username"]

    def get_queryset(self):
        queryset = Post.objects.filter(~Q(read_users=self.request.user))
        return queryset


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
    queryset = Follow.objects.all()


class FollowCreateView(generics.CreateAPIView):
    """Создание подписки"""

    serializer_class = FollowSerializer
    queryset = Follow.objects.filter()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowDestroyView(generics.DestroyAPIView):
    """Удаление подписки"""

    serializer_class = FollowSerializer
    queryset = Follow.objects.filter()


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset
