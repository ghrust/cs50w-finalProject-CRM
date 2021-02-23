"""crm/urls.py
URL configurations for CRM app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(),
         name='customer-detail'),
    path('customers/new', views.customer_create_view,
         name='customer-form'),
]
