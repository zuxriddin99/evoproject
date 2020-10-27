from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import ModelForm, forms
from django import forms
from .models import Article


class NewsForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(attrs={'placeholder': 'Describe your order in more detail...'}),
                                  required=False)

    class Meta:
        model = Article
        fields = '__all__'