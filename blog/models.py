from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    keyword = models.CharField(max_length=64)

    class Meta:
        verbose_name = _('tag')


class Article(models.Model):
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='uploads')
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
