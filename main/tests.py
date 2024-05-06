from django.test import TestCase
from django.urls import reverse


class GetPagesTestCase(TestCase):
    def setUp(self):
        pass

    def test_main_page(self):
        path = reverse('main:index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass
