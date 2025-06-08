from rest_framework import serializers
from .models import User
from .models import Product
from .models import Category
from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'profile_desc', 'location', 'profile_pic']
class UserRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'mail', 'password', 'location', 'profile_pic', 'profile_desc']
        extra_kwargs = {'password': {'write_only': True}} #hace que la contraseña se acepte al escribir pero no se devuelva en la respuesta JSON (por seguridad).

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'mail', 'profile_pic', 'location']
class ProductSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer(read_only=True)  # Esto reemplaza el ID por un diccionario con datos
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']