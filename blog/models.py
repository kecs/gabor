from django.db import models
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from io import (BytesIO, StringIO)
import os
from PIL import Image
from tinymce import models as tinymce_models


class Tag(models.Model):
    keyword = models.CharField(max_length=64)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.keyword


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    tags = models.ManyToManyField(Tag)
    content = tinymce_models.HTMLField()
    creation_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads')
    image_thumbnail = models.ImageField(upload_to='uploads', blank=True, null=True)
    
    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super().save(**kwargs)

        if not self.make_thumbnail():
            raise Exception('Could not create thumbnail - is the file type valid?')
        
        return super().save(**kwargs)

    def make_thumbnail(self):
        """
        Create and save the thumbnail for the image (simple resize with PIL).
        """

        with open(self.image.name, 'rb') as f:
            try:
                image = Image.open(f)
                image.thumbnail(settings.THUMBNAIL_SIZE, Image.ANTIALIAS)
                thumb_name, thumb_extension = os.path.splitext(self.image.name)
                thumb_extension = thumb_extension.lower()
                thumb_filename = thumb_name + '_thumb' + thumb_extension

                if thumb_extension in ['.jpg', '.jpeg']:
                    FTYPE = 'JPEG'
                elif thumb_extension == '.gif':
                    FTYPE = 'GIF'
                elif thumb_extension == '.png':
                    FTYPE = 'PNG'
                else:
                    return False    # Unrecognized file type

                # Save thumbnail to in-memory file as StringIO
                temp_thumb = BytesIO()
                image.save(temp_thumb, FTYPE)
                temp_thumb.seek(0)

                # Load a ContentFile into the thumbnail field so it gets saved
                self.image_thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=True)
                temp_thumb.close()

                return True

            except Exception as e:
                print('[*]', e)
                return False
