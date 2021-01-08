"""Serializers for crm app."""

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Customer, Company


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for User model."""
    companies = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='company-detail')

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'date_joined', 'companies']
        extra_kwargs = {'date_joined': {'read_only': True}}


class CreateUserSerializer(serializers.ModelSerializer):
    """Serializer for register new user."""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password',
                  'date_joined']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'required': True,
                'validators': [UniqueValidator(queryset=User.objects.all())],
            },
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer model."""
    class Meta:
        model = Customer
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    """Serializer for Company model."""
    class Meta:
        model = Company
        fields = '__all__'
