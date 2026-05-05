# 🛍️ Aplicación Web - TFG "Second Life"

Este proyecto es una aplicación web desarrollada como parte del Trabajo de Fin de Grado (TFG). Permite la compraventa de productos de segunda mano, inspirada en plataformas como Wallapop.

---

## 📁 Estructura del Proyecto

### 📦 `api_secondLife/`
Contiene el **backend** de la aplicación, desarrollado con **Django** y **Django REST Framework**.  
Incluye funcionalidades como:

- Registro e inicio de sesión de usuarios
- Autenticación con JWT
- Gestión de productos
- Subida y eliminación de imágenes
- Valoraciones y filtros avanzados

### 🌐 `app_secondLife/`
Contiene el **frontend** de la aplicación, desarrollado con **Vue.js** y **TailwindCSS**.  
Incluye vistas responsivas para:

- Registro e inicio de sesión
- Listado y filtrado de productos
- Publicación de productos
- Valoraciones de vendedores

---

### 📄 `docs/`
Contiene la documentación asociada al TFG:

- Esquema entidad-relación (ER)
- Memoria del proyecto en formato **PDF**
- Memoria del proyecto en formato **Word**

---

## 🚀 Tecnologías utilizadas

- **Frontend:** Vue.js, TailwindCSS, Pinia
- **Backend:** Django, Django REST Framework, JWT, Djoser
- **Base de datos:** MySQL
- **Despliegue:** Docker

---

## 🛠️ Instalación rápida (desarrollo)

```bash
# Clonar el repositorio
git https://github.com/AntonioPerez00/TFG

<<<<<<< HEAD
# Levantar el backend y frontend (si tienes Docker)
docker-compose up --build

=======
# Levantar el backend (con Docker)
docker-compose up --build

# Levantar el frontend
npm run dev

>>>>>>> 97c48a087f0e1dc600f2eddad6c55c67adbab51e
# Puede que de errores por necesitar instalar muchas dependencias en tu máquina local
