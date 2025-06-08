<template>
  <div class="flex flex-col relative w-[9rem]">
    <img
      :src="imgs[currentIndex] || '/usuario.png'"
      alt="producto"
      class="w-[9rem] h-[12rem] rounded-[0.75rem] mb-[0.5rem] object-cover"
    />

    <!-- Botón izquierdo -->
    <button
      @click.stop="prevImage"
      class="absolute top-1/2  transform -translate-y-1/2 bg-transparent border-none py-1 hover:bg-[#D3D3D3] text-[1.7rem] z-10"
      aria-label="Imagen anterior"
    >
      ‹
    </button>

    <!-- Botón derecho -->
    <button
      @click.stop="nextImage" 
      class="absolute top-1/2 right-[0px] transform -translate-y-1/2 bg-transparent border-none px-2 py-1 hover:bg-[#D3D3D3] text-[1.7rem] hover:bg-gray-400 z-10"
      aria-label="Imagen siguiente"
    >
      ›
    </button>

    <div class="flex flex-col pl-[0.4rem] gap-[0.2rem]">
      <span class="precio">{{ producto.price }} €</span>
      <span>{{ producto.name }}</span>
      <span>{{ producto.state }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const { producto } = defineProps({
  producto: Object
})

const imgs = [
  producto.picture1,
  producto.picture2,
  producto.picture3,
  producto.picture4,
  producto.picture5,
].filter(Boolean)

const currentIndex = ref(0)

function prevImage() {
  if (imgs.length === 0) return
  currentIndex.value = (currentIndex.value - 1 + imgs.length) % imgs.length
}

function nextImage() {
  if (imgs.length === 0) return
  currentIndex.value = (currentIndex.value + 1) % imgs.length
}
</script>

<style>
.precio {
  font-weight: 700;
}
</style>
