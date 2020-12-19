"""URL config for crm app."""

from django.urls import path

from . import views

urlpatterns = [
    path('auth/users/', views.CreateUserApi.as_view(), name='create-user'),
]
