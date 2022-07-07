from re import I
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


''' Bill is the user who need to input the value into check box
 and this value add to list 'To-Do'
 this user input "clean the floor"
 and he get "1: Clean the floor"
 user input second value "cooked dinner" and take two values in list.
 second "2: Cooked dinner" and his list stored in new Url - site 
 messeged him about.
 And Ted second user who need other list with unique url and can`t
  read first Bill`s list  '''

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    """test new user"""


    def setUp(self) -> None:
        '''install'''
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        '''quit'''
        self.browser.quit()

    def wait_for_row_in_list_table(self,row_text):
        """wait a row in a list table"""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        '''Test: we can start the list for one user'''
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

        # Bill input 'clean the floor'
        inputbox.send_keys('clean the floor')

        # when Bill press Enter, the page is being refreshed, and
        # the page consist '1: clean the floor' in lists item
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: clean the floor')

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: clean the floor', [row.text for row in rows])

        # browser proposes input next value 
        # Bill input "cooked dinner" 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('cooked dinner')
        inputbox.send_keys(Keys.ENTER)

        # the page refreshes and shows both items in its list
        self.wait_for_row_in_list_table('1: clean the floor')
        self.wait_for_row_in_list_table('2: cooked dinner')


    def test_multiple_users_can_start_lists_at_different_urls(self):
        '''test: multiple users can start the lists at different urls'''
        # Bill create new list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('clean the floor')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: clean the floor')

        # Bill notices that his list has a unique URL 
        bill_list_url = self.browser.current_url
        self.assertRegex(bill_list_url, '/lists/.+')

        # New user Ted open go yo the site

        ## We use new session of browser, thus ensuring that no 
        ## information from Bill gets passed through cookie data
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Ted look at the page and can`t` see Bill`s list 
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('clean the floor', page_text)
        self.assertNotIn('cooked dinner', page_text)

        # Ted start new list, entry new element
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Ted get unique url with his list
        ted_list_url = self.browser.current_url
        self.assertRegex(ted_list_url, '/lists/.+')
        self.assertNotEqual(ted_list_url, bill_list_url)

        # check item from Bill`s list in Ted list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('clean the floor', page_text)
        self.assertIn('Buy milk', page_text)

    def test_layout_and_styling(self):
        '''test: layout and styling '''
        # Bill open home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # He notices that the input field is neatly centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # he create new list and see input field is neatly centered
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        self.assertAlmostEqual(
            inputbox.location["x"] + inputbox.size['width'] / 2,
            512,
            delta=10
        )