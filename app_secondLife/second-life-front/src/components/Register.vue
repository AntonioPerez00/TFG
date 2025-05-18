<template>
  <form @submit.prevent="onSubmit" class="space-y-4">
    <input type="email" placeholder="E-mail" class="w-full p-2 border rounded" required />
    <input type="text" placeholder="Nombre de usuario" class="w-full p-2 border rounded" required />
    <input type="password" placeholder="Contraseña" class="w-full p-2 border rounded" required />
    <button type="submit" class="w-full bg-teal-500 hover:bg-teal-600 text-white p-2 rounded">
      Continuar
    </button>
  </form>
</template>

<script setup>
import { onMounted } from 'vue'

const emit = defineEmits(['registered'])

function onSubmit() {
  console.log('Submit clicked')
  emit('registered')  // 👈 esto sí emite correctamente
}

onMounted(() => {
  console.log('Register mounted')
})
</script>

