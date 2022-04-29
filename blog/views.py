from django.views.generic import ListView, CreateView

from blog.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'


