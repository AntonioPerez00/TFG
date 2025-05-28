<template>
  <div class="bg-[#FFFDF8]">
    <NavBar @buscar="filtrarProductos" />
    <div class="pt-20 px-8 flex gap-6">
      <Filtros />

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
import { ref, onMounted } from 'vue'
import api from '../services/api'
import NavBar from '../components/NavBar.vue'
import Filtros from '../components/FilterBar.vue'
import Item from '../components/Item.vue'

const productos = ref([])

async function filtrarProductos(busqueda) {
  try {
    const response = await api.get('/products/', {
      params: { search: busqueda }
    })
    productos.value = response.data
  } catch (error) {
    console.error('Error al cargar productos:', error)
  }
}

onMounted(() => {
  filtrarProductos('') // carga todos inicialmente
})
</script>
