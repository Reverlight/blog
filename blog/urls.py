from django.urls import path

from blog.views import PostListView, PostCreateView, UserCreateView, UserLoginView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('user/signup/', UserCreateView.as_view(), name='signup'),
    path('user/login/', UserLoginView.as_view(), name='login')
]
