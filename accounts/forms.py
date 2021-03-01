"""accounts/forms.py
   Accounts app forms.
"""
from django.contrib.auth import forms
from django.forms import ModelForm

from accounts.models import User


class UserCreationForm(forms.UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    class Meta:
        model = User
        fields = ('username', 'email',)


class UserUpdateForm(ModelForm):
    """Form for update user info."""

    class Meta:
        model = User
        fields = ['username']
