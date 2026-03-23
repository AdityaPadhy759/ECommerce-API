from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category, ProductImage
from rest_framework import generics
from .serializers import ProductListSerializer, ProductCategorySerializer, ProductImageSerializer, ProductStockSerializer
from rest_framework.filters import SearchFilter

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
    
#ProductImage API
class ProductImageAPI(generics.ListAPIView):
    specializer_class = ProductImageSerializer
    
    def get_queryset(self):
        product_id = self.kwargs['id']
        return ProductImage.objects.filter(product_id = product_id)
    
# ProductStock API
class ProductStockAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductStockSerializer.lookup_field = 'id'
    
#Search & Filter
class ProductListAPI(generics.ListAPIView):
    serializer_class = ProductListSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
    
        #search
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(name__icontains = search)
        
        #filter by category
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name__icontains=category)
        
        #filter by price
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        
        if min_price:
            queryset = queryset.filter(price__gte = min_price)
        
        if max_price:
            queryset = queryset.filter(price__lte = max_price)
            
            return queryset
        
        