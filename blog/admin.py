from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
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
    list_display = (
        "user",
        "body",
        "created_at",
        "updated_at",
        "approved",
    )
    search_fields = ["body", "post", "user"]
    list_filter = (
        "post",
        "approved",
        "created_at",
        "updated_at",
    )