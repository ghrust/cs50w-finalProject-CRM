"""accounts/views.py
   Accounts app views.
"""
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect

from .forms import UserCreationForm, UserUpdateForm


class SignUpView(CreateView):
    """New user register view."""
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserDetailView(TemplateView):
    """User detail(profile) view."""
    template_name = 'registration/profile.html'


def user_update_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user = request.user
            user.username = form.cleaned_data['username']
            user.save()
            return redirect('user-detail')
        else:
            return render(request, 'registration/user_update_form.html', {'form': form})
    else:
        form = UserUpdateForm()

    return render(request, 'registration/user_update_form.html', {'form': form})
