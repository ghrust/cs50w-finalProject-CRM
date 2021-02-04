from django.test import TestCase


class IndexPageTestCase(TestCase):
    """Test root URL."""
    def test_index_page_get(self):
        """Test get request for index page."""
        url = '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class RegisterPageTestCase(TestCase):
    """Test register page."""
    def test_register_page_get_request(self):
        """Test get request to Register Page."""
        url = '/register/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
