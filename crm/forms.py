from django import forms

from crm.models import Customer, User


class SignUpForm(forms.ModelForm):
    """Form for registering new user."""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'email']
