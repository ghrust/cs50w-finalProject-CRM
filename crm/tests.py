"""Tests for crm app."""

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from . import views
from .models import User


class RegisterUserTestCase(APITestCase):
    """Test register API."""

    def register_user(self):
        """Register new test user."""

        url = reverse(views.CreateUserApi.name)
        data = {
            'username': 'user01',
            'email': 'user01@test.com',
            'password': 'pass',
            'first_name': 'user',
            'last_name': '01',
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_register_user(self):
        """Ensure we can register new user."""

        response = self.register_user()

        self.assertEqual(response.status_code, 201)

        User.objects.first()
        self.assertEqual(response.data['username'], 'user01')

    def test_login_user(self):
        """Ensure we can login user."""

        self.register_user()
        response = self.client.login(username='user01', password='pass')

        self.assertEqual(response, True)
