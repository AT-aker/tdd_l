from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    '''Create home page in app views '''
    return render(request, 'home.html')

def view_list(request):
    '''view list'''
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    '''new list'''
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/only-world-list-ever/')