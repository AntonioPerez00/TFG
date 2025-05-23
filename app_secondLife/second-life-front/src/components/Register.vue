<template>
  <form @submit.prevent="onSubmit" class="space-y-4">
    <input v-model="email" type="email" placeholder="E-mail" required />
    <input v-model="username" type="text" placeholder="Nombre de usuario" required />
    <div class="passwd">
      <input
        :key="showFrontPasswordRegister"
        v-model="frontPasswordRegister"
        :type="showFrontPasswordRegister ? 'text' : 'password'"
        placeholder="Contraseña"
        required
        style="padding-bottom: 0px; margin: 5px; margin-left: 0px;"
        class="border-none"
      />
      <img
        :src="showFrontPasswordRegister ? eye : invisible"
        @click="showFrontPasswordRegister = !showFrontPasswordRegister"
        alt="Toggle password"
      />
    </div>
    <button type="submit" class="continuar">
      Continuar
    </button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import eye from '../assets/ojo.png'
import invisible from '../assets/invisible.png'

const email = ref('')
const username = ref('')
const frontPasswordRegister = ref('')
const showFrontPasswordRegister = ref(false)

const emit = defineEmits(['registered'])

async function onSubmit() {
  try {
    const response = await fetch('http://localhost:8000/api/registro/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        mail: email.value,
        name: username.value,
        password: frontPasswordRegister.value,
      }),
    })

    if (!response.ok) {
      const errorData = await response.json()
      console.error('Error en el registro:', errorData)
      alert('Error en el registro: ' + JSON.stringify(errorData))
      return
    }

    console.log('Usuario registrado con éxito')
    emit('registered')
    alert('Usuario registrado. Revisa tu correo para activarlo.')
  } catch (error) {
    console.error('Error:', error)
    alert('Error de red al registrar.')
  }
}
</script>

