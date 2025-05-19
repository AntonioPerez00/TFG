

<template>
  <form @submit.prevent="login" class="space-y-4">
    <input v-model="mail" type="mail" placeholder="E-mail" class="w-full p-2 border rounded" required />
    <input v-model="password" type="password" placeholder="Contraseña" class="w-full p-2 border rounded" required />
    <p v-if="error" class="text-red-500 text-sm">{{ error }}</p>
    <button type="submit" class="w-full bg-teal-500 hover:bg-teal-600 text-white p-2 rounded">
      Iniciar sesión
    </button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const mail = ref('')
const password = ref('')
const error = ref('')
const emit = defineEmits(['authenticated'])
// const login = async () => {
//   try {
//     const response = await axios.post('http://localhost:8000/api/login/', {
//       mail: mail.value,
//       password: password.value,
//     })

//     // Guarda el token en localStorage o donde prefieras
//     localStorage.setItem('access', response.data.access)
//     localStorage.setItem('refresh', response.data.refresh)

//     emit('authenticated') // Esto hará que te redirija a /home
//   } catch (err) {
//     error.value = 'mail o contraseña incorrectos'
//     console.error(err)
//   }
// }


async function login() {
  error.value = ''
  try {
    const response = await fetch('http://localhost:8000/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        mail: mail.value,
        password: password.value,
      }),
    })

    if (!response.ok) {
      let errorText = 'Login fallido'
      try {
        const errorData = await response.json()
        errorText = errorData.detail || errorText
      } catch {
        // No se pudo parsear JSON, mantenemos mensaje por defecto
      }
      error.value = errorText
      return
    }

    let data = null
    try {
      data = await response.json()
    } catch {
      error.value = 'Respuesta no válida del servidor'
      return
    }

    localStorage.setItem('access_token', data.access)
    localStorage.setItem('refresh_token', data.refresh)

    emit('authenticated')
  } catch (err) {
    error.value = 'Error de conexión'
    console.error('Error en fetch:', err)
  }
}

</script>