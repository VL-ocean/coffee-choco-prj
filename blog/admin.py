from django.contrib import admin
from .models import Post


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
    prepopulated_fields = {"slug": ("title",)}
