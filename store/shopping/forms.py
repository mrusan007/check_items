from django import forms
from django.db.models.fields import CharField
from shopping.models import Order

class CheckOutForm(forms.ModelForm):

    promotions = forms.CharField(max_length=256, label='Promotions:')
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form', 'aria-describedby':"emailHelp",}))
    address = forms.CharField(max_length=256, label='Home Adress:')
    card_number = forms.CharField(max_length=25, label='Credit card number:')
    cve = forms.CharField(max_length=5, label='CVE:')

    class Meta:
        model = Order
        exclude = ('item_quantity', 'promotions')
