from django.db import models

# Create your models here.
class Items(models.Model):
    '''
    Items for our store.
    '''
    name = models.CharField(max_length=256, null=False)
    price = models.FloatField(null=False)

class Promotions(models.Model):
    '''
    Promotions for our store.
    '''
    name = models.CharField(max_length=256, null=False)

class ItemsQuantity(models.Model):
    '''
    How many of items per order.
    '''
    quantity = models.IntegerField(null=False)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)

class Order(models.Model):
    '''
    Order from our customer.
    '''
    item_quantity = models.ManyToManyField(ItemsQuantity)
    promotions = models.ManyToManyField(Promotions)