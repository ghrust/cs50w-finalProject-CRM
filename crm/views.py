"""
crm/views.py
CRM app views.
"""
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from .models import Customer


class DashboardView(TemplateView):
    """View for main page."""
    template_name = 'crm/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = '-'
        return context


class CustomerView(DetailView):
    """View for customer page."""
    model = Customer
