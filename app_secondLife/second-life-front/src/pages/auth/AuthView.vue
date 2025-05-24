<!-- src/views/AuthView.vue -->
<template>
  <div class="flex items-center justify-center min-h-screen mt-[-5rem]">
  <div id="card" >
    <div id="login-register">
      <div>
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
  </div>
</template>

<style>

.continuar{
  background-color: #299CA9;
  border: none;
  color: white;
  border-radius: 10px;
  margin-top: 2rem;
}

input{
  border: none;
  border-bottom: solid;
  padding: 3px;
  margin-bottom: 25px;
  color: #9f9a8f;
  font-size: 18px;
}

input::placeholder{
  color: #9f9a8f;
}

input:focus {
  outline: none;
  box-shadow: none; /* para quitar sombras */
  border-color: transparent; /* o el color que quieras */
  border-bottom-color: #9f9a8f;
}


p{
  color: #9f9a8f;
}

button{
  color: #9f9a8f;
  border: none;
  padding: 10px 25px;
  background-color: transparent;
  margin-bottom: 30px;
  font-size: 19px;
}


hr{
  border-top: 1px solid #f1e2bc;
}

#card{
  background-color: #FFFDF8;
  border-style: solid;
  border-radius: 20px;
  border-color: #f1e2bc;
  padding: 20px;
  padding-top: 10px;
  width: fit-content;
}
#login-register{
  border: 5px;
}

</style>

<script setup>
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
  console.log('Cambiar a login')  // <-- esto debería aparecer ahora
  activeTab.value = 'login'
}
</script>
