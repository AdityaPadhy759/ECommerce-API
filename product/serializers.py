from rest_framework import serializers
from .models import Product, ProductImage, Category, ProductImage

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
#Category

class ProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price']
        
class ProductCategorySerializer(serializers.ModelSerializer):
    products = ProductSimpleSerializer(many = True, read_only = True)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'products']      
        
#Product Image

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        field = ['id', 'image']
        
#Product Stock

class ProductStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = ['id', 'name', 'stock']