"""accounts/tests.py
   Accounts app tests.
"""
from django.test import TestCase
from django.urls import reverse
from loguru import logger

from accounts.models import User


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
        self.assertRedirects(response, reverse('index'))
