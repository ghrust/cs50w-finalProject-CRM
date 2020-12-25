"""Views for crm app."""

from rest_framework import generics
from rest_framework.response import Response

from .serializers import CreateUserSerializer
from .models import User


class ApiRoot(generics.GenericAPIView):
    """Main page."""
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profile': '',
            'companies': '',
            'customers': '',
        })


class CreateUserApi(generics.CreateAPIView):
    """Register new user."""
    name = 'user-api'
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
