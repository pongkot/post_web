from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostCreateView,
    PostDeleteView,
    add_post_comment,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("new", PostCreateView.as_view(), name="post_create"),
    path("<int:post_id>/add_comment", add_post_comment, name="add_post_comment"),
    path("<int:pk>/detail", PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/update", PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
]
