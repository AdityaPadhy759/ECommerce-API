from django.urls import path
from .views import ProductListAPI,ProductDetailsAPI, ProductCategorySerializer

urlpatterns = [
    path('products/', ProductListAPI.as_view()),
    path('products/<int:id>/', ProductDetailsAPI.as_view(), name='product-detail'),
    path('categories/', ProductDetailsAPI.as_view(), name = 'categpry-list'),
]
