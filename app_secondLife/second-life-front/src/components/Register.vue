<template>
  <form @submit.prevent="onSubmit" class="space-y-4">
    <template v-if="!isCodeStep">
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
      <button type="submit" class="continuar">Continuar</button>
    </template>

    <template v-else>
      <input v-model="code" type="text" placeholder="Código de verificación" required />
      <button @click.prevent="verifyCode" class="continuar">Verificar código</button>
    </template>
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
const isCodeStep = ref(false)
const code = ref('')

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

  const messages = Object.values(errorData)
    .flat()
    .join('\n') // Para mostrar múltiples errores si los hay

  alert(`Error en el registro:\n${messages}`)
  return
}


    console.log('Usuario registrado con éxito')
    alert('Usuario registrado. Revisa tu correo para activarlo.')
    isCodeStep.value = true // ← Cambia al paso del código
  } catch (error) {
    console.error('Error:', error)
    alert('Error de red al registrar.')
  }
}

async function verifyCode() {
  try {
    const response = await fetch('http://localhost:8000/api/verify-code/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        mail: email.value,
        code: code.value,
      }),
    })

    if (!response.ok) {
      const errorData = await response.json()
      console.error('Error en la verificación:', errorData)
      alert('Código incorrecto.')
      return
    }

    alert('Cuenta activada. Ya puedes iniciar sesión.')
    emit('registered') // o cambia vista a login
  } catch (error) {
    console.error('Error en verificación:', error)
    alert('Error de red al verificar.')
  }
}
</script>
