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

# Se hacen de forma diferente al tener que utilizar campos diferentes a los de los usuarios de django
@api_view(['POST'])
def register_user(request):
    serializer = UserRegistroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"mensaje": "Usuario creado correctamente."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

