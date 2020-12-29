"""Tests for crm app."""

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from . import views
from .models import User


class RegisterUserTestCase(APITestCase):
    """Test register API."""

    USER_DATA = {
            'username': 'user01',
            'email': 'user01@test.com',
            'password': 'pass',
            'first_name': 'user',
            'last_name': '01',
        }

    def register_user(self, data=USER_DATA):
        """Register new test user."""

        url = reverse(views.CreateUserApi.name)

        response = self.client.post(url, data, format='json')
        return response

    def test_register_user(self):
        """Ensure we can register new user."""

        response = self.register_user()

        self.assertEqual(response.status_code, 201)

        User.objects.first()
        self.assertEqual(response.data['username'], 'user01')

    def test_regitster_user_existing_name(self):
        """User registration test when username already exists."""

        self.register_user()

        # username 'user01' already exists. Try to register another user with
        # the same name.

        response = self.register_user({
            'username': 'user01',
            'password': 'pass',
            'email': 'user02@test.com'
        })

        print(f'\n{response.data}')
        self.assertEqual(response.status_code, 400)

    def test_register_user_not_unique_email(self):
        """User registration test when email already exists."""

        self.register_user()

        # username 'user01@test.com' already exists. Try to register another
        # user with the same email.

        response = self.register_user({
            'username': 'user02',
            'password': 'pass',
            'email': 'user01@test.com'
            })

        print(f'\n{response.data}')

        self.assertEqual(response.status_code, 400)

    def test_login_user(self):
        """Ensure we can login user."""

        self.register_user()
        response = self.client.login(username='user01', password='pass')

        self.assertEqual(response, True)
