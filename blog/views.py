from django.views.generic import ListView, CreateView

from blog.models import Post, User


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['theme', 'description', 'image']
    template_name = 'blog/post_create.html'


class UserCreateView(CreateView):
    model = User
    fields = ['username', 'password']
    template_name = 'blog/user_create.html'
