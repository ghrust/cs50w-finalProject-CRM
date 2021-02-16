"""crm/models.py
CRM app models
"""
from django.db import models


class Customer(models.Model):
    """Customer model."""
    first_name = models.CharField(
        verbose_name='First name',
        max_length=140,
    )
    last_name = models.CharField(
        verbose_name='Last name',
        max_length=140,
    )
    phone = models.IntegerField(
        verbose_name="Customer's phone number",
    )
    email = models.EmailField(verbose_name="Customer's email")
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}\nPhone: {self.phone}'
