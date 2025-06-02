<!-- src/views/AuthView.vue -->
<template>
  <div class="flex items-center justify-center min-h-screen mt-[-5rem]">
    <NavBar />
  <div id="card" class="bg-[#FFFDF8] border border-[#f1e2bc] rounded-[20px] p-[20px] pt-[10px] w-fit">
    <div id="login-register">
      <div>
        <button
          :class="['flex-1 text-center py-2 bg-transparent pt-[10px] pb-[10px] pl-[25px] pr-[25px] mb-[30px] text-[19px] text-[#9f9a8f]', 
          activeTab === 'login' ? 'border-t-0 border-l-0 border-r-0 border-[#FFFDF8]' : 'border-none']"
          @click="activeTab = 'login'"
        >
          Iniciar sesión
        </button>
        <button
          :class="['flex-1 text-center py-2 bg-transparent pt-[10px] pb-[10px] pl-[25px] pr-[25px] mb-[30px] text-[19px] text-[#9f9a8f]', 
          activeTab === 'register' ? 'border-t-0 border-l-0 border-r-0 border-[#FFFDF8]' : 'border-none']"
          @click="activeTab = 'register'"
        >
          Registrarse
        </button>
      </div>

      <Login v-if="activeTab === 'login'" @authenticated="goToHome" />
      <Register v-else @registered="switchToLogin" />
    </div>
  </div>
  </div>
</template>

<script setup>
import NavBar from '../../components/SimpleNavBar.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Login from '../../components/auth/Login.vue'
import Register from '../../components/auth/Register.vue'

const activeTab = ref('login')
const router = useRouter()

function goToHome() {
  router.push('/home')
}

function switchToLogin() {
  activeTab.value = 'login'
}
</script>
