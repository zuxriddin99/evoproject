from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Article)
admin.site.register(Categotry)
admin.site.register(Tag)
admin.site.register(ChatForUser)
admin.site.register(ArticleComment)