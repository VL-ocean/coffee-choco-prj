from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm


class Posts(ListView):
    """View all posts"""

    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 6

    queryset = Post.objects.filter(
        status=1, approved=True).order_by('-created_at')

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            posts = self.model.objects.filter(
                Q(title__contains=query) | 
                Q(description__contains=query) |
                Q(content__contains=query) |
                Q(category__contains=query) |
                Q(type__contains=query),
                status=1, 
                approved=True
            )
        else:
            posts = self.model.objects.filter(status=1, approved=True).order_by('-created_at')
        return posts


class PostDetail(DetailView):
    """View a single post"""

    template_name = "blog/post_detail.html"
    model = Post
    context_object_name = "post"


class AddPost(LoginRequiredMixin, CreateView):
    """Add post view"""

    template_name = "blog/add_post.html"
    model = Post
    form_class = PostForm
    success_url = "/blog/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPost, self).form_valid(form)


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a post"""

    template_name = "blog/edit_post.html"
    model = Post
    form_class = PostForm
    success_url = "/blog/"

    def post(request, *args, **kwargs):
        self.object.approved = False

    def test_func(self):
        return self.request.user == self.get_object().user


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a post"""

    model = Post
    success_url = "/blog/"

    def test_func(self):
        return self.request.user == self.get_object().user
