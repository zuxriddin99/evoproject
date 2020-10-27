from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewsForm
from .models import *
from django.views.generic import DetailView, ListView, TemplateView, CreateView


class PostListView(ListView):
    ### for  post's view
    queryset = Article.objects.filter(show=True)
    template_name = 'blog/mainblog.html'
    context_object_name = 'posts'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = NewsForm()
    #     return context


class ArticleCreateView(CreateView):
    form_class = NewsForm
    template_name = 'blog/create_post_page.html'

    def get_success_url(self):
        return redirect('articles:article_detail')


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             article = form.save()
#             return redirect('/')
#     else:
#         form = NewsForm()
#     return render(request, 'blog/mainblog.html', {'form': form})

class PostDetailView(DetailView):
    model = Article

    template_name = 'blog/article_detail.html'
