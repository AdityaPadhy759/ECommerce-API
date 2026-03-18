from rest_framework import serializers
from django.contrib.auth import get_user_model 
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', ]
        extra_kwargs = {'password' : {'write_only' : True}}
    
    def validate(self, data):
        if data['password'] !=  data['confirm_password']:
            raise serializers.ValidationError("Password do not match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])         
        return user    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    
    def validate(self, data):
        user = authenticate(
            username = data['username'],
            password = data['password']
        )
        
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        
        data['user'] = user
        return data

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ChangePasswordSerializer(serializers.Serializer):
    
    old_password = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True)
    confirm_password = serializers.CharField(required = True)
    
    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("New passwords do not match")
        return data

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

