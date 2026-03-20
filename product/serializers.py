from rest_framework import serializers
from .models import Product, ProductImage

# Product List
class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source = "category.name")
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category']

#Product Image Details
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

#Product Detail
class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source = 'category.name')
    images = ProductImageSerializer(many = True, read_only = True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'stock',
            'category',
            'images',
            'created_at',
        ]

        