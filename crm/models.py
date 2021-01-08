""" Models for crm app database."""

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User."""


class Customer(models.Model):
    """Customer."""

    first_name = models.CharField('first name', max_length=150, blank=False)

    last_name = models.CharField('last name', max_length=150, blank=False)

    email = models.EmailField("customer's email address", blank=True)

    phone_number = models.CharField(
        verbose_name="customer's phone number",
        max_length=20,
        blank=False,
    )

    address = models.CharField(
        verbose_name="customer's address",
        max_length=200,
        blank=True,
    )

    date_joined = models.DateTimeField("date joined", auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Company(models.Model):
    """User's company(organization)."""

    name = models.CharField(
        verbose_name='company name',
        max_length=200,
        blank=False,
    )

    owner = models.ForeignKey(
        User,
        related_name='companies',
        verbose_name='company owner',
        on_delete=models.CASCADE,
        blank=False,
    )

    customers = models.ManyToManyField(
        Customer,
        verbose_name="company's clients",
        related_name="customers",
        blank=True,
    )

    def __str__(self):
        return str(self.name)
