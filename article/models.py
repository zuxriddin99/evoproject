from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from hitcount.models import HitCountMixin, HitCount


# Create your models here.

class Categotry(MPTTModel):
    """  for category """
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tag(models.Model):
    tag = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.tag

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = '%s-%s' % (self.id, slugify(self.tag))
            self.save(update_fields=['slug'])


class Article(models.Model, HitCountMixin):
    """ Список статей """

    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Categotry, blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, blank=True, unique=True)

    description = RichTextUploadingField(blank=True, null=True)
    tag = models.ManyToManyField(Tag, related_name='tags', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)
    moderator = models.BooleanField(default=True)
    like = models.ManyToManyField(User, related_name='like', blank=True)

    """for count views of number"""
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = '%s-%s' % (self.id, slugify(self.title))
            self.save(update_fields=['slug'])

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def get_total_likes(self):
        return self.like.count()

    """ send pk to detail page  """

    def get_absolute_url(self):
        return reverse('articles:article_detail', kwargs={'pk': str(self.pk)})


class ArticleLike(models.Model):
    article = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    number_of_like = models.PositiveIntegerField(default=0)


class ArticleView(models.Model):
    article = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    number_of_view = models.PositiveIntegerField(default=0)


class ArticleFavourite(models.Model):
    article = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class ChatForUser(models.Model):
    message_sender = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='message_sender')
    message_receiver = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='message_receiver')
    text = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)


class ArticleComment(MPTTModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    article_comment = models.TextField()
    add_comment_date = models.DateTimeField(auto_now_add=True, )

    class Meta:
        verbose_name = 'ArticleComment'
        verbose_name_plural = 'ArticleComments'

    def __str__(self):
        return self.article_comment
