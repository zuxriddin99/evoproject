from ckeditor.widgets import CKEditorWidget

from django import forms
from .models import Article, ArticleComment


class NewsForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(attrs={'placeholder': 'Describe your order in more detail...'}),
                                  required=False)

    class Meta:
        model = Article
        fields = ['category', 'title', 'description', 'tag', 'show', 'moderator']


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('article_comment', 'parent')
