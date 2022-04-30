from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, View

from .models import Post, Comment
from .forms import LoginForm, SignupForm, CommentForm


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['theme', 'description', 'image']
    template_name = 'blog/post_create.html'


class PostDetailView(LoginRequiredMixin, View):
    template_name = 'blog/post_detail.html'
    post_model = Post
    comment_model = Comment
    comment_form_class = CommentForm

    def get(self, request, pk):
        post = get_object_or_404(self.post_model, pk=pk)
        comments = self.comment_model.objects.filter(post=post)
        comment_form = self.comment_form_class()

        context = {
            'comment_form': comment_form,
            'comments': comments,
            'post': post
        }
        return render(request, self.template_name, context=context)

    def post(self, request, pk):
        post = get_object_or_404(self.post_model, pk=pk)
        comments = self.comment_model.objects.filter(post=post)
        comment_form = self.comment_form_class(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

        context = {
            'comment_form': comment_form,
            'comments': comments,
            'post': post
        }
        return render(request, self.template_name, context=context)


class UserCreateView(View):
    template_name = 'blog/user_create.html'
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context=context)


class UserLoginView(View):
    template_name = 'blog/user_login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('home')

        context = {
            'form': form
        }
        return render(request, self.template_name, context=context)
