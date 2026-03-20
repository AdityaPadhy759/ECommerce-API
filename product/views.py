from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from rest_framework import generics
from .serializers import ProductListSerializer

# Create your views here.
# ProductList API
class ProductListAPI(APIView):
    def get(self, request):
        prodcts = Product.objects.all()
        serializer = ProductListSerializer(prodcts, many=True)
        return Response(serializer.data)
    
# ProductDetails API
class ProductDetailsAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'id'