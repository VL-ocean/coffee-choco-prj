from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Allows admin to manage posts via the admin panel
    """
    list_display = (
        "title",
        "description",
        "status",
        "type",
        "category",
        "created_at",
        "approved",
    )
    search_fields = ["title", "descripton", "content"]
    list_filter = (
        "status",
        "approved",
        "type",
        "category",
        "created_at",
        "updated_at",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Allows admin to manage comments via the admin panel
    """
    list_display = (
        "user",
        "body",
        "created_at",
        "approved",

    )
    search_fields = ["body", "user", "post"]
    list_filter = (
        "created_at",
        "updated_at",
        "user",
        "post",
    )
