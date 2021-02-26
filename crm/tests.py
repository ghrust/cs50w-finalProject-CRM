"""crm/tests.py
CRM App tests.
"""
from django.test import TestCase
from django.urls import reverse

from loguru import logger

from .models import Customer, User


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
    def test_index_page_get(self):
        """Test get request for index page."""
        url = reverse('dashboard')
        response = self.client.get(url)
        logger.info(response)
        self.assertEqual(response.status_code, 200)


class CustomerTestCase(TestCase):
    """Test Customer page"""
    def setUp(self):
        test_user = User.objects.create_user(**TEST_USER)
        Customer.objects.create(
            first_name='Customer',
            last_name='Test',
            phone=1234567890,
            vendor=test_user)

    def test_customer_profile_page_get(self):
        """Test get request for customer profile page."""
        url = reverse('customer-detail', args=[Customer.objects.first().id])
        response = self.client.get(url)
        logger.info(response.context['object'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], Customer.objects.first())

    def test_add_new_customer_get(self):
        """Test can we load page with customer form."""
        self.client.login(**TEST_USER)
        url = reverse('customer-form')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_new_customer_post(self):
        """Test can we add new customer."""
        self.client.login(**TEST_USER)
        url = reverse('customer-form')
        response = self.client.post(url, TEST_CUSTOMER, follow=True)
        customer = Customer.objects.last()
        logger.info(f'\nCustomer created: {customer}\nVendor: {customer.vendor}')
        self.assertEqual(response.status_code, 200)

    def test_customer_list_page(self):
        """Test customer list page."""
        self.client.login(**TEST_USER)
        url = reverse('customer-list')
        response = self.client.get(url)
        logger.info(response)
        self.assertEqual(response.status_code, 200)

    def test_customer_update(self):
        """Test can we update customer's data."""
        self.client.login(**TEST_USER)
        url = reverse('customer-update', args=[Customer.objects.first().id])
        response = self.client.post(
            url, {**TEST_CUSTOMER, **{'first_name': 'Edited'}})
        logger.info(response)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Customer.objects.first().first_name, 'Edited')
