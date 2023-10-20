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
        ordering            = ["id"]
    
    def __str__(self):
        return self.title
    
    def manage_stock(self,quantity):
        '''WHEN ORDERING WE REDUCE IT FROM THE STOCK'''
        new_stock  = self.stock - int(quantity)
        self.stock = new_stock
        self.save()
    
    def check_stock(self,quantity):
        if int(quantity) > self.stock:
            return False
        return True
    
    def place_order(self,user,quantity):
        ''' place order with item , its quantity and associated user'''
        ## remember item is a foreign key
        ## so item has the method assoiciated 
        ## with this 
        if self.check_stock(quantity):
            order = Order.objects.create(
                item = self,
                quantity = quantity,
                user = user
            )
            self.manage_stock(quantity)
            return order
        else:
            return None
    

class Order(TimeStampedModel,ActivatorModel,Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    user     = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    item     = models.ForeignKey(Item,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=0)

    