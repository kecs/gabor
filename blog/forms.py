from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label=_('title'), max_length=255)
    
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'tags']
