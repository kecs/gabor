from django.views.generic.list import ListView

from blog.models import (Article, Tag)


class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()[:10]

        return context
