from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, register_user, login_user, logout_user

# Definir el router
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

# URLs de autenticación
urlpatterns = [
    path('registro/', register_user),
    path('login/', login_user),
    path('logout/', logout_user),
]

# Añadir las rutas generadas automáticamente por el router de productos
urlpatterns += router.urls
