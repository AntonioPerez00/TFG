// src/services/api.js
import axios from 'axios'
import router from '../router'

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


api.interceptors.response.use(
  response => response,
  error => {
    // Si el error es 401 y venía de una petición con Authorization
    if (
      error.response &&
      error.response.status === 401 &&
      error.config.headers.Authorization
    ) {
      // 1. Borrar tokens
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')

      // 2. Redirigir al login
      router.push('/auth')

      // 3. Mostrar aviso (opcional)
      console.warn('Token expirado. Redirigiendo al login...')
    }

    return Promise.reject(error)
  }
)


export default api
