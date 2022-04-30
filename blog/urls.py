from django.urls import path

from blog.views import PostListView, PostCreateView, UserCreateView

urlpatterns = [
    path('', PostListView.as_view()),
    path('post/', PostCreateView.as_view()),
    path('user/signup/', UserCreateView.as_view(), name='signup')
]
