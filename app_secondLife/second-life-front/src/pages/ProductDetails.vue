<template>
  <div class="bg-[#FFFDF8] min-h-screen" v-if="producto">
    <NavBar />

    <div class="flex justify-center">
      <div class="w-[48rem] h-[fit] bg-[#FFFFFF] mt-[8rem] mb-[8rem] shadow-[0_2px_4px_rgba(0,0,0,0.1)] rounded-[2rem] p-[2rem]">
        <div class="mb-[1.5rem] flex items-center gap-2 cursor-pointer
        hover:bg-[#eeeded] p-[6px] rounded-[20px] w-fit"
        @click="productUser">
          <img
            :src="producto.user.profile_pic || '/usuario.png'"
            class="w-[2.5rem] h-[2.5rem] rounded-full"
          />
          <span class="ml-[0.5rem]">{{ producto.user.name }}</span>
        </div>

        <!-- <div id="pictures" class="flex flex-row gap-[2rem]">
          <div v-if="producto.picture1">
            <img
              :src="producto.picture1"
              class="w-[23rem] rounded-[1rem]"
            />
          </div>
          <div class="flex flex-row gap-[1rem] flex-wrap">
            <img
              v-if="producto.picture2"
              :src="producto.picture2"
              class="w-[11rem] h-[15rem] rounded-[1rem]"
            />
            <img
              v-if="producto.picture3"
              :src="producto.picture3"
              class="w-[11rem] h-[15rem] rounded-[1rem]"
            />
            <img
              v-if="producto.picture4"
              :src="producto.picture4"
              class="w-[11rem] h-[15rem] rounded-[1rem]"
            />
            <img
              v-if="producto.picture5"
              :src="producto.picture5"
              class="w-[11rem] h-[15rem] rounded-[1rem]"
            />
          </div>
        </div> -->

        <div id="pictures" class="flex justify-center">
          <div class="relative w-[30rem] h-[35rem] flex items-center justify-center mb-[2rem]">
            <img
              :src="imgs[currentIndex] || '/usuario.png'"
              alt="producto"
              class="w-full h-full rounded-[1rem] object-cover"
            />

            <button
              @click.stop="prevImage"
              class="absolute left-[0rem] top-1/2 transform -translate-y-1/2 bg-[#ffffffcc] border-none py-2 px-3 hover:bg-[#d3d3d3] text-[2rem] rounded-full z-10"
              aria-label="Imagen anterior"
            >
              ‹
            </button>

            <button
              @click.stop="nextImage"
              class="absolute right-[0rem] top-1/2 transform -translate-y-1/2 bg-[#ffffffcc] border-none py-2 px-3 hover:bg-[#d3d3d3] text-[2rem] rounded-full z-10"
              aria-label="Imagen siguiente"
            >
              ›
            </button>
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

          <button @click="checkout(producto)" class="bg-[#299CA9] border-none text-[#FFFFFF] rounded-[1.2rem] pt-[10px] pb-[10px] pl-[25px] pr-[25px] text-[15px] cursor-pointer mt-[2rem] hover:bg-[#217d86]">
          Comprar
          </button>

        </div>

        
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../services/api'
import NavBar from '../components/NavBar.vue'

onMounted(async () => {
  try {
    const res = await api.get(`/products/${route.params.id}/`)
    producto.value = res.data
  } catch (error) {
    console.error('Error al cargar el producto:', error)
  } finally {
    loading.value = false
  }
  console.log(producto.value?.picture1)

})

const route = useRoute()
const router = useRouter()
const producto = ref(null)
const loading = ref(true)
const backendURL = 'http://localhost:8000'
const currentIndex = ref(0)

const imgs = computed(() => {
  if (!producto.value) return []
  return [
    producto.value.picture1,
    producto.value.picture2,
    producto.value.picture3,
    producto.value.picture4,
    producto.value.picture5,
  ].filter(Boolean)
})

function productUser() {
  console.log(producto.value.user.mail)
  const url = router.resolve(`/fuser/${producto.value.user.mail}`).href
  console.log(url)
  router.push(url)
}

function checkout(producto) {
  router.push(`/checkout/${producto.id}`)
}

function prevImage() {
  if (imgs.value.length === 0) return
  currentIndex.value = (currentIndex.value - 1 + imgs.value.length) % imgs.value.length
}

function nextImage() {
  if (imgs.value.length === 0) return
  currentIndex.value = (currentIndex.value + 1) % imgs.value.length
}



</script>
