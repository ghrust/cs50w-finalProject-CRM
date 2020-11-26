from rest_framework import serializers
from .models import User, Customer, Company

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_joined']


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for Customer model.
    """
    class Meta:
        model = Customer
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer for Company model.
    """
    class Meta:
        model = Company
        fields = '__all__'
