from rest_framework import serializers
from .models import User

class UserRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nombre', 'correo', 'contrasena', 'ubicacion', 'foto_perfil', 'desc_perfil']
        extra_kwargs = {'contrasena': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('contrasena')
        User = User(**validated_data)
        User.set_contrasena(password)
        User.save()
        return User
