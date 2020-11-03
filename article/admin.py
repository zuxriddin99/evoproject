from django.contrib import admin

# Register your models here.
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'category', 'created_date')
    search_fields = ('owner', 'title', 'tag')
    list_filter = ['owner', 'title', 'category', 'tag', 'show', 'hit_count_generic']


admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name', 'parent')
    list_filter = ('name', 'parent')


admin.site.register(Categotry, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'slug')
    search_fields = ('name',)


admin.site.register(Tag, TagAdmin)


class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'article', 'parent', 'add_comment_date')
    search_fields = ('owner', 'article', 'parent', 'add_comment_date')
    list_filter = ('owner', 'article', 'parent', 'add_comment_date')


admin.site.register(ArticleComment, ArticleCommentAdmin)

admin.site.register(ChatForUser)
