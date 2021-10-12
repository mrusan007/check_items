from django.shortcuts import render
from django.views.generic import ListView, CreateView
from shopping.forms import CheckOutForm
from shopping.models import Items, Promotions

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


    def get_context_data(self, **kwargs):

        context = super(CheckOut, self).get_context_data(**kwargs)
        all_promotions = Promotions.objects.all()

        promotions = {}

        for promotion in all_promotions:
            promotions[promotion.name] = str(promotion.can_combine)
        
        context['promotion'] = promotions

        return context



