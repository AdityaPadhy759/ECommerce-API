from rest_framework import serializers
from .models import Cart, CartItem

#cart item serializer
class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only = True)
    price = serializers.FloatField(source = 'product-price', read_only = True)
    total = serializers.SerializerMethodField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'prodct_name', 'price', 'quantity', 'total']
        
        def get_total(self, obj):
            return obj.product.price * obj.quantity

#cart Serializer
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many = True, read_only = True)
    total_cart_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Cart
        fields = ['id','items','total_cart_price']
        
        def  get_total_cart_price(self, obj):
            return sum(item.product.price * item.quantity for item in obj.items.all())
            