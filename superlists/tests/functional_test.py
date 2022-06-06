from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """test new user"""

    def setUp(self) -> None:
        '''install'''
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        '''quit'''
        self.browser.quit()

    def test_can_start_a_list_and_reteieve_it_later(self):
        '''Test: we can start the list and give up this list later'''
        # evaluation of the application at
        #  the address of its website
        self.browser.get('http://localhost:8000')

        # Check 'to-do' in title main page 
        self.assertIn('To-Do', self.browser.title)
        self.fail('End the Test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')


# We have some user who need to input the value into check box
# and this value add to list 'To-Do'
# this user input "clean the floor"
# and he get "1. Clean the floor"
# user input second value and take two values in list
# and his list stored in new Url - site messeged him about 
