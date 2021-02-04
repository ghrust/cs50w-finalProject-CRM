"""URL configurations for CRM app."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.SignUpView.as_view(), name='signup'),
]