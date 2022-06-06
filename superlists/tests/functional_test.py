from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

''' We have some user who need to input the value into check box
 and this value add to list 'To-Do'
 this user input "clean the floor"
 and he get "1. Clean the floor"
 user input second value and take two values in list
 and his list stored in new Url - site messeged him about'''


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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # page prompt insert value into the list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # user input 'clean the floor'
        inputbox.send_keys('clean the floor')

        # when user press Enter, the page is being refreshed, and
        # the page consist '1: Clean the floor' in lists item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1.Clean the floor' for row in rows)
        )
        self.fail('Test finally done!')
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
