from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):
    '''tjxic test'''

    def test_bad_maths(self):
        '''wrong maths method'''
        self.assertEqual(1 + 1, 3)
        
