"""
crm/views.py
CRM app views.
"""
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

from .forms import CustomerForm
from .models import Customer


class DashboardView(TemplateView):
    """View for main page."""
    template_name = 'crm/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_customers'] = Customer.objects.all()
        return context


class CustomerDetailView(DetailView):
    """View for customer page."""
    model = Customer


class CustomerUpdateView(UpdateView):
    """View for update edit/update customer's data."""
    model = Customer
    fields = ['first_name', 'last_name', 'phone', 'email']


class CustomerListView(ListView):
    """Customer list page."""
    model = Customer


@login_required
def customer_create_view(request):
    """Add new customer."""
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_customer = Customer.objects.create(**form.cleaned_data)
            new_customer.vendor = request.user
            new_customer.save()
            return redirect('dashboard')
    else:
        form = CustomerForm()

    return render(request, 'crm/customer_form.html', {'form': form})
