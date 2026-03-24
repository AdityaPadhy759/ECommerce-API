from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.
class Order(models.Model):
    STATUS_CHOICE = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered',' Delivered'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()
    status = models.CharField(max_length = 10, choices=STATUS_CHOICE, default = 'pending')
    created_at = models.DateTimeField(auto_now_add = True)
    
    def  __str__(self):
        return f"order {self.id} - {self.user.username}"
    
#OrdersItem Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name= 'items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
        
        