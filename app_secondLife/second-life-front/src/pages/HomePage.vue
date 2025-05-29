<template>
  <div class="bg-[#FFFDF8] relative min-h-screen">
    <NavBar @buscar="filtrarProductos" />
    <div class="pt-20 px-8 flex gap-6">
      <Filtros />

      <main class="flex flex-col mt-[80px] p-[20px] ml-[20rem] flex-grow">
        <div><p class="text-[#9f9a8f] text-[18px]">Dale una segunda vida a tus cosas</p></div>
        <div class="flex flex-wrap gap-[4rem]">
          <Item
            v-for="producto in productos"
            :key="producto.id"
            :producto="producto"
          />
        </div>
      </main>
    </div>

    <!-- Spinner overlay -->
    <div v-if="loading" class="spinner-overlay">
      <div class="spinner"></div>
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
const loading = ref(false)

async function filtrarProductos(busqueda) {
  loading.value = true

  const fetchPromise = api.get('/products/', {
    params: { search: busqueda }
  })

  const delay = new Promise(resolve => setTimeout(resolve, 200)) // 1 segundo

  try {
    const [response] = await Promise.all([fetchPromise, delay])
    productos.value = response.data
  } catch (error) {
    console.error('Error al cargar productos:', error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  filtrarProductos('') // carga todos inicialmente
})
</script>

<style>
.spinner-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;    /* cubrir toda la pantalla */
  height: 100vh;   /* cubrir toda la pantalla */
  background-color: rgba(0, 0, 0, 0.4); /* fondo negro semi-transparente */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999; /* por encima de todo */
}

.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #299CA9;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
}

/* Animación giratoria */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
