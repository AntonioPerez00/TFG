from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    name = models.CharField(max_length=100, help_text="Nombre completo del usuario.")
    mail = models.EmailField(unique=True, help_text="Correo electrónico usado para iniciar sesión.")
    password = models.CharField(max_length=255, help_text="Contraseña del usuario (se almacena encriptada).")
    location = models.CharField(max_length=100, null=True, blank=True, help_text="Ubicación del usuario.")
    profile_pic = models.ImageField(upload_to='users/', null=True, blank=True, help_text="Foto de perfil del usuario.")
    profile_desc = models.TextField(max_length=500, null=True, blank=True, help_text="Descripción pública del perfil del usuario.")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    email_verification_code = models.CharField(max_length=4, blank=True, null=True, help_text="Código enviado por correo para verificar la cuenta.")
    email_verification_expiry = models.DateTimeField(blank=True, null=True, help_text="Fecha y hora de expiración del código de verificación.")

    def __str__(self):
        return self.name

    def set_password(self, raw_password):
        """Método para encriptar la contraseña antes de guardarla."""
        self.password = make_password(raw_password)
        
    def check_password(self, raw_password):
        """Método para verificar si la contraseña es correcta."""
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)
    
    def is_authenticated(self):
        return True


class Category(models.Model):
    name = models.CharField(max_length=45, help_text="Nombre de la categoría del producto.")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name or "Sin nombre"


class Rating(models.Model):
    rating_value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True, help_text="Valor numérico de la valoración (0 a 5).")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Usuario que ha recibido la valoración.")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Valoración {self.rating_value} para {self.user.name}"


class Product(models.Model):
    STATE_CHOICES = [
        ('Como nuevo', 'como_nuevo'),
        ('Muy bueno', 'muy_bueno'),
        ('Bueno', 'bueno'),
        ('Regular', 'regular'),
        ('Lo ha dado todo', 'lo_ha_dado_todo'),
    ]

    DISPONIBILITY_CHOICES = [
        ('en_venta', 'En venta'),
        ('vendido', 'Vendido'),
        ('reservado', 'Reservado'),
        ('cancelado', 'Cancelado'),
    ]

    price = models.DecimalField(
    max_digits=10,  # Total de dígitos
    decimal_places=2,  # Número de decimales permitidos
    help_text="Precio del producto en euros (con decimales)."
    )
    name = models.CharField(max_length=45, null=True, blank=True, help_text="Título o nombre del producto.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Usuario que ha publicado el producto.")
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, help_text="Categoría a la que pertenece el producto.")
    description = models.TextField(max_length=5000, null=True, blank=True, help_text="Descripción detallada del producto.")
    picture1 = models.ImageField(upload_to='products/', null=True, blank=True, help_text="Imagen principal del producto.")
    picture2 = models.ImageField(upload_to='products/', null=True, blank=True, help_text="Imagen adicional del producto.")
    picture3 = models.ImageField(upload_to='products/', null=True, blank=True, help_text="Imagen adicional del producto.")
    picture4 = models.ImageField(upload_to='products/', null=True, blank=True, help_text="Imagen adicional del producto.")
    picture5 = models.ImageField(upload_to='products/', null=True, blank=True, help_text="Imagen adicional del producto.")
    disponibility = models.CharField(
        max_length=20,
        choices=DISPONIBILITY_CHOICES,
        default=DISPONIBILITY_CHOICES[0][0],
        null=True,
        blank=True,
        help_text="Estado de disponibilidad del producto (en venta, vendido, etc.)."
    )
    state = models.CharField(
        max_length=30,
        choices=STATE_CHOICES,
        default=STATE_CHOICES[2][0],
        null=True,
        blank=True,
        help_text="Condición del producto (como nuevo, bueno, etc.)."
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name or "Producto sin nombre"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Producto que ha sido comprado.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Usuario que ha realizado la compra.")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Compra de {self.product.name} por {self.user.name}"


class Offer(models.Model):
    offered_price = models.CharField(max_length=45, null=True, blank=True, help_text="Precio ofrecido por el usuario.")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='offers', help_text="Producto al que se hace la oferta.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers', help_text="Usuario que realiza la oferta.")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Oferta de {self.offered_price} por {self.user.name} para {self.product.name}"
