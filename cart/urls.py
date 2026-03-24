from django.urls import path, include
from .views import AddToCart, ViewCart, RemoveFromCart, UpdateCart
urlpatterns = [
    path('cart/add/', AddToCart.as_view()),
    path('cart/', ViewCart.as_view),
    path('cart/remove/<int:pk>/', RemoveFromCart.as_view()),
    path('cart/update/<int:pk>/', UpdateCart.as_view()),
]
