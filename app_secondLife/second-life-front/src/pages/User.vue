<template>
    <NavBar />

    <div class="p-[5rem] bg-[#FFFDF8]">
        <div id="user" class="mt-[5rem] w-full flex flex-row items-center justify-between">
            
            <div class="flex flex-row items-center">
                <img
                    :src="profile_pic || '/usuario.png'"
                    alt="usuario"
                    class="w-[6rem] h-[6rem] rounded-full"
                />
                <span class="text-[1.5rem] ml-[1.5rem]">
                    {{ nombreUsuario || 'Iniciar sesión' }}
                </span>
            </div>

            <button @click="checkout(producto)" class="bg-[#299CA9] border-none text-[#FFFFFF] rounded-[1.2rem] text-[15px] cursor-pointer pt-[0.5rem] pb-[0.5rem] w-fit pl-[1rem] pr-[1rem] right-[0rem]">
            Subir producto
            </button>

        </div>

        <div id="products">

        </div>
    </div>
</template>

<script setup>
import NavBar from '../components/NavBar.vue'
import { ref } from 'vue'

const nombreUsuario = ref('')
const profile_pic = ref('')

nombreUsuario.value = localStorage.getItem('name')
profile_pic.value = localStorage.getItem('profile_pic')


</script>
