"""crm/tests.py
CRM App tests.
"""
from django.test import TestCase
from django.shortcuts import reverse

from loguru import logger


class IndexPageTestCase(TestCase):
    """Test root URL."""
    def test_index_page_get(self):
        """Test get request for index page."""
        url = reverse('dashboard')
        response = self.client.get(url)
        logger.info(response.content)
        self.assertEqual(response.status_code, 200)
