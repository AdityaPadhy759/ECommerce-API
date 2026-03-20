from django.urls import path
from .views import ProductListAPI,ProductDetailsAPI

urlpatterns = [
    path('products/', ProductListAPI.as_view()),
    path('products/<int:id>/', ProductDetailsAPI.as_view(), name='product-detail'),
]
