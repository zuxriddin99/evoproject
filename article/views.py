from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from hitcount.views import HitCountDetailView

import article
from .forms import NewsForm, ArticleCommentForm
from .models import *
from django.views.generic import DetailView, ListView, TemplateView, CreateView


class ArticleListView(ListView):
    ### to display article or post
    queryset = Article.objects.filter(show=True)
    template_name = 'article/article_list.html'
    context_object_name = 'articles'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ArticleCreateView(CreateView):
    ## add post or article
    form_class = NewsForm
    template_name = 'article/create_post_page.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     """
    #     Handle POST requests: instantiate a form instance with the passed
    #     POST variables and then check if it's valid.
    #     """
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


class ArticleDetailView(HitCountDetailView):
    ## to display article in single page
    model = Article
    template_name = 'article/article_detail.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ArticleCommentForm()
        context.update({
            'total_likes': self.object.total_likes()
        })
        context.update({
            'popular_posts': Article.objects.order_by('-hit_count_generic__hits')[:3],

        })
        return context


def like_article(request):
    article = get_object_or_404(Article, id=request.POST.get('article_id'))
    article.like.add(request.user)

    return HttpResponseRedirect(article.get_absolute_url())


def add_comment_to_aticle(request, pk):
    ## add commentary
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


class CommentView(ListView):
    """to display comment"""
    queryset = ArticleComment.objects.all()
    template_name = "article/article_detail.html"
    context_object_name = "comment_view"
