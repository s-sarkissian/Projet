from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/communautes/', views.communautes),
    path('accounts/profile/', views.login_successful),
    path('accounts/profile/communaute/<int:id>', views.communaute),
    path('accounts/profile/post/<int:id>', views.post),
]
