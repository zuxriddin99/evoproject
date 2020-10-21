from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="base.html"), name='mainpage'),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
