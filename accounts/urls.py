"""accounts/urls.py
    Accounts app urls.
"""
from django.urls import path

from accounts.views import SignUpView, UserDetailView, user_delete_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserDetailView.as_view(), name='user-detail'),
    path('delete/', user_delete_view, name='delete_account'),
]
