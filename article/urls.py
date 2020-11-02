from django.urls import path, include
from django.views.generic import TemplateView

from article import views
from .views import ArticleDetailView, add_comment_to_aticle

app_name = 'articles'

urlpatterns = [

    # path('main/', TemplateView.as_view(template_name="article/mainblog.html"), name='main'),
    # path('profile/', TemplateView.as_view(template_name="article/profile.html"), name='profile'),
    path('post/', views.ArticleListView.as_view(), name='posts'),

    path('', TemplateView.as_view(template_name="article/../templates/register_page/navbar.html"), name='article'),
    path('<int:pk>/', add_comment_to_aticle, name='article_comment'),
    path('add-article/', views.ArticleCreateView.as_view(), name='add_article'),

    path('article-detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('comment-add/<int:pk>/', add_comment_to_aticle, name='article_comment'),
    path('comment-view/<int:pk>/', views.CommentView, name='article_views'),
]