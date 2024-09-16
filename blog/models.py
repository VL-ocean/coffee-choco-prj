from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


# Choice Fields
STATUS = ((0, "Draft"), (1, "Published"))
CATEGORY = ((0, "Coffee"), (1, "Chocolate"))
TYPE = ((0, "Article"), (1, "Recipe"))


class Post(models.Model):
    """
    A model to create and manage posts
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_owner")
    title = models.CharField(max_length=300, unique=True, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    content = RichTextField(max_length=30000, null=False, blank=False)
    image = ResizedImageField(
        size=None,
        quality=100,
        upload_to="posts/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.IntegerField(choices=CATEGORY, default=0)
    type = models.IntegerField(choices=TYPE, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} | written by {self.user}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_owner")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment {self.body} by {self.user}"