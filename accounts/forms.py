"""accounts/forms.py
   Accounts app forms.
"""
from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    class Meta:
        model = User
        fields = ('username', 'email',)


class UserDeleteForm(forms.Form):
    """Form for update user info."""

    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'password'}),
    )
