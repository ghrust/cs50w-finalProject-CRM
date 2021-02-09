"""accounts/forms.py
   Accounts app forms.
"""
from django.contrib.auth import forms
from django.contrib.auth.forms import UsernameField

from accounts.models import User


class UserCreationForm(forms.UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    class Meta:
        model = User
        fields = ('username', 'email',)
