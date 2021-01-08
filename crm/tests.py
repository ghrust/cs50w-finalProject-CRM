"""Tests for crm app."""

from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse

from . import views
from .models import User


DEFAULT_USER_DATA = {
        'username': 'user01',
        'email': 'user01@test.com',
        'password': 'pass',
        'first_name': 'user',
        'last_name': '01',
    }


def register_user(data=DEFAULT_USER_DATA):
    """Register new test user."""

    url = reverse(views.CreateUserApi.name)

    client = APIClient()
    response = client.post(url, data, format='json')

    return response


class RegisterUserTestCase(APITestCase):
    """Test register API."""

    def test_register_user(self):
        """Ensure we can register new user."""

        response = register_user()

        self.assertEqual(response.status_code, 201)

        User.objects.first()
        self.assertEqual(response.data['username'], 'user01')

    def test_regitster_user_existing_name(self):
        """User registration test when username already exists."""

        register_user()

        # username 'user01' already exists. Try to register another user with
        # the same name.

        response = register_user({
            'username': 'user01',
            'password': 'pass',
            'email': 'user02@test.com'
        })

        print(f'\n{response.data}')
        self.assertEqual(response.status_code, 400)

    def test_register_user_not_unique_email(self):
        """User registration test when email already exists."""

        register_user()

        # username 'user01@test.com' already exists. Try to register another
        # user with the same email.

        response = register_user({
            'username': 'user02',
            'password': 'pass',
            'email': 'user01@test.com'
            })

        print(f'\n{response.data}')

        self.assertEqual(response.status_code, 400)

    def test_login_user(self):
        """Ensure we can login user."""

        register_user()
        response = self.client.login(username='user01', password='pass')

        self.assertEqual(response, True)


class UserDetailAPITestCase(APITestCase):
    """Test UserDetailAPI."""

    def setup(self):
        """Test setup."""
        register_user()

    def test_user_detail_get_unauthenticated(self):
        """Test unauthenticated get request for user detail API."""

        url = reverse(views.UserDetailAPI.name)

        response = self.client.get(url)
        print(f'\n{response.data}')

        self.assertEqual(response.status_code, 401)
