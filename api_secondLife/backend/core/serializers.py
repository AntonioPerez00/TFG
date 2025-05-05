from rest_framework import serializers
from .models import Usuario

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'contrasena', 'ubicacion', 'foto_perfil', 'desc_perfil']
        extra_kwargs = {'contrasena': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('contrasena')
        usuario = Usuario(**validated_data)
        usuario.set_contrasena(password)
        usuario.save()
        return usuario
