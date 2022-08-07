from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from blog.models import Post

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Регистрация пользователя"""

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
        )
        return user

    class Meta:
        model = UserModel
        fields = ("id", "username", "password", "email")


class UserListSerializer(serializers.ModelSerializer):
    """Вывод списка пользователей"""

    posts_count = serializers.IntegerField(source="posts.count", read_only=True)

    class Meta:
        model = UserModel
        fields = ("id", "username", "first_name", "last_name", "posts_count")
