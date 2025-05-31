from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):
    name = models.CharField(max_length=100, help_text="Nombre del usuario.")
    mail = models.EmailField(unique=True, help_text="Correo electrónico del usuario")
    password = models.CharField(max_length=255, help_text="Introduce el nombre completo del producto.")
    location = models.CharField(max_length=100, null=True, blank=True, help_text="Introduce el nombre completo del producto.")
    profile_pic = models.ImageField(upload_to='users/', null=True, blank=True)
    profile_desc = models.TextField(max_length=500, null=True, blank=True, help_text="Introduce el nombre completo del producto.")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    email_verification_code = models.CharField(max_length=4, blank=True, null=True)
    email_verification_expiry = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    def set_password(self, raw_password):
        """Método para encriptar la contraseña antes de guardarla."""
        """"Method for encrypting the password before saving it"""
        self.password = make_password(raw_password) 
        
    def check_password(self, raw_password):
        """Método para verificar si la contraseña es correcta."""
        """Method to verify if the password is correct"""
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)
    
    def is_authenticated(self):
        return True
    
class Category(models.Model):
    name = models.CharField(max_length=45, help_text="Introduce el nombre completo del producto.")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name or "Sin nombre"


class Rating(models.Model):
    rating_value = models.IntegerField([MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True, help_text="Introduce el nombre completo del producto.")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Valoración {self.rating} para {self.User.name}"


class Product(models.Model):
    STATE_CHOICES = [
    ('Como nuevo', 'como_nuevo'),
    ('Muy bueno', 'muy_bueno'),
    ('Bueno', 'bueno'),
    ('Regular', 'regular'),
    ('No funciona', 'no_funciona'),
]

    DISPONIBILITY_CHOICES = [
    ('en_venta', 'En venta'),
    ('vendido', 'Vendido'),
    ('reservado', 'Reservado'),
    ('cancelado', 'Cancelado'),
]


    price = models.IntegerField(help_text="Introduce el precio del producto.")
    name = models.CharField(max_length=45, null=True, blank=True, help_text="Introduce el nombre del producto.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Introduce el nombre del producto.")
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, help_text="Introduce la categoría del producto.")
    description = models.TextField(max_length=5000, null=True, blank=True, help_text="Introduce la descripción del producto.")
    picture = models.ImageField(upload_to='products/', null=True, blank=True)
    disponibility = models.CharField(
        max_length=20, choices=DISPONIBILITY_CHOICES, default=DISPONIBILITY_CHOICES[0][0], null=True, blank=True, help_text="Introduce la disponibilidad del producto."
    )
    state = models.CharField(
        max_length=30, choices=STATE_CHOICES, default=STATE_CHOICES[2][0], null=True, blank=True, help_text="Introduce el estado del producto."
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name or "Producto sin nombre"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Introduce el nombre completo del producto.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Introduce el nombre completo del producto.")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Compra de {self.product.name} por {self.user.name}"


class Offer(models.Model):
    offered_price = models.CharField(max_length=45, null=True, blank=True, help_text="Introduce el precio ofrecido para el producto.")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='offers')  # Relación con Product
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers')  # Relación con User
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Oferta de {self.offered_price} por {self.user.name} para {self.product.name}"

