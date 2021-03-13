"""crm/tests.py
CRM App tests.
"""
from django.test import TestCase
from django.urls import reverse

from loguru import logger

from accounts.models import User
from crm.models import Customer, Category, Product, Order


TEST_USER = {
    'username': 'test_user',
    'password': 'Word9876',
}

TEST_CUSTOMER = {
    'first_name': 'Cust',
    'last_name': 'Test',
    'phone': 1234567890,
    'email': 'test_cust@test.com',
}


class IndexPageTestCase(TestCase):
    """Test root URL."""
    def setUp(self):
        User.objects.create_user(**TEST_USER)

    def test_index_page_get(self):
        """Test get request for index page."""
        self.client.login(**TEST_USER)
        url = reverse('dashboard')
        response = self.client.get(url)
        logger.info(response)
        self.assertEqual(response.status_code, 200)
