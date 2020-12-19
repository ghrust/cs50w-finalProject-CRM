from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Customer, Company

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_joined']


class CreateUserSerializer(serializers.ModelSerializer):
    """Serializer for register new user.
    """
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'required': True,
                'validators': [UniqueValidator(queryset=User.objects.all())],
            },
        }



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
