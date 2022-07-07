from django.forms import ModelForm
from .models import Post


class ProductForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author_post', 'heading_post', 'text_post', 'links_posts']
        labels = {
            'heading_post': ('Заголовок'),
            'text_post': ('Текст публикации'),
            'links_posts': ('Категория'),
            'author_post': ('Автор публикации')
        }