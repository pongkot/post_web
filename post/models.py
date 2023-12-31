from django.db import models
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

    def stars(self):
        comments = self.post_comment.all()
        sum_user_star = 0
        total_user_stars = len(comments)
        if total_user_stars > 0:
            for comment in comments:
                sum_user_star += comment.user_rating
            return sum_user_star // total_user_stars
        else:
            return 0


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
