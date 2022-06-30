from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    '''Create home page in app views '''
    return render(request, 'home.html')

def view_list(request, list_id):
    '''view list'''
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    '''create new list'''
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    '''add new item'''
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')