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

                <span class="text-[1.5rem] ml-[1.5rem]">
                    {{ nombreUsuario || 'Iniciar sesión' }}
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
            <div class="">
                <EnVenta v-if="activeTab === 'EnVenta'"/>
                <Vendidos v-else/>
            </div>

        </div>
    </div>
</template>

<script setup>
import EnVenta from '../components/FEnVenta.vue'
import Vendidos from '../components/FVendidos.vue'
import NavBar from '../components/NavBar.vue'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../services/api'

const route = useRoute()
const router = useRouter()

const nombreUsuario = ref('')
const profile_pic = ref('')
const user = ref(null)
const activeTab = ref('EnVenta')

onMounted(async () => {
  try {
    const res = await api.get(`/users/${route.params.mail}/`)
    user.value = res.data
    nombreUsuario.value = user.value.name
    profile_pic.value = user.value.profile_pic
  } catch (err) {
    console.error('Error al cargar el usuario:', err)
  }
})
</script>