"""crm/tests.py
CRM App tests.
"""
from django.test import TestCase
from django.shortcuts import reverse

from loguru import logger

from .models import Customer


class IndexPageTestCase(TestCase):
    """Test root URL."""
    def test_index_page_get(self):
        """Test get request for index page."""
        url = reverse('dashboard')
        response = self.client.get(url)
        logger.info(response)
        self.assertEqual(response.status_code, 200)


class CustomerTestCase(TestCase):
    """Test Customer page"""
    def setUp(self):
        Customer.objects.create(
            first_name='Customer',
            last_name='Test',
            phone=1234567890)

    def test_customer_profile_page_get(self):
        """Test get request for customer profile page."""
        url = reverse('customer-detail', args=[Customer.objects.first().id])
        response = self.client.get(url)
        logger.info(response.context['object'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], Customer.objects.first())
