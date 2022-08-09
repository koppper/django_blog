from django.urls import path
from blog.views import PostList, DetailPost, CreatePost

urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('<int:pk>/', DetailPost.as_view(), name='blog_item'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
]
