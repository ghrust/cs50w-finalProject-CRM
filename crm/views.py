"""Views for crm app."""

from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .custom_permissions import IsOwner
from .serializers import UserSerializer, CreateUserSerializer, CompanySerializer
from .models import User, Company


class ApiRoot(generics.GenericAPIView):
    """Main page."""
    name = 'api-root'

    def get(self, request):
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
        """Create company. Add authorized user as company owner."""
        data = {
            'name': request.data['name'],
            'owner': request.user.id,
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        """Get company list of authorized user."""
        user = request.user
        queryset = user.companies.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
