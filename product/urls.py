from django.urls import path
from .views import ProductListAPI,ProductDetailsAPI, ProductCategorySerializer, ProductImageAPI

urlpatterns = [
    path('products/', ProductListAPI.as_view()),
    path('products/<int:id>/', ProductDetailsAPI.as_view(), name='product-detail'),
    path('categories/', ProductDetailsAPI.as_view(), name = 'categpry-list'),
    path('products/<int:id>/images/', ProductImageAPI.as_view(), name = 'product-image'),
]
