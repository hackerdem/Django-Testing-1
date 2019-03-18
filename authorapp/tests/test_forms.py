from django.test import Client
from unittest import TestCase
from django.test import SimpleTestCase
from authorapp.views import CreateSuccessView

sample_image = '/home/erdem/Downloads/icon-2488093_1280.png'
image = open(sample_image,'rb')

sample_data = {
                'first_name':'John',
                'last_name':'Cash',
                'email':'john@cash.com',
                'photo':image,   
            }
wrong_file = '/home/erdem/Videos/from 21-12-18 18:44:23.webm'
wrong_image = open(wrong_file,'rb')
wrong_file_data = {
                'first_name':'Janis',
                'last_name':'Joplin',
                'email':'janis@joplin.com',
                'photo':wrong_image,   
            }

class AuthorFormTests(TestCase):
    def setUp(self):
        self.client = Client()
    def test_post_author_create_form(self):
        response = self.client.post('/author/create', sample_data)
        self.assertEqual(response.status_code,200)

    def test_author_create_success_redirect(self):
        response = self.client.post('/author/create',sample_data, follow=True)
        self.assertEqual(response.resolver_match.func.__name__, CreateSuccessView.as_view().__name__)

class AutorFormDataTests(SimpleTestCase):
    def setUp(self):
        self.new_client = Client()

    def test_photo_wrong_file_type(self):
        self.new_client = Client(enforce_csrf_checks=True)
        response = self.client.post('/author/create', wrong_file_data)

        self.assertFormError(response,'form','photo','Upload a valid image. The file you uploaded was either not an image or a corrupted image.')

    def test_empty_post_data(self):
            response = self.new_client.post('/author/create', {})
            self.assertFormError(response,'form','first_name','This field is required.')
    