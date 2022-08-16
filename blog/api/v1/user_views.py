from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.models import Count
from rest_framework import generics

from rest_framework.permissions import AllowAny

from blog.api.v1.user_serializers import UserSerializer, UserListSerializer

UserModel = get_user_model()


class CreateUserView(generics.CreateAPIView):
    """Создание пользвателя"""

    permission_classes = (AllowAny,)
    model = get_user_model()
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    """Вывод всех пользователей по убыванию количества постов"""

    serializer_class = UserListSerializer

    def get_queryset(self):
        users = cache.get('posts')
        if not users:
            users = User.objects.annotate(posts_count=Count("posts")).order_by("-posts_count")
            cache.set('users', users)
        return users
