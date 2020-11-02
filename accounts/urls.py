from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = 'account'
urlpatterns = [

    path('profile/', TemplateView.as_view(template_name="article/profile.html"), name='profile'),
    path('main/', TemplateView.as_view(template_name="article/mainblog.html"), name='main'),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', TemplateView.as_view(template_name="base.html"), name='mainpage'),

]
