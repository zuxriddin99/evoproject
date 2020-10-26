from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import DetailView, ListView


class PostListView(ListView):
    queryset = Article.objects.filter(show=True)
    template_name = 'blog/mainblog.html'
    context_object_name = 'posts'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['asd'] = 'Category.objects.all()'
        return context
