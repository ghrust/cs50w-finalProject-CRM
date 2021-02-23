"""crm/admin.py
Register models in admin panel.
"""
from django.contrib import admin

from crm.models import Customer


admin.site.register(Customer)
