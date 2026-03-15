from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import RegisterSerializer
from .serializers import LoginSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    
class LoginView(APIView):
    def post(self, request):
        Serializer = LoginSerializer(data = request.data)

        if Serializer.is_valid():
            return Response({"message":"Login Successful"}, status = status.HTTP_200_OK)
        
        return Response(Serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
