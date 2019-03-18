from django.test import Client
from unittest import TestCase
from django.test import SimpleTestCase


class AuthorCreateViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_author_create_view(self):
        response = self.client.get('/author/create')
        self.assertEqual(response.status_code,200)

    def test_get_success_view(self):
        response = self.client.get('/author/success')
        self.assertEqual(response.status_code,200)
