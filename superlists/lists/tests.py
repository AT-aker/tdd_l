from django.test import TestCase

from lists.views import home_page


class HomePageTest(TestCase):
    '''Home page test'''

    def test_uses_home_template(self):
        '''test: uses home template or not'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
