from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Comment
from .forms import PostForm


class Posts(ListView):
    """View all posts"""

    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 6

    queryset = Post.objects.filter(
        status=1,
        approved=True
    ).order_by("-created_at")

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            posts = self.model.objects.filter(
                Q(title__contains=query)
                | Q(description__contains=query)
                | Q(content__contains=query)
                | Q(category__contains=query)
                | Q(type__contains=query),
                status=1,
                approved=True,
            )
        else:
            posts = self.model.objects.filter(
                status=1,
                approved=True
            ).order_by(
                "-created_at"
            )
        return posts


class PostDetail(DetailView):
    """View a single post"""

    template_name = "blog/post_detail.html"
    model = Post
    context_object_name = "post"


class AddPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add post view"""

    template_name = "blog/add_post.html"
    model = Post
    form_class = PostForm
    success_url = "/blog/"
    success_message = "The post has been created successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPost, self).form_valid(form)


class EditPost(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    """Edit a post"""

    template_name = "blog/edit_post.html"
    model = Post
    form_class = PostForm
    success_url = "/blog/"
    success_message = "The post has been updated successfully."

    def test_func(self):
        return self.request.user == self.get_object().user


class DeletePost(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    """Delete a post"""

    model = Post
    success_url = "/blog/"
    success_message = "The post has been deleted successfully"

    def test_func(self):
        return self.request.user == self.get_object().user


class AddComment(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    """Add a comment"""

    def post(self, request, *args, **kwargs):
        body = request.POST.get("body")
        user = request.user
        post_id = request.POST.get("post_id")
        post = get_object_or_404(Post, id=post_id)

        comment_instance = Comment(body=body, user=user, post=post)
        comment_instance.save()
        messages.success(request, "The comment has been created successfully!")

        return redirect(f"/blog/{post_id}")

    def get(self, request, *args, **kwargs):
        return redirect(f"/blog/{post_id}")


class DeleteComment(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    """Delete a comment"""

    model = Comment
    success_url = "/blog/"
    success_message = "The comment has been deleted successfully"

    def test_func(self):
        return self.request.user == self.get_object().user
