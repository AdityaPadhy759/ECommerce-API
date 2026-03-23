from django.urls import path, include
from .views import AddToCart
urlpatterns = [
    path('cart/add/', AddToCart.as_view())
]
