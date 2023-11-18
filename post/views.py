from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .models import Post


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
