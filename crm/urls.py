"""URL config for crm app."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('users/', views.CreateUserApi.as_view(), name=views.CreateUserApi.name),
]
