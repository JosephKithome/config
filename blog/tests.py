from django.contrib import auth
from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your tests here.

class PostTestCase(TestCase):

    def setUp(self):
        self.user =get_user_model().objects.create_user(
            username='joseph',
            email='joseph@gmail.com',
            password='password1'
        )
        self.post =Post.objects.create(
            title='A good title',
            body='Nice body content',
            author = self.user
        )

    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post),post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','A good title')
        self.assertEqual(f'{self.post.body}','Nice body content')
        self.assertEqual(f'{self.post.author}','joseph')    

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))   
        self.assertEqual(response.status_code,200) 
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')


    def test_post_list_template_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'home.html')

    # def test_post_detail_template_view(self):
    #     response = self.client.post(reverse('post'))  
    #     self.assertEqual(response.status_code,200)
    #     self.assertTemplateUsed(response, 'post_detail.html')
                
    def test_post_create_view(self): # new
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New title')
        self.assertEqual(Post.objects.last().body, 'New text')

    def test_post_update_view(self):
        response = self.client.get(reverse('edit', args='1'),{
            'title': 'updated title',
            'body': 'updated body'
        })
        self.assertEqual(response.status_code, 302)    

    def test_delete_view(self):
        response = self.client.delete(reverse('delete', args='1'),{

        })  
        self.assertEqual(response.status_code,302)  
