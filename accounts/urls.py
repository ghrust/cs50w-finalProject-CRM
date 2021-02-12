"""Accounts app urls."""
from django.urls import path

from accounts.views import SignUpView, UserDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserDetailView.as_view(), name='user-detail'),
]
