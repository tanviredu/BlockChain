from django.db                   import models
from django.contrib.auth.models  import User
from utils.model_abstracts       import Model
from django_extensions.db.models import (
    TimeStampedModel,ActivatorModel,TitleDescriptionModel
)

class Item(TimeStampedModel,ActivatorModel,TitleDescriptionModel,Model):
    stock = models.IntegerField(default=1)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name        = 'Item'
        verbose_name_plural = 'Items'
    
    def __str__(self):
        return self.title
    
    def manage_order(self,quantity):
        '''WHEN ORDERING WE REDUCE IT FROM THE STOCK'''
        new_stock  = self.stock - int(quantity)
        self.stock = new_stock
        self.save()
    
    def check_stock(self,quantity):
        if int(quantity) > self.stock:
            return False
        return True
    

class Order(TimeStampedModel,ActivatorModel,Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    user     = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    item     = models.ForeignKey(Item,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=0)
