from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem
from product.models import Product
from .serializers import CartSerializer

# Create your views here.
# Add to Cart
def get_user_cart(user):
    cart, created = Cart.objects.get_or_create(user = user)
    return cart

class AddToCart(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        
        #get product
        try:
            product = Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            return Response({"error":"Product not found"}, status = 404)
        
        #get user cart
        cart = get_user_cart(request.user)
        
        #check if product is available or not
        cart_item, created = CartItem.objects.get_or_create(cart = cart, product = product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
            
        cart_item.save()
        return Response({",essage":"Product added to cart"}, status=200)
    
#ViewCart
class ViewCart(APIView):
    def get(self, request):
        cart = get_user_cart(request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

#Delete / Remove
class RemoveFromCart(APIView):
    def delete(self, request, pk):
        cart = get_user_cart(request.user)
        
        try:
            item = CartItem.objects.get(id = pk, cart = cart)
        except CartItem.DoesNotExist:
            return Response({"error" : "Item not found"}, status=404)
        item.delete()
        return Response({"message":"Item removed successfully"}, status=200)

#Update Cart
class UpdateCart(APIView):
    def patch(self, request, pk):
        cart = get_user_cart(request.user)
        
        try:
            item = CartItem.objects.get(id = pk, cart = cart)
        except CartItem.DoesNotExist:
            return Response({"error":"Item not found"}, status=404)
        
        quantity = int(request.data.get('quantity', 1))
        
        if quantity <= 0:
            item.delete()
            return Response({"message":"Item removed because quantity is 0"})
        
        item.quantity = quantity
        item.save()
        
        return Response({"message":"Cart updated successfully"})
        