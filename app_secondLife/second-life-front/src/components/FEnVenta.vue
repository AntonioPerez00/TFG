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
import { useRoute, useRouter } from 'vue-router'

const productos = ref([])
const loading = ref(true)
const route = useRoute()
const router = useRouter()
const token = localStorage.getItem('access_token')

const mail = route.params.mail // 👈 Esto es lo que faltaba

const params = { disponibility: 'en_venta' }

function productDetails(producto) {
  const url = router.resolve(`/product/${producto.id}`).href
  window.open(url, '_blank')
  // Aquí puedes redirigir, abrir modal, etc.
}

async function filtrarProductos(){
  try {
    const [response] = await Promise.all([
      api.get(`/users/${mail}/products/`, {
        params: { disponibility: 'en_venta' }
        
      }),
      new Promise(resolve => setTimeout(resolve, 200)) // Delay opcional
    ])
    productos.value = response.data
  } catch (error) {
    console.error('Error al cargar productos:', error)
  } finally {
    loading.value = false
  }
}

onMounted(filtrarProductos)
</script>
