from django.contrib import admin
from django.contrib.auth.models import User

from .models import Post, Follow, UserReadPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "author", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("updated_at",)
    empty_value_display = "-пусто-"


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "author")
    search_fields = ("user", "author")
    empty_value_display = "-пусто-"


@admin.register(UserReadPost)
class UserReadPostAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "post", "read_at")
    search_fields = ("user", "post")
    empty_value_display = "-пусто-"
