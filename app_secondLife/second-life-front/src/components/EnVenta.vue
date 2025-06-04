<template>
  <div class="flex flex-wrap gap-[4rem]">
    <Item
      v-for="producto in productos"
      :key="producto.id"
      :producto="producto"
      class="cursor-pointer relative"
      @click="productDetails(producto)"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'
import Item from '../components/Item.vue'

const productos = ref([])
const loading = ref(true)

// Por si usas filtros u otros parámetros:
const params = {disponibility: 'en_venta'}

onMounted(async () => {
  try {
    const [response] = await Promise.all([
      api.get('/my-products/', { params }),
      new Promise(resolve => setTimeout(resolve, 200)) // pequeño delay opcional para el spinner
    ])
    productos.value = response.data
  } catch (error) {
    console.error('Error al cargar productos:', error)
  } finally {
    loading.value = false
  }
})

// Función opcional para manejar click
function productDetails(producto) {
  console.log('Ver producto', producto)
  // Aquí puedes redirigir, abrir modal, etc.
}

</script>
