"""Accounts app tests."""
from django.test import TestCase
from django.urls import reverse


class RegisterPageTestCase(TestCase):
    """Test register page."""
    def test_register_page_get_request(self):
        """Test get request to Register Page."""
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
