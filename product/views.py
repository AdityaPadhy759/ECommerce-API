from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductListSerializer

# Create your views here.
class ProductListAPI(APIView):
    def get(self, request):
        prodcts = Product.objects.all()
        serializer = ProductListSerializer(prodcts, many=True)
        return Response(serializer.data)