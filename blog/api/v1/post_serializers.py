from rest_framework import serializers

from blog.models import Post, Follow


class PostListSerializer(serializers.ModelSerializer):
    """Вывод списка постов"""

    class Meta:
        model = Post
        fields = ["id", "title", "description", "author"]


class PostDetailSerializer(serializers.ModelSerializer):
    """Вывод полной информации о посте"""

    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    """Создание поста"""

    class Meta:
        model = Post
        fields = ["title", "description"]


class FollowSerializer(serializers.ModelSerializer):
    """Подписка на другого пользователя"""

    class Meta:
        model = Follow
        fields = ["id", "author"]
