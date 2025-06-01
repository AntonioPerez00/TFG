// src/services/api.js
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
})

// Añadir token en cada petición (si existe)
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Manejar errores globales
api.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 401) {
      // 1. Eliminar token (opcional)
      localStorage.removeItem('token')

      // 2. Redirigir al login
      router.push('/login')  // o donde manejes la autenticación

      // 3. (opcional) Mostrar notificación
      console.warn('Sesión expirada. Redirigiendo al login...')
    }

    return Promise.reject(error)
  }
)

export default api
