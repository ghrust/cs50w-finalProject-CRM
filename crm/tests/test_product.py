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
        category = Category.objects.create(name='test_category')
        user = User.objects.create_user(**TEST_USER)
        self.client.login(**TEST_USER)
        Product.objects.create(
            name='test_product_1',
            price='99.99',
            category=category,
            owner=user
        )

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
        self.assertRedirects(response, reverse('product_detail', args=[2]))

    def test_product_detail_page(self):
        """Test can we retrieve product detail page."""
        url = reverse('product_detail', args=[1])
        response = self.client.get(url)
        logger.info(response.context_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['object'].name, 'test_product_1')
