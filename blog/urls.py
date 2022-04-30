from django.urls import path

from blog.views import PostListView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view()),
    path('post/', PostCreateView.as_view())
]
