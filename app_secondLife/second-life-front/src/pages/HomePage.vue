<template>
  <div class="bg-[#FFFDF8]">
    <NavBar />
    <div class="pt-20 px-8 flex gap-6">
      <Filtros />

        <!-- Contenido principal -->
         <!-- Los productos del propio usuario logeado serán excluidos gracias a enviar el token en el get /products/ -->
        <main class="flex flex-col mt-[80px] p-[20px] ml-[20rem]">
          <h1 class="text-2xl font-bold">Bienvenido a SecondLife</h1>
          <div class="flex flex-wrap gap-[4rem]">
            <Item
              v-for="producto in productos"
              :key="producto.id"
              :producto="producto"
            />

          </div>
        </main>
      
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import api from '../services/api'
import NavBar from '../components/NavBar.vue'
import Filtros from '../components/FilterBar.vue'
import Item from '../components/Item.vue'

const productos = ref([])

onMounted(async () => {
  try {
    const response = await api.get('/products/')
    productos.value = response.data
  } catch (error) {
    console.error('Error al cargar productos:', error)
  }
})
</script>

