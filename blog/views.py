from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, View, DetailView

from .models import Post
from .forms import LoginForm, SignupForm


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['theme', 'description', 'image']
    template_name = 'blog/post_create.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


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
