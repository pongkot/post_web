from django.views.generic import ListView, DetailView, UpdateView

from .models import Post, Comment


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "post_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["name"] = "post_list"
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        commented_post_id = self.kwargs["pk"]
        comments = Comment.objects.filter(commented_post_id=commented_post_id)
        avg_user_star = 0
        if len(comments) > 0:
            total_comment = len(comments)
            total_user_star = 0
            for comment in comments:
                total_user_star += comment.user_rating
            avg_user_star = total_user_star // total_comment
        context["name"] = "post_list"
        context["user_star"] = avg_user_star
        return context


class PostUpdateView(UpdateView):
    model = Post
    context_object_name = "post"
    template_name = "post_update.html"
    fields = ["title", "author", "body"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["name"] = "post_update"
        return context
