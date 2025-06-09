<template>
  <NavBar />

  <div class="p-[5rem] bg-[#FFFDF8]">
    <div id="user" class="mt-[5rem] w-full flex flex-row items-center justify-between">
      <div class="flex flex-row items-center">
        <img
          :src="profile_pic || '/usuario.png'"
          alt="usuario"
          class="w-[6rem] h-[6rem] rounded-full object-cover"
        />

        <div class="ml-[1.5rem] flex flex-col">
          <span class="text-[1.5rem] font-medium">
            {{ nombreUsuario || 'Iniciar sesión' }}
          </span>
          <span class="text-[1rem] text-gray-500">
            {{ correo || '' }}
          </span>
          
        </div>

        <img 
          src="/editar.png" alt="editar"
          class="w-[1.5rem] ml-[1rem] rounded-full p-[0.5rem] hover:bg-[#E5E7EB] cursor-pointer" 
          @click="edit"
        />
      </div>

      <button @click="uploadProduct()" class="bg-[#299CA9] border-none text-[#FFFFFF] rounded-[1.2rem] text-[15px] cursor-pointer pt-[0.5rem] pb-[0.5rem] w-fit pl-[1rem] pr-[1rem] right-[0rem] hover:bg-[#217d86]">
        Subir producto
      </button>
    </div>

    <div class=" ml-[6rem] mt-[3rem]">
        <h2>Sobre mí</h2>
    <p class="text-[0.95rem] text-gray-600">
        {{ profile_desc || '' }}
    </p>
    <div class="flex flex-row">
      <img v-if="location" src="/mapa.png" alt="mapa" class="w-[1.3rem] mr-[1rem]">
      <span class="text-[0.95rem] text-gray-600">
        {{ location || '' }}
      </span>
    </div>
    </div>

    <div id="products" class="m-[5rem]">
      <div>
        <button
          :class="['cursor-pointer flex-1 text-center py-2 bg-transparent pt-[10px] pb-[10px] pl-[25px] pr-[25px] mb-[30px] text-[19px] text-[#9f9a8f]', 
          activeTab === 'EnVenta' ? 'border-t-0 border-l-0 border-r-0 border-[#FFFDF8]' : 'border-none']"
          @click="activeTab = 'EnVenta'"
        >
          En venta
        </button>
        <button
          :class="['cursor-pointer ml-[2rem] flex-1 text-center py-2 bg-transparent pt-[10px] pb-[10px] pl-[25px] pr-[25px] mb-[30px] text-[19px] text-[#9f9a8f]', 
          activeTab === 'register' ? 'border-t-0 border-l-0 border-r-0 border-[#FFFDF8]' : 'border-none']"
          @click="activeTab = 'register'"
        >
          Vendidos
        </button>
      </div>
      <div>
        <EnVenta v-if="activeTab === 'EnVenta'" />
        <Vendidos v-else />
      </div>
    </div>
  </div>
</template>

<script setup>
import EnVenta from '../components/EnVenta.vue'
import Vendidos from '../components/Vendidos.vue'
import NavBar from '../components/NavBar.vue'
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const nombreUsuario = ref('')
const profile_pic = ref('')
const correo = ref('')
const profile_desc = ref('')
const activeTab = ref('EnVenta')
const location = ref('')

const route = useRoute()
const router = useRouter()

function getSafeItem(key) {
  const value = localStorage.getItem(key)
  return value === null || value === 'null' ? '' : value
}

nombreUsuario.value = getSafeItem('name')
profile_pic.value = getSafeItem('profile_pic')
correo.value = getSafeItem('mail')
profile_desc.value = getSafeItem('profile_desc')
location.value = getSafeItem('location')


function uploadProduct() {
  router.push('/upload-product/')
}

function edit() {
  router.push('/edit')
}
</script>
