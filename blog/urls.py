from django.urls import path
from .views import AddPost, Posts, PostDetail

urlpatterns = [
    path("", AddPost.as_view(), name="add_post"),
    path("blog/", Posts.as_view(), name="blog"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
]
