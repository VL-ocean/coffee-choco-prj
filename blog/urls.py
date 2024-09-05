from django.urls import path
from .views import AddPost, Posts, PostDetail, DeletePost

urlpatterns = [
    path("add/", AddPost.as_view(), name="add_post"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:pk>/", DeletePost.as_view(), name="delete_post"),
    path("", Posts.as_view(), name="blog"),
]
