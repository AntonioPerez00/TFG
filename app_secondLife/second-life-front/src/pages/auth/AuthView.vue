<!-- src/views/AuthView.vue -->
<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="bg-white w-full max-w-md rounded-xl shadow-lg p-6 relative">
      <div class="flex mb-4 border-b">
        <button
          :class="['flex-1 text-center py-2', activeTab === 'login' ? 'border-b-2 border-teal-500 font-bold' : 'text-gray-500']"
          @click="activeTab = 'login'"
        >
          Iniciar sesión
        </button>
        <button
          :class="['flex-1 text-center py-2', activeTab === 'register' ? 'border-b-2 border-teal-500 font-bold' : 'text-gray-500']"
          @click="activeTab = 'register'"
        >
          Registrarse
        </button>
      </div>

      <Login v-if="activeTab === 'login'" @authenticated="goToHome" />
      <Register v-else @registered="switchToLogin" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Login from '../../components/Login.vue'
import Register from '../../components/Register.vue'

const activeTab = ref('login')
const router = useRouter()

function goToHome() {
  router.push('/home')
}

function switchToLogin() {
  console.log('Cambiar a login')  // <-- esto debería aparecer ahora
  activeTab.value = 'login'
}
</script>
