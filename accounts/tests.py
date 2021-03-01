"""accounts/tests.py
   Accounts app tests.
"""
from django.test import TestCase
from django.urls import reverse
from loguru import logger

from accounts.models import User


TEST_USER = {
    'username': 'test_user',
    'password': 'Word9876',
}


class RegisterPageTestCase(TestCase):
    """Test register page."""
    def test_register_page_get_request(self):
        """Test get request to Register Page."""
        url = reverse('signup')
        response = self.client.get(url)
        logger.info(response)
        self.assertEqual(response.status_code, 200)

    def test_register_new_user(self):
        """Test registering new user."""
        url = reverse('signup')
        response = self.client.post(url, {
            'username': 'user',
            'password1': 'Word9876',
            'password2': 'Word9876'})
        logger.info(response)
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(User.objects.all().count(), 1)


class LoginPageTestCase(TestCase):
    """Test login page."""
    def test_login_page_get_request(self):
        """Test get request for Login Page."""
        url = reverse('login')
        response = self.client.get(url)
        logger.info(response)
        self.assertEqual(response.status_code, 200)

    def test_login_user(self):
        """Test we can login user."""
        user = User.objects.create_user(username='user', password='Word9876')
        url = reverse('login')
        response = self.client.post(url, {'username': 'user', 'password': 'Word9876'})
        logger.info(response)
        self.assertRedirects(response, reverse('dashboard'))


class UserDetailPageTestCase(TestCase):
    """Test user detail (profile) page."""
    def setUp(self):
        User.objects.create_user(username='test_user', password='Word9876')

    def test_user_detail_page_get(self):
        """Test get request for user detail page."""
        url = reverse('user-detail')
        self.client.login(username='test_user', password='Word9876')
        response = self.client.get(url)
        logger.info(response)
        self.assertEqual(response.status_code, 200)


class UserUpdateDeleteTestCase(TestCase):
    """Test user update page and user delete page."""
    def setUp(self):
        User.objects.create_user(**TEST_USER)

    def test_update_user_profile(self):
        """Test can we update user info."""
        self.client.login(**TEST_USER)
        url = reverse('user-update')
        new_name = 'Test_edit'
        response = self.client.post(
            url, {**TEST_USER, **{'username': new_name}})
        logger.info(response)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.first().username, new_name)
