from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_text = models.CharField(max_length=100)
    user_rating = models.IntegerField()
    commented_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comment"
    )
    is_approved = models.BooleanField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text
