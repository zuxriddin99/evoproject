from django.urls import path, include
from django.views.generic import TemplateView

from article import views
from .views import PostDetailView

app_name = 'articles'

urlpatterns = [

    # path('main/', TemplateView.as_view(template_name="blog/mainblog.html"), name='main'),
    # path('profile/', TemplateView.as_view(template_name="blog/profile.html"), name='profile'),
    path('post/', views.PostListView.as_view(), name='posts'),
    path('', TemplateView.as_view(template_name="blog/heder_footer.html"), name='blog'),
    path('add_article/', views.ArticleCreateView.as_view(), name='add_article'),

    path('<int:pk>/', PostDetailView.as_view(), name='article_detail')
]