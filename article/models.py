from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify


# Create your models here.

class Categotry(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.tag


class Article(models.Model):
    """ Список статей """

    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True)

    description = RichTextUploadingField(blank=True, null=True)
    tag = models.ManyToManyField(Tag, related_name='tags', blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)
    moderator = models.BooleanField(default=True)

    # def save(self, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(**kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = '%s-%s' % (self.id, slugify(self.title))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title


class PostLike(models.Model):
    post = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class PostFavourite(models.Model):
    post = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)