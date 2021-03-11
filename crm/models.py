"""crm/models.py
CRM app models
"""
from django.db import models
from django.urls import reverse

from accounts.models import User


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
    vendor = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """Return URL for redirecting after success update."""
        return reverse('customer-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}\nPhone: {self.phone}'


class Category(models.Model):
    """Product category."""
    name = models.CharField(
        verbose_name='product category',
        max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    """Product model."""
    name = models.CharField(
        verbose_name='product name',
        max_length=150)
    price = models.CharField(verbose_name='product price', max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'name: {self.name}, price: {self.price}'


class Order(models.Model):
    """Order model."""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vendor = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payed_price = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'ID: {self.id}\nCustomer {self.customer} payed {self.payed_price} for product {self.product}'
