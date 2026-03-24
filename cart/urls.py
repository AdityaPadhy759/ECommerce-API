from django.urls import path, include
from .views import AddToCart, ViewCart
urlpatterns = [
    path('cart/add/', AddToCart.as_view()),
    path('cart/', ViewCart.as_view),
]
