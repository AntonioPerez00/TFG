

<template>
  <div id="login-container">
    <form @submit.prevent="login">
    <input v-model="mail" type="mail" placeholder="E-mail" required />
    <div class="passwd">
      <input
        :key="showFrontPassword"
        v-model="password"
        :type="showFrontPassword ? 'text' : 'password'"
        placeholder="Contraseña"
        required
        style="padding-bottom: 0px; margin: 5px; margin-left: 0px;"
        class="border-none"
      />
      <img
        :src="showFrontPassword ? eye : invisible"
        @click="showFrontPassword = !showFrontPassword"
        alt="Toggle password"
      />

    </div>
    <p v-if="error" class="text-red-500 text-sm">{{ error }}</p>
    <button type="submit" class="continuar">
      Iniciar sesión
    </button>
  </form>
  </div>
</template>

<style>

img{
  width: 18px;
  float: right;
  margin-top: 8px;
}

form {
 display: flex;
 flex-direction: column;
}

.passwd{
  border-bottom: solid;
  color: #9f9a8f;
  padding: 0px;
}
</style>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import eye from '../assets/ojo.png'
import invisible from '../assets/invisible.png'

const mail = ref('')
const password = ref('')
const error = ref('')
const emit = defineEmits(['authenticated'])

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

const frontPassword = ref('')
const showFrontPassword = ref(false)
</script>