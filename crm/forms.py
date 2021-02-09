from django import forms

from crm.models import User


class SignUpForm(forms.ModelForm):
    """Form for registering new user."""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
