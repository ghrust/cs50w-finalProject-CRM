"""
crm/views.py
CRM app views.
"""
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from loguru import logger

from .forms import CustomerForm
from .models import Customer, Product


class DashboardView(LoginRequiredMixin, TemplateView):
    """View for main page."""
    template_name = 'crm/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_customers'] = Customer.objects.all()
        return context


class CustomerDetailView(LoginRequiredMixin, DetailView):
    """View for customer page."""
    model = Customer


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    """View for update edit/update customer's data."""
    model = Customer
    fields = ['first_name', 'last_name', 'phone', 'email']


class CustomerListView(LoginRequiredMixin, ListView):
    """Customer list page."""
    model = Customer


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    """View to delete customer."""
    model = Customer
    success_url = reverse_lazy('customer-list')


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


# Product.
class ProductCreateView(LoginRequiredMixin, CreateView):
    """Product create page."""
    model = Product
    fields = ['name', 'category', 'price']
    # TODO: change to 'product_detail'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
