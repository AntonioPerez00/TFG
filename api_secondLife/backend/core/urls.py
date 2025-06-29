from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, get_categories, get_product_states, register_user, login_user, logout_user, verify_email_code
from .views import MyProductViewSet, get_categories, get_product_states, register_user, login_user, logout_user, verify_email_code
from .views import mark_product_sold
from .views import user_profile
from .views import get_user_by_mail
from .views import UserProductsView

# Definir el router
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'my-products', MyProductViewSet, basename='my-product')

urlpatterns = [
    path('registro/', register_user),
    path('login/', login_user),
    path('logout/', logout_user),
    path('verify-code/', verify_email_code, name='verify-code'),
    path('products/<int:product_id>/mark_sold/', mark_product_sold, name='mark_product_sold'),
    path('categories/', get_categories, name='get_categories'),
    path('products/states/', get_product_states, name='get_product_states'),
    path('profile/', user_profile, name='user-profile'),
    path('users/<str:mail>/', get_user_by_mail),
    path('users/<str:mail>/products/', UserProductsView.as_view(), name='user-products'),
]


# Añadir las rutas generadas automáticamente por el router de productos
urlpatterns += router.urls
