from rest_framework import serializers
from .models import Product

class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source = "category.name")
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category']