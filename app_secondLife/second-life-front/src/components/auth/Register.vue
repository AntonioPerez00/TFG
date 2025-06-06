<template>
  <form @submit.prevent="onSubmit" class="flex flex-col">
    <template v-if="!isCodeStep">
      <input
      v-model="email"
      type="email"
      placeholder="E-mail"
      required
      class="border-0 border-b border-b-[#9f9a8f] p-[3px] mb-[25px] text-[#9f9a8f] text-[18px] bg-[#FFFDF8] focus:outline-none placeholder-[#9f9a8f]"
    />
      <input v-model="username" type="text" placeholder="Nombre de usuario" required
        class="border-0 border-b border-b-[#9f9a8f] p-[3px] mb-[25px] text-[#9f9a8f] text-[18px] bg-[#FFFDF8] focus:outline-none placeholder-[#9f9a8f]"
      />
      <div class="border-0 border-b border-b-[#9f9a8f]">
        <input
          :key="showFrontPasswordRegister"
          v-model="frontPasswordRegister"
          :type="showFrontPasswordRegister ? 'text' : 'password'"
          placeholder="Contraseña"
          required
          style="padding-bottom: 0px; margin: 5px; margin-left: 0px;"
          class="border-none p-[3px] mb-[25px] text-[#9f9a8f] text-[18px] bg-[#FFFDF8] focus:outline-none placeholder-[#9f9a8f]"
        />
        <img
          :src="showFrontPasswordRegister ? eye : invisible"
          @click="showFrontPasswordRegister = !showFrontPasswordRegister"
          alt="Toggle password"
          class="w-[18px] float-right mt-[8px]"
        />
      </div>

      <div class="border-0 border-b border-b-[#9f9a8f] mt-[1.5rem]">
        <input
          :key="showFrontPasswordRegister"
          v-model="confirmPassword"
          :type="showFrontPasswordRegister ? 'text' : 'password'"
          placeholder="Repite la contraseña"
          required
          style="padding-bottom: 0px; margin: 5px; margin-left: 0px;"
          class="border-none p-[3px] mb-[5px] text-[#9f9a8f] text-[18px] bg-[#FFFDF8] focus:outline-none placeholder-[#9f9a8f]"
        />
        <img
          :src="showFrontPasswordRegister ? eye : invisible"
          @click="showFrontPasswordRegister = !showFrontPasswordRegister"
          alt="Toggle password"
          class="w-[18px] float-right mt-[8px]"
        />
      </div>

      <p v-if="passwordMismatch" class="text-red-600 text-sm mb-[20px]">Las contraseñas no coinciden.</p>
      <button
        type="submit"
        :disabled="passwordMismatch"
        class="bg-[#299CA9] disabled:opacity-50 pointer-cursor border-none text-[#FFFFFF] rounded-[10px] mt-[2rem] pt-[10px] pb-[10px] pl-[25px] pr-[25px] text-[19px] cursor-pointer hover:bg-[#217d86]"
      >
        Continuar
      </button>

    </template>

    <template v-else>
      <input v-model="code" type="text" placeholder="Código de verificación" required class="border-0 border-b border-b-[#9f9a8f] p-[3px] mb-[25px] text-[#9f9a8f] text-[18px] bg-[#FFFDF8] focus:outline-none placeholder-[#9f9a8f]"/>
      <button @click.prevent="verifyCode" class="bg-[#299CA9] border-none text-[#FFFFFF] rounded-[10px] mt-[2rem] pt-[10px] pb-[10px] pl-[25px] pr-[25px] text-[19px]  cursor-pointer hover:bg-[#217d86]">Verificar código</button>
    </template>
  </form>
</template>

<script setup>
import eye from '../../assets/ojo.png'
import invisible from '../../assets/invisible.png'
import { ref, watch } from 'vue'

const email = ref('')
const username = ref('')
const frontPasswordRegister = ref('')
const showFrontPasswordRegister = ref(false)
const isCodeStep = ref(false)
const code = ref('')
const confirmPassword = ref('')
const passwordMismatch = ref(false)

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

watch([frontPasswordRegister, confirmPassword], () => {
  passwordMismatch.value =
    frontPasswordRegister.value !== confirmPassword.value
})
</script>
