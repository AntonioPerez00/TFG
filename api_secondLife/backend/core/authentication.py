from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from core.models import User as CustomUser  # importa tu modelo personalizado

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get("user_id")

        if user_id is None:
            raise AuthenticationFailed("Token inválido: no hay user_id")

        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed("Usuario no encontrado en core.User")
