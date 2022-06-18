from django.urls import path

from portal import views

urlpatterns = [
    path('', views.home, name='portal-home'),
    path('profile/', views.profile, name='profile'),
    path('payment-method/', views.payment_method, name='payment-method'),
]