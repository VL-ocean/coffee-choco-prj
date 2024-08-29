from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
CATEGORY = ((0, "Coffee"), (1, "Chocolate"))
TYPE = ((0, "Article"), (1, "Recipe"))


# Create your models here.
class Post(models.Model):
    User_ID = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
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
        return f"{self.title} | written by {self.User_ID}"


class Comment(models.Model):
    Post_ID = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    User_ID = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment {self.body} by {self.User_ID}"