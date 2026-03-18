from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    
class LoginView(APIView):
    def post(self, request):
        Serializer = LoginSerializer(data = request.data)

        if Serializer.is_valid():
            return Response({"message":"Login Successful"}, status = status.HTTP_200_OK)
        
        return Response(Serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def  get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = ChangePasswordSerializer(data = request.data)
        
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.data.get('old_password')):
                return Response({"error" : "Old password is incorrect"},
                                status=status.HTTP_400_BAD_REQUEST
                                )
            if serializer.data.get('new_password') != serializer.data.get('confirm_password'):
                return Response({"error":"Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
            user.save()
            return Response({"message" : "Password changed successfully"},
                        status=status.HTTP_200_OK
                        )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token) 
            token.blacklist()
            return Response({"message" : "Logout successful"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"error":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)