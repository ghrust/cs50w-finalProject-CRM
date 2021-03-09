"""crm/tests/test_category.py
Tests for product feature."""
from django.test import TestCase
from django.urls import reverse

from loguru import logger

from crm.models import Category


class CategoryTestCase(TestCase):
    """Test for product category."""
    def test_category_model(self):
        """Test can we create category."""
        category = Category.objects.create(name='test_category')
        logger.info(category)
        self.assertEqual(Category.objects.all().count(), 1)
