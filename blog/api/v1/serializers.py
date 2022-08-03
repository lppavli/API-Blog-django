from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import serializers

from blog.models import Post, Follow


class UserSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'posts']


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = '__all__'
