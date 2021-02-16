"""crm/urls.py
URL configurations for CRM app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('customers/<int:pk>/', views.CustomerView.as_view(),
         name='customer-detail'),
]
