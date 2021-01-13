"""Views for crm app."""
from loguru import logger

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

from .custom_permissions import IsOwner
from .serializers import UserSerializer, CreateUserSerializer, CompanySerializer
from .models import User, Company


class ApiRoot(generics.GenericAPIView):
    """Main page."""
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profile': reverse(UserDetailAPI.name, request=request),
            'companies': reverse('company-list', request=request),
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
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class CompanyViewSet(viewsets.ModelViewSet):
    """Company API. Retrieve, update, partial update, delete."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def create(self, request, *args, **kwargs):
        data = {
            'name': request.data['name'],
            'owner': request.user.id,
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
