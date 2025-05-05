from django.db import models
from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=100, null=True, blank=True)
    foto_perfil = models.CharField(max_length=45, null=True, blank=True)
    desc_perfil = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def set_contrasena(self, raw_password):
        """Método para encriptar la contraseña antes de guardarla."""
        self.contrasena = make_password(raw_password)
        
    def check_contrasena(self, raw_password):
        """Método para verificar si la contraseña es correcta."""
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.contrasena)
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.nombre or "Sin nombre"


class Valoracion(models.Model):
    valoracion = models.IntegerField(null=True, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Valoración {self.valoracion} para {self.usuario.nombre}"


class Producto(models.Model):
    ESTADO_CHOICES = [
        ('Como nuevo', 'Como nuevo'),
        ('Muy bueno', 'Muy bueno'),
        ('Bueno', 'Bueno'),
        ('Bueno con marcas de uso', 'Bueno con marcas de uso'),
        ('Regular', 'Regular'),
        ('Mal', 'Mal'),
    ]

    DISPONIBILIDAD_CHOICES = [
        ('comprado', 'Comprado'),
        ('reservado', 'Reservado'),
        ('en_venta', 'En venta'),
        ('cancelado', 'Cancelado'),
    ]

    precio = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=45, null=True, blank=True)
    fecha_pub = models.DateTimeField(null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    valoracion = models.ForeignKey(Valoracion, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    disponibilidad = models.CharField(
        max_length=20, choices=DISPONIBILIDAD_CHOICES, null=True, blank=True
    )
    estado = models.CharField(
        max_length=30, choices=ESTADO_CHOICES, null=True, blank=True
    )

    def __str__(self):
        return self.nombre or "Producto sin nombre"


class Foto(models.Model):
    url = models.CharField(max_length=255, null=True, blank=True)
    fecha_subida = models.DateTimeField(null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.url or f"Foto {self.id}"


class Compra(models.Model):
    fechaCompra = models.DateTimeField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Compra de {self.producto.nombre} por {self.usuario.nombre}"


class Ofertas(models.Model):
    precio_ofertado = models.CharField(max_length=45, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Oferta de {self.precio_ofertado} por {self.usuario.nombre}"
