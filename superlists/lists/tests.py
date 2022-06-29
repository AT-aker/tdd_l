from urllib import response
from lists.models import Item, List
from django.test import TestCase

from lists.views import home_page


class HomePageTest(TestCase):
    '''Home page test'''

    def test_uses_home_template(self):
        '''test: uses home template or not'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ListAndItemModelsTest(TestCase):
    '''testing model element of list'''

    def test_saving_and_retrieving_items(self):
        '''test to store and retrieve list items '''
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)


class ListViewTest(TestCase):
    '''Test list view'''

    def test_uses_list_template(self):
        '''test: uses list template'''
        response = self.client.get('/lists/only-world-list-ever/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        '''test: views all elements of list'''
        list_ = List.objects.create()
        Item.objects.create(text='itemey 1', list=list_)
        Item.objects.create(text='itemey 2', list=list_)

        response = self.client.get('/lists/only-world-list-ever/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):
    '''test new list'''

    def test_can_save_a_POST_request(self):
        '''Test: can save post request'''
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        '''test: redirect after post request'''
        response = self.client.post(
            '/lists/new', data={'item_text': 'A new list item'}
            )

        self.assertRedirects(response, '/lists/only-world-list-ever/')
