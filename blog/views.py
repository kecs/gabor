from django.views.generic.list import ListView
from django.views.generic import DetailView

from blog.models import (Article, Tag)


class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        tag = self.kwargs.get('tag')

        if tag:
            return qs.filter(tags__keyword=tag)
        else:
            return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()[:10]

        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'

