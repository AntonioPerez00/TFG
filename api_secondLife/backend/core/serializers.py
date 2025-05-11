from rest_framework import serializers
from .models import User
from .models import Product

class UserRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'mail', 'password', 'location', 'profile_pic', 'profile_desc']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'