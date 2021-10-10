from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from shopping.models import Items

# Create your views here.
class ItemsListView(ListView):
    '''
    Listing all items.
    '''
    model = Items
    template_name = 'items.html'



class CheckOut(TemplateView):
    '''
    Check out items, make an order.
    '''
    template_name = 'check_out.html'