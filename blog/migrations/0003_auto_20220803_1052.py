# Generated by Django 3.2 on 2022-08-03 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0002_auto_20220802_1024"),
    ]

    operations = [
        migrations.CreateModel(
            name="Follow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="folowing",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="folower",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "subscribe",
                "verbose_name_plural": "subscribe",
                "db_table": "folow",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
            },
        ),
        migrations.RemoveField(
            model_name="post",
            name="subscribes",
        ),
        migrations.DeleteModel(
            name="Subscribe",
        ),
    ]
