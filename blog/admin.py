from django.contrib import admin

from .models import (Article, Tag)
from .forms import ArticleForm


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ('title', 'creation_date')
    search_fields = ['tags__keyword']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)

