"""URL config for crm app."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    # TODO: change url to 'users/' for new user
    path('auth/users/', views.CreateUserApi.as_view(), name='create-user'),
]
