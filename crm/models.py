""" Models for crm app database."""

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User."""


class Company(models.Model):
    """User's company(organization)."""

    name = models.CharField(
        verbose_name='company name',
        max_length=200,
    )

    owner = models.ForeignKey(
        User,
        verbose_name='company owner',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.name)
