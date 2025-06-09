from rest_framework import serializers
from .models import User
from .models import Product
from .models import Category
from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'profile_desc', 'location', 'profile_pic', 'mail']
        
    def update(self, instance, validated_data):
        # Si 'profile_pic' está en los datos y es una cadena vacía, eliminamos la imagen
        profile_pic = validated_data.get('profile_pic', None)
        if profile_pic == '':
            if instance.profile_pic:
                instance.profile_pic.delete(save=False)  # Borra el archivo físico
            instance.profile_pic = None
            validated_data.pop('profile_pic')  # No queremos que intente guardar '' en el campo

        return super().update(instance, validated_data)
    
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
    user = UserBasicSerializer(read_only=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = '__all__'

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if request and request.method == 'PUT':
            for i in range(1, 6):
                image_field = f'picture{i}'
                delete_flag = request.data.get(f'delete_picture{i}', 'false')

                if delete_flag.lower() == 'true':
                    # Eliminar la imagen si existe
                    setattr(instance, image_field, None)

                elif image_field in request.FILES:
                    # Reemplazar con nueva imagen
                    setattr(instance, image_field, request.FILES[image_field])

        # Actualizar otros campos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']