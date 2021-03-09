"""crm/tests/test_order.py
Tests for product feature."""
from django.test import TestCase
from django.urls import reverse

from loguru import logger

from crm.models import Category, Order, Product, User
from crm.tests import TEST_USER, TEST_CUSTOMER


class OrderTestCase(TestCase):
    """Test order feature."""
    def setUp(self):
        user = User.objects.create_user(**TEST_USER)
        Customer.objects.create(**TEST_CUSTOMER)
        category = Category.objects.create(name='Test_category')
        Product.objects.create(name='Test_product', category=category,
                               price='18,99', owner=user)

    def test_order_create(self):
        """Test can we create order programmatically."""
        order = Order.objects.create(
            customer=Customer.objects.first(),
            vendor=User.objects.first(),
            product=Product.objects.first(),
            payed_price='18,99',
        )
        logger.info(order)
        self.assertEqual(Order.objects.all().count(), 1)
