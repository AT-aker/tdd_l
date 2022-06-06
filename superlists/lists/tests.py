from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):
    '''Home page test'''

    def test_root_url_resolves_to_home_page_view(self):
        '''test:root url converted to home page url'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

