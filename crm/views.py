from rest_framework import generics
from rest_framework.response import Response

from .serializers import CreateUserSerializer
from .models import User


class ApiRoot(generics.GenericAPIView):
    """Main page."""
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'companies': '',
            'customers': '',
        })


class CreateUserApi(generics.CreateAPIView):
    """Register new user."""
    # TODO: add name
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
