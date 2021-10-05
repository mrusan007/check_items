from django.db import models

# Create your models here.
class Items(models):
    '''
    Items for our store.
    '''
    name = models.CharField(max_length=256, null=False)
    price = models.FloatField(null=False)