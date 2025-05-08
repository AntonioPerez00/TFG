# TFG - 2º DAM

## Antonio Pérez Cuéllar

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
### Notas

#### Migraciones:
Las migraciones permiten sincronizar los cambios de los modelos de la base de datos con el esquema real de la base de datos.  
Asegúrate de ejecutar las migraciones después de realizar cambios en los modelos.

#### Superusuario:
Si necesitas crear un superusuario para acceder al panel de administración de Django, usa el siguiente comando:

```bash
python manage.py createsuperuser
