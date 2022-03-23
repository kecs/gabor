from django.urls import path

from .views import (ArticleDetailView, ArticleListView)


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('articles/list/<str:tag>/', ArticleListView.as_view(), name='article_list_by_tag'),
    path('articles/detail/<str:slug>/', ArticleDetailView.as_view(), name='article_detail'),
]
