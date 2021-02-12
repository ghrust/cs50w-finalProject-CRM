"""accounts/views.py
   Accounts app views.
"""
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from .forms import UserCreationForm


class SignUpView(CreateView):
    """New user register view."""
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserDetailView(TemplateView):
    """User detail(profile) view."""
    template_name = 'registration/profile.html'
