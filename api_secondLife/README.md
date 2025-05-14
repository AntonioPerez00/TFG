# TFG - 2º DAM

## Antonio Pérez Cuéllar
Este proyecto es una plataforma de compraventa de productos de segunda mano, similar a Wallapop. Incluye autenticación de usuarios, gestión de productos con imágenes, y control de permisos para proteger los datos de cada usuario.

### Clonar el repositorio

```bash
git clone https://github.com/AntonioPerez00/TFG
cd tu-repo
```

### Autenticación

Para iniciar sesión y obtener los tokens necesarios para acceder a rutas protegidas:

- `POST /api/login/`

```json
{
  "mail": "antonio@example.com",
  "password": "1234"
}
```
La respuesta será algo así
```json
{
  "refresh": "xxx",
  "access": "yyy"
}
```
Un token de acceso que dura un día y uno de refresco que dura 90.

El token de acceso se suará en el header de las peticiones protegidas, como en el caso de crear un producto.
```json
Authorization: Bearer <access_token>
```

### Comandos básicos

- `docker compose up --build`  
  Ejecuta el entorno en Docker (local).

- `python manage.py makemigrations`  
  Crea las migraciones (cada vez que se hace un cambio en `models.py`).

- `python manage.py migrate`  
  Aplica las migraciones.

- `rm core/migrations/0*.py`  
  Borra las migraciones.

### Registro de usuarios

Para registrar un nuevo usuario, realiza una petición `POST` a la siguiente URL:  
**`http://localhost:8000/api/registro/`**

- **Ruta en `urls.py`:**
  - `config -> urls.py -> /api/`
  - `core -> urls.py -> /registro/`

#### Ejemplo de JSON para crear un usuario:

```json
{
  "name": "Antonio García",
  "mail": "antonio@example.com",
  "password": "1234",
  "location": "Sevilla",
  "profile_pic": "https://example.com/foto.jpg",
  "profile_desc": "Me gusta comprar y vender cosas de segunda mano"
}
```


### Productos
#### Crear producto
- `POST /api/products/`
- Para crear el producto también necesitarás el token que se crea con el login del usuario.

```json
{
  "name": "Camiseta verde",
  "price": "20",
  "category": "2",
  "description": null
}
```
#### Listar productos
- `GET /api/products/`
- Este no requiere token de autenticación.

#### Detalles de producto
- `GET /api/products/<id>/`

#### Editar producto (PUT toca todos los cambios)
- `PUT /api/products/<id>/`
#### Editar producto (PATCH toca solo el campo que necesitas)
- `PATCH /api/products/<id>/`
#### Editar de producto
- `DELETE /api/products/<id>/`

#### Restricciones
- Solo los usuarios logeados podrán ver y  crear productos, esto se controla mediante el access token.
- Solo los usuarios propietarios del producto podrán editarlo o eliminarlo. (permissions.py)

### Filtros de Productos

#### 1. **Filtrar productos por categoría**
- **Método**: `GET`
- **URL**: `http://localhost:8000/api/products/?category=2`
- **Descripción**: Filtra los productos que pertenecen a la categoría con ID `2`.

#### 2. **Filtrar productos por disponibilidad**
- **Método**: `GET`
- **URL**: `http://localhost:8000/api/products/?disponibility=en_venta`
- **Descripción**: Filtra los productos que están disponibles para la venta (disponibilidad "en_venta").

#### 3. **Filtrar productos por estado**
- **Método**: `GET`
- **URL**: `http://localhost:8000/api/products/?state=bueno`
- **Descripción**: Filtra los productos que están en buen estado.

#### 4. **Filtrar productos por ubicación**
- **Método**: `GET`
- **URL**: `http://localhost:8000/api/products/?location=Sevilla`
- **Descripción**: Filtra los productos que tienen la ubicación "Sevilla".

#### 5. **Filtrar productos por precio mínimo y máximo**
- **Método**: `GET`
- **URL**: `http://localhost:8000/api/products/?min_price=10&max_price=100`
- **Descripción**: Filtra los productos cuyo precio esté entre 10 y 100.

#### 6. **Ordenar productos por precio**
- **Método**: `GET`
- **URL**: `http://localhost:8000/api/products/?ordering=-price`
- **Descripción**: Ordena los productos de mayor a menor precio.

#### 7. **Filtrar productos por múltiples filtros combinados**
- **Método**: `GET`
- **URL**: `http://localhost:8000/api/products/?category=2&state=bueno&min_price=20&max_price=100&ordering=-price`
- **Descripción**: Filtra los productos de la categoría 2, en buen estado, cuyo precio esté entre 20 y 100, ordenados de mayor a menor precio.


### Notas

#### Migraciones:
Las migraciones permiten sincronizar los cambios de los modelos de la base de datos con el esquema real de la base de datos.  
Asegúrate de ejecutar las migraciones después de realizar cambios en los modelos.

#### Superusuario:
Si necesitas crear un superusuario para acceder al panel de administración de Django, usa el siguiente comando:

```bash
python manage.py createsuperuser
