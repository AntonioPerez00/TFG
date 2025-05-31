<template>
  <div class="bg-[#FFFDF8] min-h-screen" v-if="producto">
    <NavBar />

    <div class="flex justify-center">
      <div class="w-[48rem] h-[fit] bg-[#FFFFFF] mt-[8rem] shadow-[0_2px_4px_rgba(0,0,0,0.1)] rounded-[2rem] p-[2rem]">
        <div>
          <img
            :src="getFullImageUrl(producto?.user?.profile_pic)"
            alt="usuario"
            class="w-[2.5rem] h-[2.5rem] rounded-full"
          />

        </div>
        <div id="pictures" class="flex flex-row gap-[2rem]">
          <div>
            <img :src="producto.picture || '/usuario.png'"
              class="w-[23rem] rounded-[1rem]"      
            >
          </div>
          <div class="flex flex-row gap-[1rem] flex-wrap">
            <img :src="producto.picture || '/usuario.png'"
              class="w-[11rem] h-[14.7rem] rounded-[1rem]"      
            >
            <img :src="producto.picture || '/usuario.png'"
              class="w-[11rem] h-[14.7rem] rounded-[1rem]"     
            >
            <img :src="producto.picture || '/usuario.png'"
              class="w-[11rem] h-[15rem] rounded-[1rem]"       
            >
            <img :src="producto.picture || '/usuario.png'"
              class="w-[11rem] h-[15rem] rounded-[1rem]"     
            >
          </div>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '../services/api'
import NavBar from '../components/NavBar.vue'

const route = useRoute()
const producto = ref(null)
const loading = ref(true)
const backendURL = 'http://localhost:8000'

const getFullImageUrl = (path) => {
  if (!path) return '/usuario.png'
  return path.startsWith('http') ? path : `${backendURL}${path.startsWith('/') ? '' : '/'}${path}`
}

onMounted(async () => {
  try {
    const res = await api.get(`/products/${route.params.id}/`)
    producto.value = res.data
    console.log('Producto recibido:', producto.value)
    console.log('User dentro del producto:', producto.value.user)
  } catch (error) {
    console.error('Error al cargar el producto:', error)
  } finally {
    loading.value = false
  }
})

</script>
