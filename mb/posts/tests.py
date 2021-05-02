from django.test import TestCase,SimpleTestCase
from .models import Post
from django.urls import  reverse
# Create your tests here.

class HomePageTestCase(SimpleTestCase):
    def home_page_test(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

class PostModelTestCase(TestCase):
    def setUp(self):
        Post.objects.create(text ="Just testing")
       

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'  
        self.assertEqual(expected_object_name,'Just testing')   

class HomePageViewTestCase(TestCase):
    def setUp(self):
        Post.objects.create(text ="Another testing") 

    def test_view_url_exitsts_at_proper_location(self): 
        response = self.client.get('/') 
        self.assertEqual(response.status_code,200)

    def test_url_view_by_name(self):
        resp = self.client.get(reverse('home'))   
        self.assertEqual(resp.status_code,200)    

    def test_view_uses_correct_template(self):  
        resp = self.client.get(reverse('home'))   
        self.assertEqual(resp.status_code,200) 
        self.assertTemplateUsed(resp,'home.html')     

    

