from django.urls import path
from .views import AddPost, Posts

urlpatterns = [
    path("", AddPost.as_view(), name="add_post"),
    path("blog/", Posts.as_view(), name="blog"),
]
