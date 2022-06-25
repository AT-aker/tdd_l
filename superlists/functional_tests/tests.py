from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


''' We have some user who need to input the value into check box
 and this value add to list 'To-Do'
 this user input "clean the floor"
 and he get "1: Clean the floor"
 user input second value "cooked dinner" and take two values in list.
 second "2: Cooked dinner" and his list stored in new Url - site messeged him about'''


class NewVisitorTest(LiveServerTestCase):
    """test new user"""

    def setUp(self) -> None:
        '''install'''
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        '''quit'''
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        """validating a row in a list table"""
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_reteieve_it_later(self):
        '''Test: we can start the list and give up this list later'''
        # evaluation of the application at
        #  the address of its website
        self.browser.get(self.live_server_url)

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
        # the page consist '1: clean the floor' in lists item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: clean the floor')

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1:clean the floor' for row in rows),
        #     f"New element not consist in table. The content was: \n{table.text}"
        # )
        self.assertIn('1: clean the floor', [row.text for row in rows])

        # browser proposes input next value 
        # user input "cooked dinner" 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('cooked dinner')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # the page refreshes and shows both items in its list
        self.check_for_row_in_list_table('1: clean the floor')
        self.check_for_row_in_list_table('2: cooked dinner')

        # list stored in new Url - site messeged him about

        
        self.fail('Test finally done!')
        
# if __name__ == '__main__':
#     unittest.main(warnings='ignore')
