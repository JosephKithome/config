from django.http import response
from django.test import TestCase,SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_homepage(self):
        response =self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):    
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)
