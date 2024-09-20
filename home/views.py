from django.views.generic import ListView
from blog.models import Post


class Index(ListView):
    """ View home page """
    template_name = 'home/index.html'
    model = Post
    context_object_name = 'posts'

    queryset = Post.objects.filter(
        status=1, approved=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = self.queryset[:3]
        return context
