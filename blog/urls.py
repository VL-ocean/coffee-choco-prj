from django.urls import path
from .views import (
    AddPost,
    Posts,
    PostDetail,
    DeletePost,
    EditPost,
    AddComment,
    DeleteComment,
)

urlpatterns = [
    path("add/", AddPost.as_view(), name="add_post"),
    path("", Posts.as_view(), name="blog"),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<int:pk>/", DeletePost.as_view(), name="delete_post"),
    path("edit/<int:pk>/", EditPost.as_view(), name="edit_post"),
    path("comment/add/", AddComment.as_view(), name="add_comment"),
    path(
        "comment/delete/<int:pk>/",
        DeleteComment.as_view(),
        name="delete_comment"
    ),
]
