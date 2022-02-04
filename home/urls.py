from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wallets/<slug:slug>/', views.wallets, name='wallets'),
    path('<slug:slug>/', views.wallet_details, name='wallet_details'),
]