from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewsForm, ArticleCommentForm
from .models import *
from django.views.generic import DetailView, ListView, TemplateView, CreateView


# @login_required()
class ArticleListView(ListView):
    ### for  post's view
    queryset = Article.objects.filter(show=True)
    template_name = 'blog/mainblog.html'
    context_object_name = 'articles'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ArticleCreateView(CreateView):
    form_class = NewsForm
    template_name = 'blog/create_post_page.html'


class ArticleDetailView(DetailView):
    model = Article

    template_name = 'blog/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['articles'] = Article.objects.all()
        context['form'] = ArticleCommentForm()
        return context


def add_comment_to_aticle(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user
            comment.article = article
            comment.save()
    else:
        form = ArticleCommentForm()
    # return HttpResponse('ok')
    return redirect(article)