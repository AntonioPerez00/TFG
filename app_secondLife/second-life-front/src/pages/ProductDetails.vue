<template>
  <div class="bg-[#FFFDF8] min-h-screen" v-if="producto">
    <NavBar />

    <div class="flex justify-center">
      <div class="w-[48rem] h-[fit] bg-[#FFFFFF] mt-[8rem] mb-[8rem] shadow-[0_2px_4px_rgba(0,0,0,0.1)] rounded-[2rem] p-[2rem]">
        <div class="mb-[1.5rem] flex items-center gap-2">
          <img
            :src="producto.user.profile_pic || '/usuario.png'"
            class="w-[2.5rem] h-[2.5rem] rounded-full"
          />
          <span class="ml-[0.5rem]">{{ producto.user.name }}</span>
        </div>

        <div id="pictures" class="flex flex-row gap-[2rem]">
          <div>
            <img :src="producto.picture1 || '/usuario.png'"
              class="w-[23rem] rounded-[1rem]"      
            >
          </div>
          <div class="flex flex-row gap-[1rem] flex-wrap">
            <img :src="producto.picture2 || '/usuario.png'"
              class="w-[11rem] h-[14.7rem] rounded-[1rem]"      
            >
            <img :src="producto.picture3 || '/usuario.png'"
              class="w-[11rem] h-[14.7rem] rounded-[1rem]"     
            >
            <img :src="producto.picture4 || '/usuario.png'"
              class="w-[11rem] h-[15rem] rounded-[1rem]"       
            >
            <img :src="producto.picture5 || '/usuario.png'"
              class="w-[11rem] h-[15rem] rounded-[1rem]"     
            >
          </div>
        </div>  
        <div class="ml-[1rem] mt-[1rem] flex flex-col gap-[1rem]">
          <span class="text-[2rem] font-bold">
            {{ producto.price }} €
          </span>

          <span class="text-[2rem] font-bold">
            {{ producto.name }}
          </span>

          <span class="whitespace-pre-line text-[1rem]">
            {{ producto.description }}
          </span>

          <button @click="checkout(producto)" class="bg-[#299CA9] border-none text-[#FFFFFF] rounded-[1.2rem] pt-[10px] pb-[10px] pl-[25px] pr-[25px] text-[15px] cursor-pointer mt-[2rem]">
          Comprar
          </button>

        </div>

        
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../services/api'
import NavBar from '../components/NavBar.vue'

const route = useRoute()
const router = useRouter()
const producto = ref(null)
const loading = ref(true)
const backendURL = 'http://localhost:8000'
const currentIndex = ref(0)

const imgs = [
  producto.picture1,
  producto.picture2,
  producto.picture3,
  producto.picture4,
  producto.picture5,
].filter(Boolean)

function checkout(producto) {
  router.push(`/checkout/${producto.id}`)
}

function prevImage() {
  if (imgs.length === 0) return
  currentIndex.value = (currentIndex.value - 1 + imgs.length) % imgs.length
}

function nextImage() {
  if (imgs.length === 0) return
  currentIndex.value = (currentIndex.value + 1) % imgs.length
}

onMounted(async () => {
  try {
    const res = await api.get(`/products/${route.params.id}/`)
    producto.value = res.data
  } catch (error) {
    console.error('Error al cargar el producto:', error)
  } finally {
    loading.value = false
  }
})

</script>
