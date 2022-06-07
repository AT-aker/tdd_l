from django.shortcuts import render



# Create your views here.
def home_page(request):
    '''Create home page in app views '''
    return render(request, 'home.html')