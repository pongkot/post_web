from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)

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
        context["name"] = "post_list"
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


class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = ["title", "author", "body"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["name"] = "post_create"
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_list")


def add_post_comment(request, post_id):
    if request.method == "POST":
        Comment.objects.create(
            commented_post_id=post_id,
            user_rating=request.POST.get("user_star"),
            comment_text=request.POST.get("comment"),
            is_approved=True,
        )
    return HttpResponseRedirect(f"/post/{post_id}/detail#comment")
