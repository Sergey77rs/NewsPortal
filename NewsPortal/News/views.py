from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class NewsList(ListView):
    model = Post
    ordering = '-id'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class OnenewsDetail(DetailView):
    model = Post
    template_name = 'onenews.html'
    context_object_name = 'onenews'

