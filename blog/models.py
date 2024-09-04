from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    A model to create and manage posts
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_owner"
    )
    title = models.CharField(max_length=300, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.CharField(max_length=500, null=False, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.IntegerField(choices=CATEGORY, default=0)
    type = models.IntegerField(choices=TYPE, default=0)
    approved = models.BooleanField(default=False)
    # featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} | written by {self.user}"