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

            <button @click="uploadProduct()" class="bg-[#299CA9] border-none text-[#FFFFFF] rounded-[1.2rem] text-[15px] cursor-pointer pt-[0.5rem] pb-[0.5rem] w-fit pl-[1rem] pr-[1rem] right-[0rem]">
            Subir producto
            </button>

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
import EnVenta from '../components/EnVenta.vue'
import Vendidos from '../components/Vendidos.vue'
import NavBar from '../components/NavBar.vue'
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const nombreUsuario = ref('')
const profile_pic = ref('')

const activeTab = ref('EnVenta')

const route = useRoute()
const router = useRouter()

nombreUsuario.value = localStorage.getItem('name')
profile_pic.value = localStorage.getItem('profile_pic')

function uploadProduct() {
    router.push('/upload-product/')
}


</script>
