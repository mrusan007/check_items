from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from shopping.forms import CheckOutForm
from shopping.models import Items

# Create your views here.
class ItemsListView(ListView):
    '''
    Listing all items.
    '''
    model = Items
    template_name = 'items.html'



class CheckOut(CreateView):
    '''
    Check out items, make an order.
    '''
    template_name = 'check_out.html'
    form_class = CheckOutForm
    success_url = 'index'