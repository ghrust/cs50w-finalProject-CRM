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
        self.assertEqual(response.status_code, 200)

    def test_register_new_user(self):
        """Test registering new user."""
        url = reverse('signup')
        response = self.client.post(url, {
            'username': 'user',
            'password1': 'Word9876',
            'password2': 'Word9876'})
        logger.debug(response.content)
        logger.info(f'User created: {User.objects.first()}')
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(User.objects.all().count(), 1)
