"""accounts/views.py
   Accounts app views.
"""
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

from .forms import CustomUserCreationForm, UserDeleteForm


class SignUpView(CreateView):
    """New user register view."""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserDetailView(TemplateView):
    """User detail(profile) view."""
    template_name = 'registration/profile.html'


@login_required
def user_delete_view(request):
    """Delete user account."""
    if request.method == 'POST':
        # Check password to verify deletion.
        form = UserDeleteForm(request.POST)
        if form.is_valid():
            if check_password(form.cleaned_data['password'], request.user.password):
                request.user.delete()
                return redirect('signup')
            else:
                return render(
                    request,
                    'registration/user_delete_form.html',
                    {'form': form, 'error': 'password is wrong!'})

    form = UserDeleteForm()
    return render(request, 'registration/user_delete_form.html', {'form': form})
