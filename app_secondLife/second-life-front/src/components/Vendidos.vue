<template>
  <div class="flex flex-wrap gap-[4rem]">
    <Item
      v-for="producto in productos"
      :key="producto.id"
      :producto="producto"
      class="cursor-pointer relative"
      @click="myProductDetails(producto)"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'
import Item from '../components/Item.vue'
import { useRoute, useRouter } from 'vue-router'

const productos = ref([])
const loading = ref(true)
const router = useRouter()

// Por si usas filtros u otros parámetros:
const params = {disponibility: 'vendido'}

// Función opcional para manejar click
function myProductDetails(producto) {
  const url = router.resolve(`/my-product/${producto.id}`).href
  window.open(url, '_blank')
  // Aquí puedes redirigir, abrir modal, etc.
}

async function filtrarProductos(){
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
}

onMounted(async () => {
  filtrarProductos();
});

</script>
