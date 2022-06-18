from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login
from django.urls import path, include

from .forms import LoginForm
from account import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('register/', views.register, name='register'),
    path('callback-request/', views.callback_request, name='callback-request'),
    url(r'^logout/$', lambda request: logout_then_login(request, "/"), name='logout'),

    path("", include("django.contrib.auth.urls"))
]