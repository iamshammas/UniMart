from django.db import models
from django.contrib.auth.models import User
from Cart.models import Product
from Authentication.models import Profile
# Create your models here.

class Order(models.Model):
    STATUS = [
        ('pending','Pending'),
        ('success','Success'),
        ('cancelled','Cancelled'),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_amount = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=50,choices=STATUS,default='pending')
    order_status = models.CharField(max_length=50,choices=STATUS,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    @property
    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product.name