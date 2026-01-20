from django.db import models
from django.contrib.auth.models import User
from Product.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT,related_name='carts')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_amount(self):
        less = [x.total for x in self.cartitem_set.all()]
        print(less)
        print('HELOOOOOOOOOO')
        return sum(x.total for x in self.cartitem_set.all())

    def __str__(self):
        return self.user.username

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL,related_name='cart_items')
    quantity = models.PositiveIntegerField()
    
    @property
    def total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name