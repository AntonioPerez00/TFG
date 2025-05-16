# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserRegistroSerializer
from .models import User
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from core.models import User 
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tokens import email_verification_token
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from datetime import timedelta
import random
from django.utils import timezone

# Se hacen de forma diferente al tener que utilizar campos diferentes a los de los usuarios de django
# @api_view(['POST'])
# def register_user(request):
#     serializer = UserRegistroSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"mensaje": "Usuario creado correctamente."}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistroSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.is_active = False  # Para evitar login antes de verificar

        # Generar código y expiración
        code = f"{random.randint(0, 9999):04d}"
        user.email_verification_code = code
        user.email_verification_expiry = timezone.now() + timedelta(minutes=15)
        user.save()

        # Enviar correo con código
        send_mail(
            subject='Tu código de verificación',
            message=f'Tu código de verificación es: {code}',
            from_email='a.secondlifeteam@gmail.com',
            recipient_list=[user.mail],
            fail_silently=False,
        )

        return Response({"mensaje": "Usuario creado. Revisa tu correo para verificar tu cuenta."}, status=201)
    
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def verify_email_code(request):
    mail = request.data.get('mail')
    code = request.data.get('code')
    try:
        user = User.objects.get(mail=mail)
    except User.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=404)
    if user.email_verification_code == code and user.email_verification_expiry > timezone.now():
        user.is_active = True
        user.email_verification_code = None
        user.email_verification_expiry = None
        user.save()
        return Response({"mensaje": "Correo verificado correctamente"})
    return Response({"error": "Código inválido o expirado"}, status=400)

@api_view(['POST'])
def login_user(request):
    mail = request.data.get('mail')
    password = request.data.get('password')

    if not mail or not password:
        return Response({'error': 'Faltan credenciales'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, mail=mail, password=password) #Busca un usuario con estos datos

    #Si el usuario es válido creo los tokens
    if user:
        refresh = RefreshToken.for_user(user) 
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def logout_user(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"mensaje": "Sesión cerrada correctamente."}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    filterset_fields = {
        'category': ['exact'],
        'disponibility': ['exact'],
        'state': ['exact'],
        'user__location': ['exact'],
        'price': ['gte', 'lte'],
    }
    
    ordering_fields = ['price', 'created_at']
    search_fields = ['name', 'description']
    
    def get_queryset(self):
        queryset = Product.objects.all()
        user = self.request.user
        if user.is_authenticated:
            # Excluir productos propios
            queryset = queryset.exclude(user=user)
        # Opcional: aquí podrías filtrar también solo productos en venta, por ejemplo:
        queryset = queryset.filter(disponibility='en_venta')
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

