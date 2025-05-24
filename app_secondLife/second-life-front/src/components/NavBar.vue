<template>
  <nav
    :class="['fixed top-0 left-0 w-full bg-white shadow-md z-50 px-6 py-3 flex justify-between items-center transition-transform duration-300', 
      isVisible ? 'translate-y-0' : '-translate-y-full']">
    <div class="text-xl font-bold">SecondLife</div>
    <div class="space-x-4">
      <button class="text-gray-600 hover:text-black">Inicio</button>
      <button class="text-gray-600 hover:text-black">Categorías</button>
      <button class="text-gray-600 hover:text-black">Mi cuenta</button>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isVisible = ref(true)
let lastScrollY = window.scrollY

function handleScroll() {
  const currentY = window.scrollY
  isVisible.value = currentY < lastScrollY || currentY < 10
  lastScrollY = currentY
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})
onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>
