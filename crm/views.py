"""
crm/views.py
CRM app views.
"""
from django.views.generic.base import TemplateView


class DashboardView(TemplateView):
    """View for main page."""
    template_name = 'crm/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = '-'
        return context
