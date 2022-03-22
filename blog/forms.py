from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Article


class ArticleForm(forms.ModelForm):    
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'tags']
