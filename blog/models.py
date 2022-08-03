import uuid

from django.contrib.auth.models import User
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _
from django.db import models


class Post(models.Model):
    """ Модель для постов"""
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_('description'), blank=True)
    created_at = models.DateTimeField(_("date_create"), auto_now_add=True)
    updated_at = models.DateTimeField(_("date_update"), auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name=_("author"))
    read_users = models.ManyToManyField(User, through="UserReadPost", verbose_name=_("reads"))

    def __str__(self):
        return self.title

    class Meta:
        db_table = "post"
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-created_at']


class Follow(models.Model):
    # пользователь, который подписывается
    user = models.ForeignKey(User, related_name=_("folower"),
                             on_delete=models.CASCADE, verbose_name=_("user"))
    # пользователь, на которого подписываются
    author = models.ForeignKey(User, related_name=_("folowing"),
                               on_delete=models.CASCADE, verbose_name=_("author"))

    def __str__(self):
        return ""

    class Meta:
        db_table = "folow"
        verbose_name = _("subscribe")
        verbose_name_plural = _("subscribe")


class UserReadPost(models.Model):
    user = models.ForeignKey(User, related_name='user_read_posts', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='posts_read_by_users', on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ""

    class Meta:
        db_table = "reads"
        verbose_name = _("reads")
        verbose_name_plural = _("reads")
