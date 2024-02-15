from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role','is_superuser', 'is_staff', 'password']
       
        extra_kwargs = {
            'password': {'write_only' :True}
        }
        
    def create(self, validated_data):
        user = CustomUser(
            email= validated_data['email'],
            username = validated_data['username'],
            role = validated_data['role'],
            is_superuser= validated_data['is_superuser'],
            is_staff = validated_data['is_staff']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
