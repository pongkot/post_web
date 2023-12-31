# Generated by Django 4.2.7 on 2023-11-12 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("comment_text", models.CharField(max_length=100)),
                ("user_rating", models.IntegerField()),
                ("is_approved", models.BooleanField()),
                ("date_created", models.DateTimeField(auto_now=True)),
                (
                    "commented_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_comment",
                        to="post.post",
                    ),
                ),
            ],
        ),
    ]
