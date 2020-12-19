from django.shortcuts import render

from rest_framework import generics

from .serializers import CreateUserSerializer
from .models import User


class CreateUserApi(generics.CreateAPIView):
    """Register new user."""
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
