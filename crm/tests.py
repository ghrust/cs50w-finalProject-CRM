"""Tests for crm app."""

from loguru import logger

from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status

from . import views
from .models import User, Company

TEST_USER_DATA = {
        'username': 'user01',
        'email': 'user01@test.com',
        'password': 'pass',
        'first_name': 'user',
        'last_name': '01',
    }
TEST_COMPANY_DATA = {
    'name': 'company01'
}


def register_user(data=TEST_USER_DATA):
    """Register new test user."""

    url = reverse(views.CreateUserApi.name)

    client = APIClient()
    response = client.post(url, data, format='json')
    user = User.objects.get(username=TEST_USER_DATA['username'])

    return response


class RegisterUserTestCase(APITestCase):
    """Test register API."""

    def test_register_user(self):
        """Ensure we can register new user."""

        response = register_user()

        self.assertEqual(response.status_code, 201)

        User.objects.first()
        self.assertEqual(response.data['username'], 'user01')

    def test_register_user_existing_name(self):
        """User registration test when username already exists."""

        register_user()

        # username 'user01' already exists. Try to register another user with
        # the same name.

        response = register_user({
            'username': 'user01',
            'password': 'pass',
            'email': 'user02@test.com'
        })

        logger.info(f'\n{response.data}')
        self.assertEqual(response.status_code, 400)

    def test_register_user_not_unique_email(self):
        """User registration test when email already exists."""

        register_user()

        # Username 'user01@test.com' already exists.
        # Try to register another user with the same email.

        response = register_user({
            'username': 'user02',
            'password': 'pass',
            'email': 'user01@test.com'
            })

        logger.info(f'\n{response.data}')

        self.assertEqual(response.status_code, 400)

    def test_login_user(self):
        """Ensure we can login user."""

        register_user()
        response = self.client.login(username='user01', password='pass')

        self.assertEqual(response, True)


class UserDetailAPITestCase(APITestCase):
    """Test UserDetailAPI."""

    def setUp(self):
        """Test setup."""
        register_user()

    def test_user_detail_get_unauthenticated(self):
        """Test unauthenticated get request for user detail API."""

        url = reverse(views.UserDetailAPI.name)

        response = self.client.get(url)
        logger.info(f'\n{response.data}')

        self.assertEqual(response.status_code, 401)

    def test_user_detail_get_authenticated(self):
        """Test authenticated get request for user detail API."""

        url = reverse(views.UserDetailAPI.name)

        self.client.login(username=TEST_USER_DATA['username'],
                          password=TEST_USER_DATA['password'])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class CompanyAPITestCase(APITestCase):
    """Test company API."""
    # TODO: refactor user login
    def setUp(self):
        register_user()
        self.client.login(username=TEST_USER_DATA['username'],
                          password=TEST_USER_DATA['password'])
        user01 = User.objects.get(username=TEST_USER_DATA['username'])
        user02 = User.objects.create_user(username='user02', password='pass',
                                          email='user02f@test.com')
        Company.objects.create(name='company01', owner=user01)
        Company.objects.create(name='company02', owner=user01)
        Company.objects.create(name='company03', owner=user02)

    def test_get_company_list_unauthorized(self):
        """Test unauthorized get request for company API."""
        url = reverse('company-list')
        self.client.logout()
        response = self.client.get(url)
        logger.info(response.data)
        self.assertEqual(response.status_code, 401)

    def test_get_company_list_authorized(self):
        """Test authorized get request for company API."""
        url = reverse('company-list')
        user01 = User.objects.get(username=TEST_USER_DATA['username'])

        response = self.client.get(url)

        logger.info(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), user01.companies.all().count())

    def test_create_new_company(self):
        """Test creating new company."""
        url = reverse('company-list')
        response = self.client.post(url, data=TEST_COMPANY_DATA)

        logger.info(response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_company(self):
        """Test get company."""
        url = reverse('company-detail', args=[1])
        response = self.client.get(url)
        logger.info(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], TEST_COMPANY_DATA['name'])

    def test_update_company(self):
        """Test update company data."""
        url = reverse('company-detail', args=[1])
        new_name = 'NewName'
        data = {'name': new_name}
        response = self.client.patch(url, data=data)
        logger.info(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], new_name)

    def test_delete_company(self):
        """Test delete company."""
        url = reverse('company-detail', args=[1])
        response = self.client.delete(url)
        logger.info(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)