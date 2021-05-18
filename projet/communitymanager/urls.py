from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('communautes/', views.communaute),
    path('accounts/profile', views.login_successful),
]
