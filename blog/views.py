from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm
from .models import Category, Post

#
# def blog_get(request):
#     objects = Post.objects.all()
#     return render(request, 'blog/index.html', {'objects': objects})


class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ('Главная страница',)
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('category')


class DetailPost(DetailView):
    model = Post
    context_object_name = 'blog_item'
    template_name = 'blog/blog_item.html'


class CreatePost(CreateView):
    form_class = PostForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('blog')
