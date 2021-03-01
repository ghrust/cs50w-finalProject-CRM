"""accounts/urls.py
    Accounts app urls.
"""
from django.urls import path

from accounts.views import SignUpView, UserDetailView, user_update_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserDetailView.as_view(), name='user-detail'),
    path('update/', user_update_view, name='user-update'),
]
