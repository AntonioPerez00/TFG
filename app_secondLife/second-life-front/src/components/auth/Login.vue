

<template>
  <div id="login-container">
    <form @submit.prevent="login" class="flex flex-col">
    <input
      v-model="mail"
      type="email"
      placeholder="E-mail"
      required
      class="border-0 border-b border-b-[#9f9a8f] p-[3px] mb-[25px] text-[#9f9a8f] text-[18px] bg-[#FFFDF8] focus:outline-none placeholder-[#9f9a8f]"
    />

    <div class="border-0 border-b border-b-[#9f9a8f]">
      <input
        :key="showFrontPassword"
        v-model="password"
        :type="showFrontPassword ? 'text' : 'password'"
        placeholder="Contraseña"
        required
        style="padding-bottom: 0px; margin: 5px; margin-left: 0px;"
        class="border-none p-[3px] mb-[25px] text-[#9f9a8f] text-[18px] bg-[#FFFDF8] focus:outline-none placeholder-[#9f9a8f]"
/>
      <img
        :src="showFrontPassword ? eye : invisible"
        @click="showFrontPassword = !showFrontPassword"
        alt="Toggle password"
        class="w-[18px] float-right mt-[8px]"
      />

    </div>
    <p v-if="error" id="error" class="text-[#CC6565]">{{ error }}</p>
    <button type="submit" class="bg-[#299CA9] cursor-pointer border-none text-[#FFFFFF] rounded-[10px] mt-[2rem] pt-[10px] pb-[10px] pl-[25px] pr-[25px] text-[19px] hover:bg-[#217d86]">
      Iniciar sesión
    </button>
  </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import eye from '../../assets/ojo.png'
import invisible from '../../assets/invisible.png'

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

    // Buscar distintos posibles campos de error
    if (errorData.detail) {
      errorText = errorData.detail
    } else {
      errorText = Object.values(errorData).flat().join('\n')
    }
  } catch {
    errorText = 'Respuesta no válida del servidor'
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
    localStorage.setItem('name', data.name)
    localStorage.setItem('mail', data.mail)
    localStorage.setItem('profile_pic', data.profile_pic)

    emit('authenticated')
  } catch (err) {
    error.value = 'Error de conexión'
    console.error('Error en fetch:', err)
  }
  
}

const frontPassword = ref('')
const showFrontPassword = ref(false)
</script>