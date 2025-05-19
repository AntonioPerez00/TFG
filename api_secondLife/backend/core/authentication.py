from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from core.models import User as CustomUser  # importa tu modelo personalizado
from django.contrib.auth.backends import BaseBackend
from core.models import User

class EmailBackend(BaseBackend):
    def authenticate(self, request, mail=None, password=None, **kwargs):
        print(f"Intentando autenticar: mail={mail}, password={password}")
        if mail is None or password is None:
            print("Faltan mail o password")
            return None
        try:
            user = User.objects.get(mail=mail)
            print(f"Usuario encontrado: {user}")
        except User.DoesNotExist:
            print("Usuario no encontrado")
            return None
        if user.check_password(password) and user.is_active:
            print("Contraseña correcta y usuario activo")
            return user
        print("Contraseña incorrecta o usuario no activo")
        return None

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get("user_id")

        if user_id is None:
            raise AuthenticationFailed("Token inválido: no hay user_id")

        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed("Usuario no encontrado en core.User")
