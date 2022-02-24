from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wallets/<slug:slug>/', views.wallets, name='wallets'),
    path('<slug:slug>/', views.wallet_details, name='wallet_details'),
]

# ad32891d9e98f06b691298bf5189b71d1289bd9d268dc6e9