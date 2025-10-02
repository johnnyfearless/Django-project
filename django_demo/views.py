# views.py

from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    the_return_data = {
        'home_last':"Testing"
        }
    
    return render(request, 'home.html', the_return_data)

def contact_page(request):
    return render(request, 'contact.html')

 