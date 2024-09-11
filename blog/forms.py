from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Post


class PostForm(forms.ModelForm):
    """Form to create a post"""

    class Meta:
        model = Post
        fields = [
            "title",
            "description",
            "content",
            "image",
            "image_alt",
            "status",
            "type",
            "category",
        ]

        content = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Post Title",
            "description": "Description",
            "content": "Main Content",
            "image": "Post Image",
            "image_alt": "Image Description",
            "status": "Post Status",
            "category": "Category",
            "type": "Post Type",
        }