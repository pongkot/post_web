from django.urls import path
from .views import post_home

urlpatterns = [
    path("", post_home, name="post_home"),
]
