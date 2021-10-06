from django.shortcuts import render
from django.views.generic import ListView
from shopping.models import Items

# Create your views here.
class ItemsListView(ListView):
    '''
    Listing all items.
    '''
    model = Items
    template_name = 'items.html'