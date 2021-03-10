"""crm/tests/test_product.py
Tests for product feature."""
from django.test import TestCase
from django.urls import reverse

from loguru import logger

from crm.models import Category, Product, User
from crm.tests import TEST_USER


class ProductTestCase(TestCase):
    """Test for product."""
    def setUp(self):
        Category.objects.create(name='test_category')
        User.objects.create_user(**TEST_USER)
        self.client.login(**TEST_USER)

    def test_product_model(self):
        """Test can we add product."""
        product = Product.objects.create(
            name='Test_product',
            price='99.99',
            owner=User.objects.first(),
            category=Category.objects.first()
        )
        logger.info(product)
        self.assertEqual(Category.objects.all().count(), 1)

    def test_post_request_to_product_create_page(self):
        """Test product create page."""
        url = reverse('product_create')
        response = self.client.post(url, {
            'name': 'test_product',
            'category': Category.objects.first().id,
            'price': '18.99',
        })
        logger.info(response.content)
        # TODO: change to reverse('product_detail')
        self.assertRedirects(response, reverse('dashboard'))
