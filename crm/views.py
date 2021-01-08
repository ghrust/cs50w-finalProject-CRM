"""Views for crm app."""

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import UserSerializer, CreateUserSerializer
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


class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """User profile API. Get, update, delete user info."""
    name = 'user-detail'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)