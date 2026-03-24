from rest_framework import serializers
from .models import Order, OrderItem

#Order Item
class OrderItem(serializers.ModelSerializer):
    product_name = serializers.CharField(source = 'product.name', read_only = True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']
        
#Order
class Order(serializers.ModelSerializer):
    items = OrderItem(many = True, read_only = True)
    class Meta:
        model = Order
        fields = ['id', 'total_price', 'status', 'created_at', 'items']