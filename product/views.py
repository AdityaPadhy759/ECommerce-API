from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category
from rest_framework import generics
from .serializers import ProductListSerializer, ProductCategorySerializer

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
    
# ProductCategory API
class ProductCategoryAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductCategorySerializer