from django.test import TestCase
from authorapp.models import Author
import os

class AuthorModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Adam',
                              last_name='Fisher',
                              email='adam@gmail.com',
                              photo='/home/erdem/Desktop/blog/apptest/testproject/photos/placeholder-profile.jpg')
    
    def test_return_value(self):
        author = Author.objects.get(id=1)
        expected_return_value = '{} {}'.format(author.first_name, author.last_name)
        self.assertEquals(expected_return_value, str(author))

    def test_author_photo(self):
        author = Author.objects.get(id=1)
        self.assertIsNotNone(author.photo)

    def test_author_photo_size(self):
        author = Author.objects.get(id=1)
        photo_size = os.path.getsize(author.photo.path)
        self.assertLessEqual(photo_size,5242880)