from django.urls import path

from .views import PostListView, PostDetailView, PostUpdateView

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<int:pk>/detail", PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/update", PostUpdateView.as_view(), name="post_update"),
]
