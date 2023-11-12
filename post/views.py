from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "post_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["name"] = "post_list"
        return context
